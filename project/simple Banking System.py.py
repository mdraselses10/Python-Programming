# simple Banking System.py

# Class representing a bank account
class BankAccount:
    def __init__(self, account_number, owner_name, initial_balance=0.0):

        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = initial_balance

    def deposit(self, amount):

        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):

        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            print("Withdrawal amount must be positive!")

    def check_balance(self):

        return self.balance


def main():

    accounts = {}

    while True:
        print("\n--- Simple Banking System ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':

            account_number = input("Enter a unique account number: ")
            if account_number in accounts:
                print("Account number already exists! Please try again.")
            else:
                owner_name = input("Enter account owner's name: ")
                initial_balance = float(input("Enter initial deposit (or 0 if none): "))
                accounts[account_number] = BankAccount(account_number, owner_name, initial_balance)
                print(f"Account created successfully for {owner_name}.")

        elif choice == '2':

            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter amount to deposit: "))
                accounts[account_number].deposit(amount)
            else:
                print("Account not found!")

        elif choice == '3':

            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter amount to withdraw: "))
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found!")

        elif choice == '4':

            account_number = input("Enter account number: ")
            if account_number in accounts:
                balance = accounts[account_number].check_balance()
                print(f"Current balance: ${balance:.2f}")
            else:
                print("Account not found!")

        elif choice == '5':

            print("Thank you for using the Simple Banking System. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a valid option.")



if __name__ == "__main__":
    main()
