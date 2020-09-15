from my_budget import get_goals, edit_accounts, get_monthly_income, get_bill_amounts, print_bills, deposit, \
    withdrawal
from program_flow_states import MyStates, UserRegistrationStates
from user import new_user, login, admin_login, get_user
from db_functions import create_tables


def main():
    create_tables()
    login_states = UserRegistrationStates
    budgeting_states = MyStates
    print('Welcome to Jaxon\'s Budget Program!')
    for state in login_states:
        print(f'{state.value}: {state.name.replace("_", " ").title()}')
    try:
        current_state = input('What would you like to do?\n')
        current_state = int(current_state)
    except ValueError:
        print(f'Value Error: could not convert {current_state} to int, please enter a number '
              f'corresponding to a menu item')
    while True:
        if current_state == login_states.create_account.value:
            new_user()
        elif current_state == login_states.login.value:
            user = get_user(login())
            for state in budgeting_states:
                print(f'{state.value}: {state.name.replace("_", " ").title()}')
            try:
                current_state = input('What would you like to do?\n')
                current_state = int(current_state)
            except ValueError:
                print(f'Value Error: could not convert {current_state} to int, please enter a number '
                      f'corresponding to a menu item')
            while True:
                if current_state == budgeting_states.goals.value:
                    get_goals()
                    print('')
                    for state in budgeting_states:
                        print(f'{state.value}: {state.name.replace("_", " ").title()}')
                    try:
                        current_state = input('What would you like to do?\n')
                        current_state = int(current_state)
                    except ValueError:
                        print(f'Value Error: could not convert {current_state} to int, please enter a number '
                              f'corresponding to a menu item')
                    continue
                elif current_state == budgeting_states.account_actions.value:
                    edit_accounts(user)
                    print('')
                    for state in budgeting_states:
                        print(f'{state.value}: {state.name.replace("_", " ").title()}')
                    try:
                        current_state = input('What would you like to do?\n')
                        current_state = int(current_state)
                    except ValueError:
                        print(f'Value Error: could not convert {current_state} to int, please enter a number '
                              f'corresponding to a menu item')
                    continue
                elif current_state == budgeting_states.monthly_income.value:
                    get_monthly_income()
                    print('')
                    for state in budgeting_states:
                        print(f'{state.value}: {state.name.replace("_", " ").title()}')
                    try:
                        current_state = input('What would you like to do?\n')
                        current_state = int(current_state)
                    except ValueError:
                        print(f'Value Error: could not convert {current_state} to int, please enter a number '
                              f'corresponding to a menu item')
                    continue
                elif current_state == budgeting_states.bills.value:
                    print_bills(get_bill_amounts())
                    print('')
                    for state in budgeting_states:
                        print(f'{state.value}: {state.name.replace("_", " ").title()}')
                    try:
                        current_state = input('What would you like to do?\n')
                        current_state = int(current_state)
                    except ValueError:
                        print(f'Value Error: could not convert {current_state} to int, please enter a number '
                              f'corresponding to a menu item')
                    continue
                elif current_state == budgeting_states.make_deposit.value:
                    deposit()
                    print('')
                    for state in budgeting_states:
                        print(f'{state.value}: {state.name.replace("_", " ").title()}')
                    try:
                        current_state = input('What would you like to do?\n')
                        current_state = int(current_state)
                    except ValueError:
                        print(f'Value Error: could not convert {current_state} to int, please enter a number '
                              f'corresponding to a menu item')
                    continue
                elif current_state == budgeting_states.make_withdrawal.value:
                    withdrawal()
                    print('')
                    for state in budgeting_states:
                        print(f'{state.value}: {state.name.replace("_", " ").title()}')
                    try:
                        current_state = input('What would you like to do?\n')
                        current_state = int(current_state)
                    except ValueError:
                        print(f'Value Error: could not convert {current_state} to int, please enter a number '
                              f'corresponding to a menu item')
                    continue
                elif current_state == budgeting_states.log_out.value:
                    print(f'Logged Out')
                    break
        elif current_state == login_states.admin_login.value:
            if admin_login():
                print()
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


if __name__ == '__main__':
    main()