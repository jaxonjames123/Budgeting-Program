import json
import datetime
from security import encrypt_password, check_encrypted_password
import getpass
import os
from Database.db_functions import insert_user, load_user, check_bank_exists
from Classes.bank import Bank
from global_functions import name_validation, format_date, email_validation, ssn_validation


class User:
    def __init__(self, first_name, last_name, username, password, dob, ssn, email, bank):
        self._accounts = []
        self._first_name = first_name
        self._last_name = last_name
        self._username = username
        self._password = password
        self._dob = dob
        self._ssn = ssn
        self._email = email
        self._bank = bank

    def __str__(self):
        return f'{self._first_name} {self._last_name} born: {format_date(self._dob)} email is {self._email}, ' \
               f'and has {len(self._accounts)} accounts with {self._bank}'

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def dob(self):
        return self._dob

    @property
    def ssn(self):
        return self._ssn

    @property
    def email(self):
        return self._email

    @property
    def accounts(self):
        return self._accounts

    @property
    def bank(self):
        return self._bank

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @ssn.setter
    def ssn(self, ssn):
        self._ssn = ssn

    @email.setter
    def email(self, email):
        self._email = email

    @accounts.setter
    def accounts(self, *accounts):
        for account in accounts:
            for _ in account:
                self._accounts.append(_)

    @username.setter
    def username(self, username):
        self._username = username

    @password.setter
    def password(self, password):
        self._password = password

    @bank.setter
    def bank(self, bank):
        self._bank = bank


def new_user():
    bank_id = int()
    while True:
        has_bank = input('Are you currently a member at a bank? (Yes/No) ').upper().strip()
        if has_bank == 'YES' or has_bank == 'Y':
            bank_name = input('What is the name of your bank? ').upper().strip()
            bank_location = input('Where is your bank located? ').upper().strip()
            bank = Bank(bank_name, bank_location)
            try:
                if check_bank_exists(bank):
                    bank_id = bank.bank_id
                    break
                else:
                    print(f'{bank_name} is not registered with us.')
                    continue
            except IndexError:
                print('Internal Error. Please contact your system administrator for help resolving this issue.')
                return 0
        else:
            print('Please register with a bank before accessing this application.')
            return 0
    while True:
        first_name = input('First Name: ').rstrip().upper()
        if name_validation(first_name):
            break
        else:
            continue
    while True:
        last_name = input('Last Name: ').rstrip().upper()
        if name_validation(last_name):
            break
        else:
            continue
    while True:
        username = input('Username: ').rstrip().lower()
        if load_user(username)[0]:
            print(f'Username {username} already exists, please try a different one')
            continue
        else:
            break
    while True:
        pt_password = getpass.getpass()
        print('Please confirm your password')
        confirm_password = getpass.getpass()
        if pt_password == confirm_password:
            password = encrypt_password(pt_password)
            break
        else:
            print('Passwords do not match. Please try again')
            continue
    while True:
        dob = input('Date of Birth (Month-Day-Year): ').strip().split('-')
        try:
            dob = datetime.date(int(dob[2]), int(dob[0]), int(dob[1]))
            break
        except ValueError:
            print('Date of Birth not entered in correct format. Please try again.')
            continue
    while True:
        ssn = input('SSN (###-##-####): ').strip()
        if ssn_validation(ssn):
            break
        else:
            print("SSN is not valid. Please enter in specified format.")
            continue
    while True:
        email = str(input('Email: ')).lower().strip()
        if email_validation(email):
            break
        else:
            print(f'{email} is not a valid email address, please try again.')
            continue
    print(f'\nYour username is: {username}')
    user = User(first_name, last_name, username, password, dob, ssn, email, bank_id)
    insert_user(user)
    return user

def get_user(user_info):
    try:
        user = User(user_info[0], user_info[1], user_info[2], user_info[3], user_info[4], user_info[5], user_info[6],
                    user_info[7])
        print(user)
        return user
    except TypeError:
        print('Username/password combination incorrect. Please try again.\n')


# Function to allow system admins to log in, after logging in they will be able to add new banks
def admin_login():
    username = input('Username: ').strip().lower()
    pt_password = getpass.getpass()
    filename = '../GeneratedFiles/AdminLogin.json'
    if os.path.exists(filename):
        try:
            with open(filename) as f:
                users_dict = json.load(f)
            if username in users_dict and check_encrypted_password(pt_password, users_dict[username]):
                print(f'Login Successful!')
                return True
            else:
                print('Invalid Username or Password, Please try again.\n')
        except UnboundLocalError:
            print('Not an admin. Please try again.\n')
    else:
        print('Incorrect Username or Password, Please try again\n')

def login():
    username = input('Username: ').rstrip().lower()
    pt_password = getpass.getpass()
    user_info = load_user(username)[1]
    if load_user(username)[0] and check_encrypted_password(pt_password, user_info[3]):
        print(f'Login Successful!\n')
        return user_info

