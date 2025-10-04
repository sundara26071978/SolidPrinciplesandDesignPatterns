import single_responsibility_principle as srp


def test_register_user_sends_email_and_prints(monkeypatch, capsys):
    """UserRegistration should call EmailService.send_email with correct args and print success."""

    recorded = []

    def fake_send_email(self, email, subject, body):
        recorded.append((email, subject, body))

    # Replace the EmailService.send_email with our fake
    monkeypatch.setattr(srp.EmailService, 'send_email', fake_send_email)

    registration = srp.UserRegistration(srp.EmailService())
    registration.register_user('Dana', 'dana@example.com')

    # Verify email was sent with expected values
    assert recorded == [
        (
            'dana@example.com',
            'Welcome!',
            'Hello Dana, thank you for registering!'
        )
    ]

    # Verify printed registration success is present
    captured = capsys.readouterr()
    assert 'User Dana registered successfully.' in captured.out
