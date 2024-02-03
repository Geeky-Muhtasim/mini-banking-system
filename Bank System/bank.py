class User:

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_user_details(self):
        print("Personal Details")
        print("")
        print("Name: " , self.name)
        print("Age: " , self.age)
        print("Gender: ", self.gender)


class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0

    def deposit(self,amount):
        self.amount = amount
        self.balance += self.amount
        print("Account balance has been updated")
        print("Total deposited: $" , self.amount)
    
    def withdraw(self,amount):
        self.amount = amount        
        if self.balance>self.amount:
            self.balance -= self.amount
            print("Withdrawl Successful")
        else:
            print("Insufficient Balance $" , self.balance)

    def view_balance(self):
        self.show_user_details()
        print("Balance: $", self.balance)


shochcho = Bank("Shochcho", 24, "Male")

shochcho.deposit(20000)
shochcho.withdraw(7000)
shochcho.view_balance()