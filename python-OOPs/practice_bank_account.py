class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Transaction successful.")
        else:
            print(
                "You cannot withdraw.",
                "Amount should be less than or equal to",
                self.balance
            )

    def show_balance(self):
        print("Account holder:", self.account_holder)
        print("Balance:", self.balance)


# Create an object
account = BankAccount("Karan", 1000)

account.show_balance()

account.deposit(500)
account.show_balance()

account.withdraw(300)
account.show_balance()

account.withdraw(1500)