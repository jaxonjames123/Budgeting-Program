from user_actions import get_goals, edit_accounts, get_monthly_income, get_bill_amounts, print_bills, deposit, \
    withdrawal
from States.program_flow import BudgetStates, UserRegistrationStates, AdminFunctionStates, BankFunctions, \
    AccountTypeActions, EditAccountType
from Classes.user import new_user, login, admin_login, get_user, User
from Database.db_functions import create_tables, remove_bank, load_all_banks, load_account_types
from Classes.bank import new_bank, change_bank_name, change_bank_location, get_bank, print_banks
from Classes.account_type import add_account_type, edit_account_type_name, edit_interest_rate, edit_monthly_fees,\
    edit_minimum_balance, edit_max_withdrawals, delete_account_type, get_account_type, print_all_account_types, \
    AccountType


def main():
    create_tables()
    login_states = UserRegistrationStates
    budgeting_states = BudgetStates
    admin_states = AdminFunctionStates
    bank_states = BankFunctions
    account_types = AccountTypeActions
    edit_account = EditAccountType
    print('Welcome to Jaxon\'s Budget Program!')
    while True:
        # Regular Login Menu
        current_state = get_current_state(login_states)
        if current_state == login_states.create_account.value:
            new_user()
            continue
        # Standard User Login
        elif current_state == login_states.login.value:
            user = get_user(login())
            # Check to see if the account actually exists, if it is a user, then moves on to budgeting states
            if isinstance(user, User):
                # Program flow for budgeting menu options
                while True:
                    current_state = get_current_state(budgeting_states)
                    if current_state == budgeting_states.goals.value:
                        get_goals()
                        continue
                    elif current_state == budgeting_states.account_actions.value:
                        edit_accounts(user)
                        continue
                    elif current_state == budgeting_states.monthly_income.value:
                        get_monthly_income()
                        continue
                    elif current_state == budgeting_states.bills.value:
                        print_bills(get_bill_amounts())
                        continue
                    elif current_state == budgeting_states.make_deposit.value:
                        deposit()
                        continue
                    elif current_state == budgeting_states.make_withdrawal.value:
                        withdrawal()
                        continue
                    elif current_state == budgeting_states.log_out.value:
                        print(f'Logged Out')
                        break
            continue

        # Administrator login
        elif current_state == login_states.admin_login.value:
            # If admin login is successful, moves on  to administrator-restricted menu
            if admin_login():
                while True:
                    current_state = get_current_state(admin_states)
                    if current_state == admin_states.create_new_admin.value:
                        continue
                    elif current_state == admin_states.view_all_users.value:
                        continue
                    elif current_state == admin_states.create_bank.value:
                        new_bank()
                        continue
                    elif current_state == admin_states.view_all_banks.value:
                        print_banks(load_all_banks())
                        continue

                    #Bank Functions
                    elif current_state == admin_states.bank_menu.value:
                        print('All banks registered with this system: ')
                        print_banks(load_all_banks())
                        bank = get_bank()
                        while bank is not None:
                            print(bank)
                            current_state = get_current_state(bank_states)
                            if current_state == bank_states.remove_bank.value:
                                bank = remove_bank(bank)
                                continue
                            elif current_state == bank_states.change_bank_name.value:
                                bank = change_bank_name(bank)
                                print(bank)
                                continue
                            elif current_state == bank_states.change_bank_location.value:
                                bank = change_bank_location(bank)
                                print(bank)
                                continue
                            elif current_state == bank_states.edit_account_types.value:
                                print('This bank currently supports the following types of accounts: ')
                                print_all_account_types(load_account_types(bank))
                                while True:
                                    current_state = get_current_state(account_types)
                                    if current_state == account_types.back_to_bank_menu.value:
                                        break
                                    elif current_state == account_types.view_account_types.value:
                                        print_all_account_types(load_account_types(bank))
                                        continue
                                    elif current_state == account_types.add_account_type.value:
                                        add_account_type(bank)
                                        continue
                                    elif current_state == account_types.edit_account_type.value:
                                        account = get_account_type()
                                        if isinstance(account, AccountType):
                                            while True:
                                                current_state = get_current_state(edit_account)
                                                if current_state == edit_account.back_to_account_types_menu.value:
                                                    break
                                                elif current_state == edit_account.edit_account_type_name.value:
                                                    edit_account_type_name(account)
                                                    continue
                                                elif current_state == edit_account.edit_account_interest_rate.value:
                                                    edit_interest_rate(account)
                                                    continue
                                                elif current_state == edit_account.edit_account_monthly_fees.value:
                                                    edit_monthly_fees(account)
                                                    continue
                                                elif current_state == edit_account.edit_account_minimum_balance.value:
                                                    edit_minimum_balance(account)
                                                    continue
                                                elif current_state == edit_account.edit_account_max_withdrawals.value:
                                                    edit_max_withdrawals(account)
                                                    continue
                                        continue
                                    elif current_state == account_types.remove_account_type.value:
                                        delete_account_type()
                                        continue
                            elif current_state == bank_states.back_to_admin_menu.value:
                                break
                    elif current_state == admin_states.log_out.value:
                        print('Logged Out')
                        break
            continue
        elif current_state == login_states.exit_program.value:
            print('Exiting Program... Have a nice day!')
            break


def get_current_state(menu):
    print()
    for state in menu:
        print(f'{state.value}: {state.name.replace("_", " ").title()}')
    try:
        current_state = input('What would you like to do?\n')
        current_state = int(current_state)
        return current_state
    except ValueError:
        print(f'Value Error: could not convert input to int, please enter a number '
              f'corresponding to a menu item')


if __name__ == '__main__':
    main()
