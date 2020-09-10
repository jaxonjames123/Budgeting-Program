from enum import Enum, auto

class MyStates(Enum):
    log_out = 0
    account_actions = auto()
    make_deposit = auto()
    make_withdrawal = auto()
    goals = auto()
    monthly_income = auto()
    bills = auto()

class UserRegistrationStates(Enum):
    exit_program = 0
    create_account = auto()
    login = auto()
    admin_login = auto()
