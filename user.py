import json
import datetime
import re
from security import encrypt_password, check_encrypted_password
import getpass
import os
from db_functions import insert_user, load_user, get_bank_id, check_bank_exists
from bank import Bank


class User:
    def __init__(self, first_name, last_name, username, password, dob, ssn, email, bank=None):
        self._accounts = []
        self._first_name = first_name
        self._last_name = last_name
        self._username = username
        self._password = password
        add_user(self._username, self._password)
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


# add a username and hashed password to the UserList json file
# used in the new_user() function
def add_user(username, password):
    filename = './GeneratedFiles/UserList.json'
    if os.path.exists(filename):
        with open(filename) as f:
            users_dict = json.load(f)
        users_dict.update({username: password})
    else:
        users_dict = {username: password}
    with open(filename, 'w') as f:
        json.dump(users_dict, f)


def name_concat(first, last):
    return f'{first} {last}'


def format_date(date):
    return date.strftime('%x')


def email_validation(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex, email):
        return True
    else:
        return False


def name_validation(name):
    name = name
    if name.isalpha():
        return True
    else:
        print("Please enter a name with only letter characters")
        return False


def ssn_validation(ssn):
    chunks = ssn.split('-')
    if len(chunks) == 3:
        if len(chunks[0]) == 3 and len(chunks[1]) == 2 and len(chunks[2]) == 4:
            return True
        else:
            return False
    else:
        return False


def new_user():
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
    filename = './GeneratedFiles/UserList.json'
    if os.path.exists(filename):
        with open(filename) as f:
            users_dict = json.load(f)
        while True:
            username = input('Username: ').rstrip().lower()
            if username in users_dict.keys():
                print(f'Username {username} already exists, please try a different one')
                continue
            else:
                break
    else:
        username = input('Username: ').strip().lower()
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
        dob = input('Date of Birth (Year-Month-Date): ').strip().split('-')
        try:
            dob = datetime.date(int(dob[0]), int(dob[1]), int(dob[2]))
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
    while True:
        has_bank = input('Are you currently a member at a bank? (Yes/No)').upper().strip()
        if has_bank == 'YES' or has_bank == 'Y':
            bank_name = input('What is the name of your bank?')
            bank_location = input('Where is your bank located?')
            bank = Bank(bank_name, bank_location)
            if check_bank_exists(bank):
                bank_id = int(get_bank_id(bank))
                user = User(first_name, last_name, username, password, dob, ssn, email, bank_id)
                insert_user(user)
                return user
            else:
                print(f'{bank_name} is not registered with us.')
                continue
        else:
            break
    user = User(first_name, last_name, username, password, dob, ssn, email)
    insert_user(user)
    return user


def login():
    username = input('Username: ').rstrip().lower()
    pt_password = getpass.getpass()
    filename = './GeneratedFiles/UserList.json'
    if os.path.exists(filename):
        try:
            with open(filename) as f:
                users_dict = json.load(f)
            if username in users_dict and check_encrypted_password(pt_password, users_dict[username]):
                print(f'Login Successful!\n')
                return username
            else:
                print('Username/password combination incorrect. Please try again.\n')
        except IndexError:
            print('Username/password combination incorrect. Please try again or create an account.')
    else:
        print('Username/password combination incorrect. Please try again.\n')


# Function to allow system admins to log in, after logging in they will be able to add new banks
def admin_login():
    username = input('Username: ').strip().lower()
    pt_password = getpass.getpass()
    filename = './GeneratedFiles/AdminLogin.json'
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


def get_user(username):
    try:
        user_data_list = load_user(username)
        if user_data_list is not None:
            user = User(user_data_list[0], user_data_list[1], user_data_list[2], user_data_list[3], user_data_list[4],
                        user_data_list[5], user_data_list[6])
            return user
    except IndexError:
        print('Incorrect username or password. Please try again.\n')
