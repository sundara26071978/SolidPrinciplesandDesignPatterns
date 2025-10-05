"""Open/Closed Principle example.

PaymentProcessor is closed for modification but open for extension via new
PaymentMethod implementations. Each payment method implements a common
interface (process) so the processor doesn't need to change when new methods
are added.

"""
from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def process(self, amount: float) -> bool:
        """Process the payment of the given amount. Return True on success."""


class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def process(self, amount: float) -> bool:
        # placeholder for real card processing logic
        print(f"Charging {amount:.2f} to credit card {self.card_number}")
        return True


class PaypalPayment(PaymentMethod):
    def __init__(self, account_email: str):
        self.account_email = account_email

    def process(self, amount: float) -> bool:
        print(f"Charging {amount:.2f} to PayPal account {self.account_email}")
        return True


class PaymentProcessor:
    """Processor depends on PaymentMethod abstraction, not concrete types."""

    def __init__(self):
        self.methods = []

    def register_method(self, method: PaymentMethod):
        if not isinstance(method, PaymentMethod):
            raise TypeError("method must implement PaymentMethod")
        self.methods.append(method)

    def charge_all(self, amount: float) -> dict:
        """Charge the amount using all registered methods.

        Returns a mapping of method index -> boolean success.
        """
        results = {}
        for i, method in enumerate(self.methods):
            try:
                success = method.process(amount)
            except Exception:
                success = False
            results[i] = bool(success)
        return results


# Example of extending without modifying PaymentProcessor: a new method
class CryptoPayment(PaymentMethod):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def process(self, amount: float) -> bool:
        print(f"Transferring {amount:.2f} in crypto to {self.wallet_address}")
        return True


def main():
    processor = PaymentProcessor()
    processor.register_method(CreditCardPayment('4242-4242-4242-4242'))
    processor.register_method(PaypalPayment('user@example.com'))
    processor.register_method(CryptoPayment('0xabc123'))

    results = processor.charge_all(10.0)
    print('Results:', results)


if __name__ == '__main__':
    main()
