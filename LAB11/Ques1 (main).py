from Ques1 import Account

def main():
    print("Welcome to the Bank!")

    # Create an account
    account_number = input("Enter Account Number: ")
    account_name = input("Enter Account Name: ")
    initial_balance = float(input("Enter Initial Balance: "))
    new_account = Account(account_number, account_name, initial_balance)

    while True:
        print("\nMenu:")
        print("1. Display Account Details")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            new_account.display_account_details()
        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            new_account.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            new_account.withdraw(amount)
        elif choice == "4":
            new_account.transaction_history_report()
        elif choice == "5":
            print("Thank you for using our banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
