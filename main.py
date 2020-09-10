from my_budget import get_goals, edit_accounts, get_monthly_income, get_bill_amounts, print_bills, deposit, \
    withdrawal
from program_flow_states import MyStates, UserRegistrationStates
from db_connection import my_cursor, users_db
from user import new_user, login


def main():
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
            user = new_user()
            # Upload user info to database when creating a new user
            insert_query = ('INSERT INTO users (first_name, last_name, username, password, dob, ssn, email) VALUES '
                            f'("{user.first_name}", "{user.last_name}", "{user.username}", "{user.password}", '
                            f'STR_TO_DATE("{user.dob}", "%Y-%m-%d"), "{user.ssn}", "{user.email}")')
            my_cursor.execute(insert_query)
            users_db.commit()
            print(my_cursor.rowcount, "User successfully inserted into users table")
            my_cursor.close()
        elif current_state == login_states.login.value:
            if login():
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
                    elif current_state == budgeting_states.account_actions.value:
                        edit_accounts()
                    elif current_state == budgeting_states.monthly_income.value:
                        get_monthly_income()
                    elif current_state == budgeting_states.bills.value:
                        print_bills(get_bill_amounts())
                    elif current_state == budgeting_states.make_deposit.value:
                        deposit()
                    elif current_state == budgeting_states.make_withdrawal.value:
                        withdrawal()
                    elif current_state == budgeting_states.log_out.value:
                        print(f'Logged Out')
                        break
                    print('')
                    for state in budgeting_states:
                        print(f'{state.value}: {state.name.replace("_", " ").title()}')
                    try:
                        current_state = input('What would you like to do?\n')
                        current_state = int(current_state)
                    except ValueError:
                        print(f'Value Error: could not convert {current_state} to int, please enter a number '
                              f'corresponding to a menu item')
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