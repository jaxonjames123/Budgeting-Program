import re


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