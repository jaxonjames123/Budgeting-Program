from ..Database.db_functions import load_bank, load_user, fetch_account_type, fetch_type_from_name, load_account_types, add_account_db
from datetime import datetime
from global_functions import format_date
from Classes.user import User
import pytz


class Account:
    def __init__(self, bank, account_number, balance, account_holder, account_type_id,
                 date_created=datetime.now(tz=pytz.utc), account_id=0):
        self._bank = bank
        self._account_number = account_number
        self._balance = balance
        self._account_holder = account_holder
        self._date_created = date_created
        self._account_type_id = account_type_id
        self._account_id = account_id

    def __str__(self):
        bank = load_bank(self._bank)
        username = load_user(self._account_holder)
        account_type = fetch_account_type(self._account_type_id)
        return f'\n' \
               f'Bank: {bank[0]}\n' \
               f'Account Number: {self._account_number}\n' \
               f'Balance: {self._balance}\n' \
               f'Account Holder: {username[1][2]}\n' \
               f'Account Type: {account_type[0]}\n' \
               f'Account ID: {self._account_id}\n' \
               f'Date Created: {format_date(self._date_created)}'

    @property
    def bank(self):
        return self._bank

    @bank.setter
    def bank(self, value):
        self._bank = value

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        self._account_number = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    @property
    def account_holder(self):
        return self._account_holder

    @account_holder.setter
    def account_holder(self, value):
        self._account_holder = value

    @property
    def date_created(self):
        return self._date_created

    @date_created.setter
    def date_created(self, value):
        self._date_created = value

    @property
    def account_type_id(self):
        return self._account_type_id

    @account_type_id.setter
    def account_type_id(self, value):
        self._account_type_id = value

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value

    def withdrawal(self, amount):
        self._balance -= amount

    def deposit(self, amount):
        self._balance += amount

def add_account(user):
    is_new = input('Are you opening up a brand new account with a bank? (Yes/No) ').upper().strip()
    bank = get_bank()
    account_number = get_account_number()
    balance = get_current_balance()
    account_holder = user.username
    account_type_id = get_account_type(bank)
    if is_new != 'Y' and is_new != 'YES':
        date_created = get_date_created()
        new_account = Account(bank, account_number, balance, account_holder, account_type_id, date_created)
    else:
        new_account = Account(bank, account_number, balance, account_holder, account_type_id)
    add_account_db(new_account)
    user.accounts.append(new_account)
    return new_account


def get_bank():
    while True:
        resp = input('What is the bank ID of the bank this account belongs to? ').strip()
        try:
            resp = int(resp)
            bank = load_bank(resp)
            if bank is not None:
                bank = bank[2]
                return bank
            else:
                print(f'{resp} is not a valid bank ID.')
                continue
        except ValueError:
            print('Please input a positive whole number corresponding to a bank\'s ID')
            continue


def get_account_number():
    while True:
        resp = input('If you know your account number, enter it here. If not, enter 0: ').strip()
        try:
            account_number = int(resp)
            return account_number
        except ValueError:
            print('Please input a whole number')
            continue


def get_current_balance():
    while True:
        resp = input('What is the current account balance? $').strip()
        try:
            balance = float(resp)
            return balance
        except ValueError:
            print('Please input a number')
            continue


def get_account_type(bank):
    while True:
        account_type_name = input('What type of account is this? ').strip().upper()
        try:
            exists = fetch_type_from_name(account_type_name, bank)
            if exists[0]:
                account_type_id = exists[1]
                print(account_type_id)
                return account_type_id
            else:
                print('The current bank selected does not support this kind of account')
                print(f'The current bank selected only supports {load_account_types(bank)}')
                resp = input('Would you like to proceed with the currently selected bank? (Yes/No) ').upper().strip()
                if resp != 'Y' or resp != 'YES':
                    bank = get_bank()
            continue
        except ValueError:
            print('Please input a number')
            continue


def get_date_created():
    while True:
        resp = input('When was this account created? Please insert date in the format: (Month-Day-Year) ') \
            .strip().split('-')
        try:
            created = datetime.datetime(int(resp[2]), int(resp[0]), int(resp[1]))
            return created
        except ValueError:
            print('Date of Birth not entered in correct format. Please try again.')
            continue


account1 = Account(1, 134562, 352.89, 'test1', 8)
x = datetime.now()
user1 = User('Jaxon', 'Terrell', 'test1', 'hhrS15513', x, 123456789, 'noxaj123@gmail.com', 1)
account = add_account(user1)
print(account)
