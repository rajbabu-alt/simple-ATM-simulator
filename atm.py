
balance = 1000
def balance_check():
    return balance
print("you have " + str(balance) + " balance in your account")

def withdraw(amount):
    global balance
    if amount > balance:
        print("insufficient balance")
    else:
        balance -= amount
        print("your updated balance is " + str(balance))

def deposit(amount):

    global balance
    balance += amount
    print ("your updated balance is " + str(balance))

while True:
    print("\t welcome to ATM \t")
    print("1. balance check")
    print("2. withdraw")
    print("3. deposit")
    print("4. exit")

    chose = int(input("enter the number from (1 to 4) according to your requirement :"))
    if chose == 1:
        balance_check()
        print("your current balance is :" ,balance_check())

    elif chose == 2:
        amount = int(input ("enter the amount you want to withdraw"))
        withdraw(amount)

    elif chose == 3:
        amount = int(input ("enter the amount you want to deposit"))
        deposit(amount)

    elif chose == 4:
        print ("Thank you for using this program")
        break

    else :
        print("please enter a valid number")

