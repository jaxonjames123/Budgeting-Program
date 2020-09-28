from db_functions import insert_bank, check_bank_exists, update_bank, load_bank


class Bank:

    # Must change location to address, city, state, zip
    def __init__(self, name, location, bank_id=0):
        self._name = name
        self._location = location
        self._bank_id = bank_id

    def __str__(self):
        return f'\nBank: {self._name}\nLocation: {self._location}\nID: {self._bank_id}\n'

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    @name.setter
    def name(self, name):
        self._name = name

    @location.setter
    def location(self, location):
        self._location = location

    @property
    def bank_id(self):
        return self._bank_id

    @bank_id.setter
    def bank_id(self, value):
        self._bank_id = value


def new_bank():
    bank_name = input('Bank Name: ').strip().upper()
    location = input('City: ').strip().upper()
    bank = Bank(bank_name, location)
    if not check_bank_exists(bank)[0]:
        insert_bank(bank)
        return bank
    else:
        print(f'The bank: {bank} has already been created')


def change_bank_name(bank):
    updated_bank = Bank("", "")
    new_name = input('What is the bank\'s new name?: ').strip().upper()
    updated_bank.name = new_name
    updated_bank.location = bank.location
    updated_bank.bank_id = bank.bank_id
    update_bank(updated_bank)
    return updated_bank


def change_bank_location(bank):
    updated_bank = Bank("", "")
    location = input('What is the new location of this bank? ').strip().upper()
    updated_bank.name = bank.name
    updated_bank.location = location
    updated_bank.bank_id = bank.bank_id
    update_bank(updated_bank)
    return updated_bank

def get_bank():
    knows_id = input('Do you know your bank\'s id? (Yes/No) ').strip().upper()
    if knows_id == 'YES' or knows_id == 'Y':
        bank_id = int(input('What is your bank\'s id? '))
        bank_info = load_bank(bank_id)
        bank = Bank(bank_info[0], bank_info[1], bank_info[2])
        return bank
    else:
        bank_name = input('What is your bank name? ').strip().upper()
        bank_location = input('Where is your bank located? ').strip().upper()
        bank = Bank(bank_name, bank_location)
        bank_info = check_bank_exists(bank)[1]
        if check_bank_exists(bank)[0]:
            bank = Bank(bank_info[0], bank_info[1], bank_info[2])
            return bank
        else:
            print(f'{bank_name} with {bank_location} does not exist, please create a bank with these parameters.')

def print_banks(banks):
    for _ in banks:
        bank = Bank(_[0], _[1], _[2])
        print(bank)