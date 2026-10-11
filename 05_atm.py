name=input("enter your name: ")
pin=int(input("enter your pin: "))
balance=100000
if pin==1234:
    print("choose option")
    print("1. balance inquiry")
    print("2. withdrawl money")
    print("3. deposit money")
    choice=int(input("choose option: "))
    if choice==1:
        print("your balance is: ",balance)
    elif choice==2:
        withdrawl=int(input("enter witdrawl amount: "))
        if withdrawl <= balance:
            balance -= withdrawl
            print("your withdrawl of amount: ", withdrawl)
            print("your balance is: ", balance)
        else:
            print("insufficent balance")
    elif choice==3:
        deposit=int(input("enter deposit amount: "))
        balance = deposit+balance
        print("your deposit of amount: ", deposit )
        print("your balance is: ", balance)
    else:
        print("invalid option choose a valid one")
else:
    print("wrong pin please try again")


