from db_functions import insert_bank, check_bank_exists, get_bank_id, update_bank, load_bank


class Bank:

    # Must change location to address, city, state, zip
    def __init__(self, name, location):
        self._name = name
        self._location = location

    def __str__(self):
        return f'\nBank: {self._name}\nLocation: {self._location}\n'

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


# need to add address validation after I change location to full address
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
    bank = Bank(bank[0], bank[1])
    updated_bank = Bank("", "")
    new_name = input('What is the bank\'s new name?: ').strip().upper()
    updated_bank.name = new_name
    updated_bank.location = bank.location
    bank_id = get_bank_id(bank)
    update_bank(updated_bank, bank_id)
    return updated_bank


def change_bank_location(bank):
    bank = Bank(bank[0], bank[1])
    updated_bank = Bank("", "")
    location = input('What is the new location of this bank? ').strip().upper()
    updated_bank.name = bank.name
    updated_bank.location = location
    bank_id = get_bank_id(bank)
    update_bank(updated_bank, bank_id)
    return updated_bank

def get_bank():
    knows_id = input('Do you know your bank\'s id? (Yes/No) ').strip().upper()
    if knows_id == 'YES' or knows_id == 'Y':
        bank_id = int(input('What is your bank\'s id? '))
        return load_bank(bank_id)
    else:
        bank_name = input('What is your bank name? ').strip().upper()
        bank_location = input('Where is your bank located? ').strip().upper()
        bank = Bank(bank_name, bank_location)
        if check_bank_exists(bank)[0]:
            return load_bank(get_bank_id(bank))
        else:
            print(f'{bank_name} with {bank_location} does not exist, please create a bank with these parameters.')
            get_bank()





# This becomes obsolete once we decided users contains the foreign key for banks
# def remove_user_bank(bank):
#     user = input('What is the username of the member you would like to remove from the bank? ').lower().strip()
#     if bank.users == user:
#         bank.users.remove(user)
#         print(f'{user} has been removed from this bank')
#     else:
#         print(f'{user} is not a member of this bank')

# this also became obsolete
# def add_user_bank(bank):
#     pass
# users = []
# usernames = input('Enter member\'s usernames separated by a comma: ').strip().lower().split(', ')
# for username in usernames:
#     try:
#         if username == get_user(username).username:
#             users.append(username)
#             print(f'Successfully added {username} to bank')
#     except AttributeError:
#         print(f'{username} is not currently registered to a member')
# bank.users = users
