import json
import os
import datetime


def add_user(username, name):
    filename = './UserList.json'
    if os.path.exists(filename):
        with open(filename) as f:
            users_dict = json.load(f)
        users_dict.update({username: name})
    else:
        users_dict = {username: name}
    with open(filename, 'w') as f:
        json.dump(users_dict, f)


def name_concat(first, last):
    return f'{first} {last}'

def format_date(date):
    return date.strftime('%x')


class User:
    def __init__(self, first_name, last_name, username, password, dob, ssn, email):
        self._accounts = []
        self._first_name = first_name
        self._last_name = last_name
        self._username = username
        add_user(self._username, name_concat(self._first_name, self._last_name))
        self._password = password
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