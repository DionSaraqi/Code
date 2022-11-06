from ATM import myacc

while True:
    try:
        pasn = input("Type in your name: ")
        pas = int(input("Type in your password: "))
        ps = myacc.login(pasn,pas)
        if ps == False: 
            print("Wrong credentials, please try again")
        elif ps == True: 
            
            while True:
                ask = input("Do you want to Deposit, Withdraw, Display your balance or Exit? ")
                if ask == "Deposit":
                    myacc.deposit()
                elif ask == "Withdraw":
                    myacc.withdraw()
                elif ask == "Display":
                    myacc.display()
                elif ask == "Exit":
                    print("This program has been terminated!")  
                    quit()
                else:
                    print("Invalid input!")
    except:
        print("To use the program again, re-run it!")
        exit()