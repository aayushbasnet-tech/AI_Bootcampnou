class BankAccount:
    def __init__(self,balance):
        self.__balance=balance

    def deposit(self,amount):
        self.__balance+=amount

    def show_balance(self):
        print("Balance:",self.__balance)

b=BankAccount(5000)
b.__balance=1000
b.deposit(1000)
b.show_balance()
# b.__balance cannot change the current balance since __balance is private so cannot be accessed