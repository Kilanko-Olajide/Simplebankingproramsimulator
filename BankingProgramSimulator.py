starter = True
balance = 0

def showbalance():
    print(f"Your balance is {balance} naira.")
def deposit(balance):
    deposit = input("How much do you want to deposit: ")
    deposit = deposit.replace(",", "")
    if float(deposit) < 0:
        print("You cannot deposit less that 0 naira.")
        return 0
    else:
        print(f"You deposited {deposit} naira.")
        return deposit
def withdraw(balance):
    withdraw = input("How much do you want to withdraw: ")
    withdraw = withdraw.replace(",", "")
    if balance < float(withdraw):
        print("Insufficient funds.")
        print(f"Your balance is {balance} naira.")
        return 0
    elif float(withdraw) < 0:
        print("You must withdraw more than 0 naira.")
        return 0
    else:
        print(f"You withdrew {withdraw} naira.")
        return withdraw


while starter:
    print("1. Show balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Quit")

    choice = input("Enter 1,4 to perform your desired action: ")
    if choice == "1":
        showbalance()
    elif choice == "2":
        balance += float(deposit(balance))
    elif choice == "3":
        balance -= float(withdraw(balance))
    elif choice == "4":
        break
    else:
        print("This is an invalid command.")
