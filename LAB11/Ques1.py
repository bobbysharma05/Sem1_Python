from datetime import datetime

class Account:
    def __init__(self, account_number, account_name, initial_balance=0.0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance_amount = initial_balance
        self.status = "Active"
        self.transaction_history = []

    def display_account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Name: {self.account_name}")
        print(f"Balance Amount: ${self.balance_amount}")
        print(f"Account Status: {self.status}")

    def deposit(self, amount):
        if amount > 0:
            self.balance_amount += amount
            self._add_transaction("Deposit", amount)
            print(f"Deposit successful. New balance: ${self.balance_amount}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance_amount:
            self.balance_amount -= amount
            self._add_transaction("Withdrawal", amount)
            print(f"Withdrawal successful. New balance: ${self.balance_amount}")
        else:   
            print("Invalid withdrawal amount or insufficient balance.")

    def transaction_history_report(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def _add_transaction(self, transaction_type, amount):
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.transaction_history.append(transaction)
        if len(self.transaction_history) > 5:
            self.transaction_history.pop(0)  # Keep only the last 5 transactions
