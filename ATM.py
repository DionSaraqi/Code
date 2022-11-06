class Bank(object):
    def __init__(self,name,password,balance):
        self.name = name
        self.password = password
        self.balance = balance
    
    def display(self):
        print(f"You have {self.balance}$ in your account.")

    def deposit(self):
        try:
            inp = int(input("How much do you want to deposit?: "))
        
            if inp > 0:
                print(f"{inp}$ has been added to your account.")
                self.balance = self.balance + inp
            else:
                print("Invlaid input!")
                myacc.deposit()
        except:
            print("Invalid input, try again?")
            myacc.deposit()
    
    def withdraw(self):
        try:
            inp1 = int(input("How much money do you to withdraw from your account?: "))
            if inp1 > self.balance:
                print("You do not have sufficient funds, try again!")
                myacc.withdraw()
            else:
                self.balance = self.balance - inp1
                print(f"{inp1}$ have been withdrawed from your account.")
        except:
            print("Invalid input, try again!")
            myacc.withdraw()

    def login(self,name,password):
        try:
            if password == self.password and name==self.name:
                print("Your name and password are correct!")
                return True 
            else:
                print("Your name and password are incorrect, try again!")
                return False 
        except:
            print("Invalid input, your password must only contain numbers, try again!")
            myacc.login()
            

myacc = Bank("Dion",123456,1500)



