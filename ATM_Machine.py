import time

print("Please insert Your CARD ")
time.sleep(5)

password = 1234
balance = 6000

try:
    pin = int(input("Enter your pin: "))
except:
    print("Please enter a valid pin number.")

if pin == password:
    while True:
        print("""
        1 == Check Balance
        2 == Withdraw Balance
        3 == Deposit Balance
        4 == Exit
        """)
        
        try:
            option = int(input("Please enter your choice: "))
        except:
            print("Please enter a valid option.")
            
        
        if option == 1:
            print(f"Your updated balance is {balance}")
            print("======================================")
        
        elif option == 2:
            try:
                withdraw_amount = int(input("Please enter withdrawal amount: "))
                if withdraw_amount > balance:
                    print("Insufficient balance!")
                else:
                    balance -= withdraw_amount
                    print(f"{withdraw_amount} is debited from your account.")
                    print(f"Your current balance is {balance}")
            except:
                print("Invalid withdrawal amount.")
            
            print("======================================")

        elif option == 3:
            try:
                deposit_amount = int(input("Please enter deposit amount: "))
                balance += deposit_amount
                print(f"{deposit_amount} is credited to your account.")
                print(f"Your updated balance is {balance}")
            except:
                print("Invalid deposit amount.")
            
            print("======================================")

        elif option == 4:
            print("Thank you for using our ATM service.")
            break

        else:
            print("Please enter a valid option.")
else:
    print("Wrong pin. Please try again.")
