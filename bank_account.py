first_name = input("Enter your first name: ")
middle_name = input("Enter your middle name: ")
last_name = input("Enter your last name: ")
account_type = input("Enter your account type (savings or checkings): ")
balance = 0
other_account = "old savings"


class BankAccount:
    def __init__(self, first_name, middle_name, last_name, account_type, balance, status):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.account_type = account_type
        self.balance = balance
        self.status = status

    def open_account(self, balance):
        self.balance = int(input("Enter deposit amount: "))
        if (self.balance >= 100):
            self.status = "open"
            print("congrats on your new account")

        else:
            print("There are not enough funds to open an account")
    def show_balance(self):
        print(self.balance)

    def transfer_money(self, account_type, balance, other_account, transfer_amount):
        transfer_amount = int(transfer_amount)
        if (self.status == "open"):
            self.balance -= transfer_amount
            other_account.balance += transfer_amount
            if (self.balance < 0):
                self.balance -= 35
            print(self.balance)
            return self.balance

    def withdraw_money(self, account_type, withdraw_amount, balance):
        if (self.account_type == "freeze"):
            print("Cannot withdaw, your {0} is frozen".format(account_type))
        elif (self.account_type == "closed"):
            print("That account has been closed")
        else:
            self.balance -= withdraw_amount
            if (self.balance < 0):
                self.balance -= 35
            print(self.balance)
            return self.balance

        

    def options(self):
        decision = input("Enter 'o' to open an account, 't' to transfer money, 'w' to withdraw money, or 'b' to show your balance: ")
        
        if (decision == "o"):
            self.open_account(0)
        
        if (decision == "t"):
            transfer_amount = int(input("how much would you like to transfer?: "))
            self.transfer_money(self.account_type, self.balance, other_account, transfer_amount)
        
        if (decision == "w"):
            withdraw_amount = int(input("How much would you like to withdraw?: "))
            self.withdraw_money(self.account_type, withdraw_amount, self.balance)
        
        if (decision == "b"):
            self.show_balance()
        
        else:
            print("invalid command")

person1 = BankAccount(first_name, middle_name, last_name, account_type, balance, "closed")
other_account = BankAccount(first_name, middle_name, last_name, account_type, 500, "open")

person1.open_account(balance)
while True:
    person1.options()
    break