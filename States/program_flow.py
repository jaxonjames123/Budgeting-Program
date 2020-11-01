from enum import Enum, auto

class BudgetStates(Enum):
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

class AdminFunctionStates(Enum):
    log_out = 0
    create_new_admin = auto()
    view_all_users = auto()
    bank_menu = auto()
    create_bank = auto()
    view_all_banks = auto()

class BankFunctions(Enum):
    back_to_admin_menu = 0
    remove_bank = auto()
    change_bank_name = auto()
    change_bank_location = auto()
    edit_account_types = auto()

class AccountTypeActions(Enum):
    back_to_bank_menu = 0
    view_account_types = auto()
    add_account_type = auto()
    edit_account_type = auto()
    remove_account_type = auto()

class EditAccountType(Enum):
    back_to_account_types_menu = 0
    edit_account_type_name = auto()
    edit_account_interest_rate = auto()
    edit_account_monthly_fees = auto()
    edit_account_minimum_balance = auto()
    edit_account_max_withdrawals = auto()