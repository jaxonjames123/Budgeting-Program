import os
import json


def sql_close_account():
    pass


def edit_accounts(user):
    filename = './accounts.json'
    accounts_dict = {}
    if os.path.exists(filename):
        with open(filename) as f:
            accounts_dict = json.load(f)
        if input('Would you like to check the balance of your existing accounts? (Yes/No) ').upper() == "YES":
            print_accounts(accounts_dict)
        if input('Would you like to close one of your existing accounts? (Yes/No) ').upper() == 'YES':
            account_close = input('Which account would you like to close? ').upper()
            if account_close in accounts_dict:
                accounts_dict.pop(account_close)
                print(f'{account_close} has been closed successfully')
                with open(filename, 'w') as f:
                    json.dump(accounts_dict, f)
            else:
                print(f'The account with the name {account_close} does not exist')
    if input('Would you like to open a new account? (Yes/No) ').upper() == 'YES':
        account = input('What type of account is this? (Ex. Checking, Savings): ').upper()
        balance = input(f'What is the current balance of your {account} account? (Ex. 6675.14) ')
        try:
            balance = float(balance)
            if balance < 0:
                print("Please input a positive number, if you would like to withdraw money, "
                      "use the withdrawal option.")
            else:
                accounts_dict.update({account: balance})
                user.accounts = account
                with open(filename, 'w') as f:
                    json.dump(accounts_dict, f)
                print(f'Your current {account} balance is: ${balance:,.2f}')

        except ValueError:
            print(f'{balance} not in valid number format, please try again')


def deposit():
    filename = './accounts.json'
    if os.path.exists(filename):
        with open(filename) as f:
            accounts_dict = json.load(f)
        print_accounts(accounts_dict)
        account = input('What account would you like to make a deposit to? ').upper()
        if account in accounts_dict:
            while True:
                amount = input('How much would you like to deposit? ')
                try:
                    amount = float(amount)
                    if amount < 0:
                        print("Please input a positive number, if you would like to withdraw money, "
                              "use the withdrawal option.")
                        continue
                    else:
                        new_balance = float(accounts_dict.get(account)) + amount
                        print(f"The updated balance for {account} is ${new_balance:,.2f}")
                        accounts_dict.update({account: new_balance})
                        with open(filename, 'w') as f:
                            json.dump(accounts_dict, f)
                        break
                except ValueError:
                    print('Please input a number of a valid format. (Ex 6542.33)')
                    continue
        else:
            print(f'{account} is not an active account, please try again with a valid account name')
    else:
        print('You do not currently have an open account with us. Please open an account first')


def withdrawal():
    filename = './accounts.json'
    if os.path.exists(filename):
        with open(filename) as f:
            accounts_dict = json.load(f)
        print_accounts(accounts_dict)
        account = input('What account would you like to make a withdrawal from? ').upper()
        if account in accounts_dict:
            while True:
                amount = input('How much would you like to withdraw? ')
                try:
                    amount = float(amount)
                    if amount < 0:
                        print("Please input a positive number")
                        continue
                    elif amount > float(accounts_dict.get(account)):
                        print(f"Unfortunately, you do not have enough money in this {account}  at this time to withdraw"
                              f"that much. Please input a number smaller than your current balance")
                        continue
                    else:
                        new_balance = float(accounts_dict.get(account)) - amount
                        print(f"The updated balance for {account} is ${new_balance:,.2f}")
                        accounts_dict.update({account: new_balance})
                        with open(filename, 'w') as f:
                            json.dump(accounts_dict, f)
                        break
                except ValueError:
                    print('Please input a number of a valid format. (Ex 6542.33)')
                    continue
        else:
            print(f'{account} is not an active account, please try again with a valid account name')
    else:
        print('You do not currently have an open account with us. Please open an account first')


def get_goals():
    filename = './goals.txt'
    if os.path.exists(filename):
        print_file(filename)
        while True:
            if input("You will be able to add to your old goals, or overwrite your existing ones.\n"
                     "Would you like to overwrite your old goals? (Yes/No) ").upper() == "YES":
                n = input('How many budgeting goals do you have?: ')
                try:
                    n = int(n)
                    if n < 0:
                        print('Please input a whole number greater than 0\n')
                        continue
                    goals = []
                    for i in range(n):
                        goals.append(input(f'What is your #{i + 1} goal?: ').upper() + '\n')
                        i += 1
                    with open(filename, 'w') as f:
                        f.writelines(goals)
                    print_file(filename)
                except ValueError:
                    print('Please enter a whole number greater than 0\n')
                    continue
            while True:
                if input("Would you like to add more goals? (Yes/No) ").upper() == "YES":
                    n = input('How many additional budgeting goals do you have?: ')
                    try:
                        n = int(n)
                        if n < 0:
                            print('Please enter a whole number greater than 0\n')
                            continue
                        goals = []
                        for i in range(n):
                            goals.append(input(f'What is your #{i + 1} goal?: ').upper() + '\n')
                            i += 1
                        with open(filename, 'a') as f:
                            f.writelines(goals)
                        print_file(filename)
                    except ValueError:
                        print('Please enter a whole number greater than 0\n')
                        continue
                break
            break
    else:
        # Get goals from user
        n = input('How many budgeting goals do you have?: ')
        try:
            n = int(n)
            if n < 0:
                print('Please enter a whole number greater than 0\n')
            else:
                goals = []
                for i in range(n):
                    goals.append(input(f'What is your #{i + 1} goal?: ').upper() + '\n')
                    i += 1
                with open(filename, 'w') as f:
                    f.writelines(goals)
                print_file(filename)
        except ValueError:
            print("Please enter a whole number greater than 0\n")


def get_monthly_income():
    incomes_dict = dict()
    filename = './incomes.json'
    if os.path.exists(filename):
        with open(filename) as f:
            incomes_dict = json.load(f)
        print('Current income sources: ')
        print_incomes(incomes_dict)
    else:
        print('Currently there are no saved income sources')
    while True:
        if input('\nAdd an income source? (Yes/No) ').upper() == 'YES':
            incomes_dict.update(get_income_source())
            print_incomes(incomes_dict)
            with open(filename, 'w') as f:
                json.dump(incomes_dict, f)
        else:
            break
    while True:
        print('\nYour current income sources are: ')
        print_incomes(incomes_dict)
        if input('\nRemove an income source? (Yes/No) ').upper() == 'YES':
            source = input('What income source would you like to remove? ').upper()
            if source in incomes_dict:
                incomes_dict.pop(source)
                print(f'{source} has been removed from income sources')
                with open(filename, 'w') as f:
                    json.dump(incomes_dict, f)
            else:
                print(f'{source} is already not in the list of income sources')
        else:
            break


def get_income_source():
    source = input('What is the source of income? ').upper()
    try:
        income = float(input('How much income is that source bringing in a month? '))
    except TypeError:
        print('Please enter a valid number (Ex. 45.63) ')
    return {source: income}


def get_bill_amounts():
    filename = './bills.json'
    if os.path.exists(filename):
        with open(filename) as f:
            bills_dict = json.load(f)
        editing = True
        removing = True
        while editing:
            print_bills(bills_dict)
            if input("Would you like to change the cost of one your monthly bills? (Yes/No) ").upper() == "YES":
                bill = input('Which bill would you like to change? ').upper()
                while True:
                    bill_value = input(f'What is the new monthly cost of {bill}? ')
                    try:
                        bill_value = float(bill_value)
                        if bill_value < 0:
                            print('Please input a positive number')
                            continue
                        else:
                            bills_dict[bill] = bill_value
                            break
                    except ValueError:
                        print('Please input a positive number')
                        continue
            elif input('Would you like to add a new bill? (Yes/No) ').upper() == "YES":
                bill = input('What bill would you like to add? ').upper()
                while True:
                    bill_cost = input(f'How much does {bill} cost? ')
                    try:
                        bill_cost = float(bill_cost)
                        if bill_cost < 0:
                            print('Please input a positive number')
                            continue
                        else:
                            bills_dict.update({bill: bill_cost})
                            break
                    except ValueError:
                        print('Please input a positive number\n')
                        continue
            else:
                editing = False
        while removing:
            if input("Would you like to remove a bill? (Yes/No) ").upper() == "YES":
                bill = input('What bill would you like to remove? ').upper()
                print(f'You have removed the bill: {bill}')
                bills_dict.pop(bill)
            else:
                removing = False
    else:
        bills_in = input('Enter your bills separated by a comma: ').upper().split(", ")
        bills_dict = {}
        bills_dict = bills_dict.fromkeys(bills_in)
        for bill in bills_dict:
            while True:
                cost = input(f'How much does your {bill} bill cost? ')
                try:
                    cost = float(cost)
                    if cost < 0:
                        print('Please input a positive number\n')
                        continue
                    else:
                        bills_dict[bill] = cost
                        break
                except ValueError:
                    print("Please input a positive number (Ex. 1600.28)\n")
                    continue
        with open(filename, 'w') as f:
            json.dump(bills_dict, f)
        return bills_dict


def print_incomes(incomes_in: dict) -> dict:
    for source in incomes_in:
        print(f'{source} brings in ${incomes_in[source]:,.2f} a month')


def print_bills(bills_in: dict) -> dict:
    for item in bills_in:
        print(f'{item} costs: ${bills_in[item]:,.2f}')
    print(f'Your monthly expenses total ${sum(bills_in.values()):,.2f}\n')


def print_accounts(accounts_in: dict) -> dict:
    for account in accounts_in:
        print(f'{account} balance: ${accounts_in[account]:,.2f}')


def print_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line.rstrip())
