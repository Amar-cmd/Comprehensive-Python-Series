# Online Payment System (Beginner Friendly, Console Based)
# OOP: Abstraction (ABC) + Polymorphism
# Menu: match-case (Python 3.10+)

from abc import ABC, abstractmethod
import random


# -------------------- Abstract Class --------------------
class Payment(ABC):
    @abstractmethod
    def validate(self, details: dict) -> bool:
        pass

    @abstractmethod
    def pay(self, amount: float, details: dict) -> None:
        pass

    def transaction_summary(self, amount: float, status: str, mode: str, txn_id: int) -> None:
        print("\n--- Transaction Summary ---")
        print("Mode   :", mode)
        print("Amount :", amount)
        print("Status :", status)
        print("Txn ID :", txn_id)


# -------------------- Payment Types --------------------
class CreditCardPayment(Payment):
    def validate(self, details: dict) -> bool:
        card_no = details.get("card_no", "")
        cvv = details.get("cvv", "")

        if len(card_no) != 16 or not card_no.isdigit():
            print("Validation failed: Card number must be 16 digits.")
            return False
        if len(cvv) != 3 or not cvv.isdigit():
            print("Validation failed: CVV must be 3 digits.")
            return False
        return True

    def pay(self, amount: float, details: dict) -> None:
        print("Processing card payment...")
        print("Payment Successful via Credit Card")


class UPIPayment(Payment):
    def validate(self, details: dict) -> bool:
        upi = details.get("upi_id", "")
        if "@" not in upi or upi.strip() == "":
            print("Validation failed: Invalid UPI ID")
            return False
        return True

    def pay(self, amount: float, details: dict) -> None:
        print("Processing UPI payment...")
        print("Payment Successful via UPI")


class NetBankingPayment(Payment):
    def validate(self, details: dict) -> bool:
        bank = details.get("bank", "")
        user = details.get("user_id", "")
        pwd = details.get("password", "")

        if bank.strip() == "":
            print("Validation failed: Bank name cannot be empty")
            return False
        if user.strip() == "" or pwd.strip() == "":
            print("Validation failed: User ID/Password cannot be empty")
            return False
        return True

    def pay(self, amount: float, details: dict) -> None:
        print("Processing Net Banking payment...")
        print("Payment Successful via Net Banking")


# -------------------- Gateway (Polymorphism) --------------------
class PaymentGateway:
    def process(self, payment_obj: Payment, amount: float, details: dict) -> None:
        mode = payment_obj.__class__.__name__.replace("Payment", "")
        txn_id = random.randint(10000, 99999)

        if payment_obj.validate(details):  # polymorphism
            payment_obj.pay(amount, details)  # polymorphism
            payment_obj.transaction_summary(amount, "SUCCESS", mode, txn_id)
        else:
            payment_obj.transaction_summary(amount, "FAILED", mode, txn_id)


# -------------------- Helpers --------------------
def read_float(prompt: str) -> float:
    while True:
        try:
            x = float(input(prompt).strip())
            return x
        except ValueError:
            print("Enter a valid number.")


def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Enter a valid choice.")


# -------------------- Main Program --------------------
gateway = PaymentGateway()

while True:
    print("\n--- Online Payment System ---")
    print("1. Credit Card")
    print("2. UPI")
    print("3. Net Banking")
    print("4. Exit")

    choice = read_int("Choose payment method: ")

    match choice:
        case 1:
            amount = read_float("Enter amount: ")
            details = {
                "card_no": input("Enter 16-digit card number: ").strip(),
                "cvv": input("Enter 3-digit CVV: ").strip(),
            }
            gateway.process(CreditCardPayment(), amount, details)

        case 2:
            amount = read_float("Enter amount: ")
            details = {"upi_id": input("Enter UPI ID (name@bank): ").strip()}
            gateway.process(UPIPayment(), amount, details)

        case 3:
            amount = read_float("Enter amount: ")
            details = {
                "bank": input("Enter bank name: ").strip(),
                "user_id": input("Enter user id: ").strip(),
                "password": input("Enter password: ").strip(),
            }
            gateway.process(NetBankingPayment(), amount, details)

        case 4:
            print("Bye!")
            break

        case _:
            print("Invalid choice.")
