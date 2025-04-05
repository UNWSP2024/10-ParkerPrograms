# Nathan Parker
# 04/04/25
# Program #1

# This program is a copy of Dr. James Smith's bankaccount.py and account_test.py programs



class BankAccount:
    # The __init__ method accepts an argument for the account's balance and assigns it to balance
    def __init__(self, bal):
        self.__balance = bal

    # The deposit method makes a deposit into the account
    def deposit(self, amount):
        self.__balance += amount

    # The withdraw method withdraws an amount from the account
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Error: Insufficient funds')

    # The get_balance method returns the account balance
    def get_balance(self):
        return self.__balance



def main():
    # Get the starting balance
    start_bal = float(input('Enter your starting balance: '))

    # Create a BankAcount object named savings
    savings = BankAccount(start_bal)

    # Deposit the user's paycheck
    pay = float(input('How much were you paid this week? '))
    print('I will deposit that into your account.')
    savings.deposit(pay)

    # Display the balance
    print('Your account balance is $',
          format(savings.get_balance(), ',.2f'), sep='')

    # Get the amount to withdraw
    cash = float(input('How much would you like to withdraw? '))
    print('I will withdraw that from your account.')
    savings.withdraw(cash)

    # Display the balance
    print('Your account balance is $',
          format(savings.get_balance(), ',.2f'),sep='')

# Call the main function
main()

