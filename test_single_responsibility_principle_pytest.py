import pytest
from unittest.mock import Mock, patch

import single_responsibility_principle as srp


def test_register_user_with_mock_injection(capsys):
    """Inject a Mock EmailService and assert send_email is called with expected args."""

    mock_email_service = Mock(spec=srp.EmailService)
    registration = srp.UserRegistration(mock_email_service)

    registration.register_user('Eve', 'eve@example.com')

    mock_email_service.send_email.assert_called_once_with(
        'eve@example.com',
        'Welcome!',
        'Hello Eve, thank you for registering!'
    )

    captured = capsys.readouterr()
    assert 'User Eve registered successfully.' in captured.out


def test_register_user_with_patch_object(capsys):
    """Patch EmailService.send_email and verify it was called for an actual EmailService instance."""

    with patch.object(srp.EmailService, 'send_email') as mock_send:
        registration = srp.UserRegistration(srp.EmailService())
        registration.register_user('Frank', 'frank@example.com')

    mock_send.assert_called_once_with(
        'frank@example.com',
        'Welcome!',
        'Hello Frank, thank you for registering!'
    )

    captured = capsys.readouterr()
    assert 'User Frank registered successfully.' in captured.out
