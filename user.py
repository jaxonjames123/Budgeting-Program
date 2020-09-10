import json
import datetime
import re
from security import encrypt_password, check_encrypted_password
import getpass
import os


def add_user(username, password):
    filename = './UserList.json'
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
    filename = './UserList.json'
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
        username = input('Username: ').rstrip().lower()
    pt_password = getpass.getpass()
    password = encrypt_password(pt_password)
    while True:
        dob = input('Date of Birth (Year-Month-Date): ').rstrip().split('-')
        try:
            dob = datetime.date(int(dob[0]), int(dob[1]), int(dob[2]))
            break
        except ValueError:
            print('Date of Birth not entered in correct format. Please try again.')
            continue
    while True:
        ssn = input('SSN (###-##-####): ').rstrip()
        if ssn_validation(ssn):
            break
        else:
            print("SSN is not valid. Please enter in specified format.")
            continue
    while True:
        email = str(input('Email: ')).lower()
        if email_validation(email):
            break
        else:
            print(f'{email} is not a valid email address, please try again.')
            continue
    print(f'\nYour username is: {username}')
    return User(first_name, last_name, username, password, dob, ssn, email)


def login():
    username = input('Username: ').rstrip().lower()
    pt_password = getpass.getpass()
    filename = './UserList.json'
    if os.path.exists(filename):
        with open(filename) as f:
            users_dict = json.load(f)
    if username in users_dict and check_encrypted_password(pt_password, users_dict[username]):
        print(f'Login Successful!')
        return True
    else:
        print('Incorrect Username or Password, Please try again\n')
        login()

# Function to allow system admins to log in, after logging in they will be able to add new banks
def admin_login():
    username = input('Username: ').rstrip().lower()
    pt_password = getpass.getpass()
    filename = './AdminLogin.json'
    if os.path.exists(filename):
        with open(filename) as f:
            users_dict = json.load(f)
    if username in users_dict and check_encrypted_password(pt_password, users_dict[username]):
        print(f'Login Successful!')
        return True
    else:
        print('Incorrect Username or Password, Please try again\n')


class User:
    def __init__(self, first_name, last_name, username, password, dob, ssn, email):
        self._accounts = []
        self._first_name = first_name
        self._last_name = last_name
        self._username = username
        self._password = password
        add_user(self._username, self._password)
        self._dob = dob
        self._ssn = ssn
        self._email = email

    def __str__(self):
        return f'{self._first_name} {self._last_name} born: {format_date(self._dob)} email is {self._email}, ' \
               f'and has {len(self._accounts)} accounts with us'

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

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @dob.setter
    def age(self, age):
        self._dob = age

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