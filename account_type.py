from db_functions import insert_account_type, remove_account_type, fetch_account_type, update_account_info


class AccountType:
    def __init__(self, account_type, bank, interest_rate, monthly_fees, minimum_balance, max_withdrawals,
                 account_type_id=0):
        self._account_type = account_type
        self._bank = bank
        self._interest_rate = interest_rate
        self._monthly_fees = monthly_fees
        self._minimum_balance = minimum_balance
        self._max_withdrawals = max_withdrawals
        self._account_type_id = account_type_id

    def __str__(self):
        return f'{self._account_type} at Bank: {self._bank} has\nMonthly interest rate: %{self.interest_rate:,.2f}\n' \
               f'Monthly fees: ${self._monthly_fees:,.2f}\nTotal monthly withdrawals: {self._max_withdrawals}\n' \
               f'Minimum monthly balance: ${self._minimum_balance:,.2f}'

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value

    @property
    def bank(self):
        return self._bank

    @bank.setter
    def bank(self, value):
        self._bank = value

    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        self._interest_rate = value

    @property
    def monthly_fees(self):
        return self._monthly_fees

    @monthly_fees.setter
    def monthly_fees(self, value):
        self._monthly_fees = value

    @property
    def minimum_balance(self):
        return self._minimum_balance

    @minimum_balance.setter
    def minimum_balance(self, value):
        self._minimum_balance = value

    @property
    def max_withdrawals(self):
        return self._max_withdrawals

    @max_withdrawals.setter
    def max_withdrawals(self, value):
        self._max_withdrawals = value

    @property
    def account_type_id(self):
        return self._account_type_id

    @account_type_id.setter
    def account_type_id(self, value):
        self._account_type_id = value


def add_account_type(bank):
    while True:
        account_type = input('What kind of account is being added? ').strip().upper()
        if not account_type.isalpha():
            print('Account types cannot contain numbers')
            continue
        else:
            break
    bank = bank.bank_id
    while True:
        interest_rate = input(f'What is the interest rate for {account_type} accounts? ').strip()
        try:
            interest_rate = float(interest_rate)
            break
        except ValueError:
            print('Please input a number, enter 0 if there is no interest rate')
            continue
    while True:
        monthly_fees = input("What is the total cost of the monthly fees associated with this kind of account? ") \
            .strip()
        try:
            monthly_fees = float(monthly_fees)
            break
        except ValueError:
            print('Please input a number, enter 0 if there are no monthly fees')
            continue
    while True:
        minimum_balance = input('Does a certain monthly balance need to be maintained with this kind of account? ') \
            .strip()
        try:
            minimum_balance = float(minimum_balance)
            break
        except ValueError:
            print('Please input a number, enter 0 if there is no minimum monthly balance')
            continue
    while True:
        max_withdrawals = input('How many monthly withdrawals are allowed for accounts of this type? ')
        try:
            max_withdrawals = float(max_withdrawals)
            if max_withdrawals == 0:
                max_withdrawals = 99999
            break
        except ValueError:
            print('Please input a number, enter 0 if there is no maximum')
            continue
    _ = AccountType(account_type, bank, interest_rate, monthly_fees, minimum_balance, max_withdrawals)
    insert_account_type(_)
    return _


def edit_account_type_name(account):
    old_name = account.account_type
    new_name = input('What would you like to rename this account? ').strip().upper()
    if new_name.isalpha():
        account.account_type = new_name
        update_account_info(account, 'account_type', new_name)
        print(f'{old_name} has been updated to {new_name}')
    else:
        print('Account type name cannot contain numbers, please re-enter using only letters')


def edit_interest_rate(account):
    old_rate = account.interest_rate
    new_rate = input('What is the new interest rate for this account type? ').strip()
    try:
        new_rate = float(new_rate)
        account.interest_rate = new_rate
        update_account_info(account, 'interest_rate', new_rate)
        print(f'Old rate of {old_rate:,.2f}% has been updated to {new_rate:,.2f}%')
    except ValueError:
        print('Please try again with a number')
        edit_interest_rate(account)


def edit_monthly_fees(account):
    old_fee = account.monthly_fees
    new_fee = input('What is the monthly fee for this account type? ').strip()
    try:
        new_fee = float(new_fee)
        account.monthly_fees = new_fee
        update_account_info(account, 'monthly_fees', new_fee)
        print(f'Old monthly fee of ${old_fee:,.2f} has been updated to ${new_fee:,.2f}')
    except ValueError:
        print('Please try again with a number')
        edit_interest_rate(account)


def edit_minimum_balance(account):
    old_balance = account.minimum_balance
    new_balance = input('What is the minimum balance for this account type? ').strip()
    try:
        new_balance = float(new_balance)
        account.minimum_balance = new_balance
        update_account_info(account, 'minimum_balance', new_balance)
        print(f'Old minimum balance of ${old_balance:,.2f} has been updated to ${new_balance:,.2f}')
    except ValueError:
        print('Please try again with a number')
        edit_minimum_balance(account)


def edit_max_withdrawals(account):
    old_number = account.max_withdrawals
    new_number = input('What is the maximum number of withdrawals allowed for this account type? ').strip()
    try:
        new_number = int(new_number)
        account.max_withdrawals = new_number
        update_account_info(account, 'max_withdrawals', new_number)
        print(f'Old maximum number of withdrawals of ${old_number} has been updated to ${new_number}')
    except ValueError:
        print('Please try again with a whole number')
        edit_max_withdrawals(account)


def delete_account_type():
    account_type_id = input('What is the ID of the account type that you would like to delete? ').strip()
    try:
        account_type_id = int(account_type_id)
        remove_account_type(account_type_id)
    except ValueError:
        print('Please try again, and input a number.')


def get_account_type():
    resp = input('Do you know the account type ID (Yes/No) ').strip().upper()
    if resp == 'YES' or resp == 'Y':
        type_id = input('Enter the account type ID: ')
        try:
            type_id = int(type_id)
            try:
                account_info = fetch_account_type(type_id)
                account_type = AccountType(account_info[0], account_info[1], account_info[2], account_info[3],
                                           account_info[4], account_info[5], account_info[6])
                print(account_type)
                return account_type
            except TypeError:
                print('There is no account type associated with that ID')
        except ValueError:
            print("Please input a valid whole number")
    else:
        print('Please obtain your account type IDs by selecting the "View Account Types" menu option')


def print_all_account_types(accounts):
    for _ in accounts:
        account = AccountType(_[0], int(_[1]), float(_[2]), float(_[3]), float(_[4]), int(_[5]),
                              int(_[6]))
        print(account)
