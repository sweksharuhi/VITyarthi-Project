balance = 5000   # starting balance
pin = "1234"     # default PIN

print("----- Welcome to ATM -----")

# Login
entered_pin = input("Enter your 4-digit PIN: ")

if entered_pin != pin:
    print("Incorrect PIN! Exiting...")
else:
    while True:
        print("\n----- ATM Menu -----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Your balance is:", balance)

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print("Deposited successfully!")
                print("New balance:", balance)
            else:
                print("Invalid amount.")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance and amount > 0:
                balance -= amount
                print("Withdrawn successfully!")
                print("Remaining balance:", balance)
            else:
                print("Invalid or insufficient balance.")

        elif choice == "4":
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid option, try again.")