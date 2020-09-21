from my_budget import get_goals, edit_accounts, get_monthly_income, get_bill_amounts, print_bills, deposit, \
    withdrawal
from program_flow_states import BudgetStates, UserRegistrationStates, AdminFunctionStates
from user import new_user, login, admin_login, get_user, User
from db_functions import create_tables, remove_bank
from bank import new_bank, change_bank_name, change_bank_location, get_bank


def main():
    create_tables()
    login_states = UserRegistrationStates
    budgeting_states = BudgetStates
    admin_states = AdminFunctionStates
    print('Welcome to Jaxon\'s Budget Program!')
    while True:
        # Regular Login Menu
        current_state = get_current_state(login_states)
        if current_state == login_states.create_account.value:
            new_user()
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

        # Administrator login
        elif current_state == login_states.admin_login.value:
            # If admin login is successful, moves on  to administrator-restricted menu
            if admin_login():
                while True:
                    current_state = get_current_state(admin_states)
                    if current_state == admin_states.create_bank.value:
                        new_bank()
                        continue
                    elif current_state == admin_states.remove_bank.value:
                        remove_bank(get_bank())
                        continue
                    elif current_state == admin_states.change_bank_name.value:
                        change_bank_name(get_bank())
                        continue
                    elif current_state == admin_states.change_bank_location.value:
                        change_bank_location(get_bank())
                        continue
                    elif current_state == admin_states.log_out.value:
                        print('Logged Out')
                        break
        elif current_state == login_states.exit_program.value:
            print('Exiting Program... Have a nice day!')
            break
        print()
        for state in login_states:
            print(f'{state.value}: {state.name.replace("_", " ").title()}')
        try:
            current_state = input('What would you like to do?\n')
            current_state = int(current_state)
        except ValueError:
            print(f'Value Error: could not convert {current_state} to int, please enter a number '
                  f'corresponding to a menu item')

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