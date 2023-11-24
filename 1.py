class User:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
        else:
            print("Insufficient funds!")

    def transfer(self, recipient, amount):
        if amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient.user_id}")
        else:
            print("Insufficient funds!")

    def display_balance(self):
        print(f"Balance: ${self.balance}")

    def display_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)


class ATM:
    def authenticate_user(self, user_id, pin, users):
        for user in users:
            if user.user_id == user_id and user.pin == pin:
                return user
        return None


def main():
    # Sample users
    user1 = User("12345", "1234", 1000)
    user2 = User("67890", "5678", 500)

    users = [user1, user2]

    atm = ATM()

    # User login
    user_id = input("Enter user ID: ")
    pin = input("Enter PIN: ")

    current_user = atm.authenticate_user(user_id, pin, users)

    if current_user:
        print(f"Welcome, {current_user.user_id}!")

        while True:
            print("\nOptions:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Display Balance")
            print("5. Display Transaction History")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                amount = float(input("Enter deposit amount: "))
                current_user.deposit(amount)
            elif choice == "2":
                amount = float(input("Enter withdrawal amount: "))
                current_user.withdraw(amount)
            elif choice == "3":
                recipient_id = input("Enter recipient's user ID: ")
                recipient = atm.authenticate_user(recipient_id, "", users)
                if recipient:
                    amount = float(input("Enter transfer amount: "))
                    current_user.transfer(recipient, amount)
                else:
                    print("Recipient not found.")
            elif choice == "4":
                current_user.display_balance()
            elif choice == "5":
                current_user.display_transaction_history()
            elif choice == "6":
                print("Exiting. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    else:
        print("Invalid user ID or PIN. Access denied.")


if __name__ == "__main__":
    main()
