"""Single Responsibility Principle example in the finance domain.

Classes:
 - Account: simple data holder for account information.
 - Ledger: records transaction entries (immutable responsibility: record-keeping).
 - NotificationService: sends notifications (printing in this demo).
 - TransactionService: performs deposits/withdrawals and coordinates ledger + notifications.
 - ReportGenerator: builds account statements from ledger entries.

Each class has one reason to change.
"""
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Account:
    account_id: str
    owner: str
    email: str
    balance: float = 0.0


class Ledger:
    """Responsible only for recording transactions."""

    def __init__(self):
        self._entries: List[Dict] = []

    def record(self, account_id: str, kind: str, amount: float, balance: float) -> None:
        entry = {
            'account_id': account_id,
            'type': kind,
            'amount': amount,
            'balance': balance,
        }
        self._entries.append(entry)

    def entries_for(self, account_id: str) -> List[Dict]:
        return [e for e in self._entries if e['account_id'] == account_id]


class NotificationService:
    """Responsible only for sending notifications to users.

    In production this might send emails/SMS; here it prints for clarity.
    """

    def notify(self, email: str, subject: str, body: str) -> None:
        print(f"Notify {email}: {subject}\n{body}\n")


class TransactionService:
    """Responsible for business rules around transactions (deposit/withdraw).

    It delegates persistence to Ledger and communication to NotificationService.
    """

    def __init__(self, ledger: Ledger, notifier: NotificationService):
        self.ledger = ledger
        self.notifier = notifier

    def deposit(self, account: Account, amount: float) -> None:
        if amount <= 0:
            raise ValueError('Deposit amount must be positive')
        account.balance += amount
        self.ledger.record(account.account_id, 'deposit', amount, account.balance)
        self.notifier.notify(
            account.email,
            'Deposit received',
            f'Hi {account.owner}, your deposit of {amount:.2f} was successful. New balance: {account.balance:.2f}'
        )

    def withdraw(self, account: Account, amount: float) -> None:
        if amount <= 0:
            raise ValueError('Withdrawal amount must be positive')
        if amount > account.balance:
            # Business rule: insufficient funds
            self.notifier.notify(
                account.email,
                'Withdrawal failed',
                f'Hi {account.owner}, attempted withdrawal of {amount:.2f} failed due to insufficient funds.'
            )
            raise ValueError('Insufficient funds')
        account.balance -= amount
        self.ledger.record(account.account_id, 'withdraw', amount, account.balance)
        self.notifier.notify(
            account.email,
            'Withdrawal processed',
            f'Hi {account.owner}, your withdrawal of {amount:.2f} was processed. New balance: {account.balance:.2f}'
        )


class ReportGenerator:
    """Responsible for generating simple textual reports from the ledger."""

    @staticmethod
    def account_statement(account: Account, ledger: Ledger) -> str:
        entries = ledger.entries_for(account.account_id)
        lines = [f"Statement for {account.owner} (Account: {account.account_id})", '-' * 40]
        for e in entries:
            lines.append(f"{e['type'].title():10} {e['amount']:10.2f}  Balance: {e['balance']:10.2f}")
        lines.append('-' * 40)
        lines.append(f"Current balance: {account.balance:.2f}")
        return '\n'.join(lines)


def main():
    ledger = Ledger()
    notifier = NotificationService()
    tx = TransactionService(ledger, notifier)

    alice = Account('A-100', 'Alice Example', 'alice@example.com', balance=100.0)

    tx.deposit(alice, 50)
    try:
        tx.withdraw(alice, 30)
    except ValueError:
        pass

    report = ReportGenerator.account_statement(alice, ledger)
    print(report)


if __name__ == '__main__':
    main()
