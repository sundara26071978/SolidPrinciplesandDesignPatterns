import pytest
from unittest.mock import Mock

import finance_srp as fs


def test_deposit_records_ledger_and_notifies():
    ledger = fs.Ledger()
    notifier = Mock(spec=fs.NotificationService)
    tx = fs.TransactionService(ledger, notifier)

    acct = fs.Account('X1', 'Test User', 'test@example.com', balance=0.0)
    tx.deposit(acct, 200.0)

    # ledger entry recorded
    entries = ledger.entries_for('X1')
    assert len(entries) == 1
    assert entries[0]['type'] == 'deposit'
    assert entries[0]['amount'] == 200.0

    # notifier called once
    notifier.notify.assert_called_once()

    # balance updated
    assert acct.balance == 200.0


def test_withdraw_insufficient_funds_notifies_and_raises():
    ledger = fs.Ledger()
    notifier = Mock(spec=fs.NotificationService)
    tx = fs.TransactionService(ledger, notifier)

    acct = fs.Account('X2', 'Low Funds', 'low@example.com', balance=50.0)

    with pytest.raises(ValueError):
        tx.withdraw(acct, 100.0)

    # ensure a notification was sent about failure
    notifier.notify.assert_called_once()

    # balance unchanged
    assert acct.balance == 50.0


def test_withdraw_success_records_and_notifies():
    ledger = fs.Ledger()
    notifier = Mock(spec=fs.NotificationService)
    tx = fs.TransactionService(ledger, notifier)

    acct = fs.Account('X3', 'Rich User', 'rich@example.com', balance=500.0)
    tx.withdraw(acct, 150.0)

    entries = ledger.entries_for('X3')
    assert len(entries) == 1
    assert entries[0]['type'] == 'withdraw'
    assert entries[0]['amount'] == 150.0

    notifier.notify.assert_called_once()
    assert acct.balance == 350.0
