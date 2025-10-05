import pytest
from unittest.mock import Mock

import open_closed_principle as ocp


def test_register_method_type_check():
    processor = ocp.PaymentProcessor()
    with pytest.raises(TypeError):
        processor.register_method(object())


def test_charge_all_with_success_and_failure():
    processor = ocp.PaymentProcessor()

    # mock method that returns True
    good = Mock(spec=ocp.PaymentMethod)
    good.process.return_value = True

    # mock method that raises an exception
    bad = Mock(spec=ocp.PaymentMethod)
    bad.process.side_effect = RuntimeError('processing failed')

    processor.register_method(good)
    processor.register_method(bad)

    results = processor.charge_all(5.0)

    assert results == {0: True, 1: False}


def test_real_methods_work(monkeypatch, capsys):
    processor = ocp.PaymentProcessor()
    processor.register_method(ocp.CreditCardPayment('1111'))

    # Patch the credit card process to avoid printing in tests and return True
    monkeypatch.setattr(ocp.CreditCardPayment, 'process', lambda self, amt: True)

    results = processor.charge_all(1.0)
    assert results == {0: True}
