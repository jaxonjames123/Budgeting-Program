from my_budget import get_goals, edit_accounts, get_monthly_income, get_bill_amounts, print_bills, deposit, MyStates


def main():
    states = MyStates
    print('Welcome to Jaxon\'s Budget Program!')
    for state in states:
        print(f'{state.value}: {state.name.replace("_", " ").title()}')
    try:
        current_state = input('What would you like to do?\n')
        current_state = int(current_state)
    except ValueError:
        print(f'Value Error: could not convert {current_state} to int, please enter a number '
              f'corresponding to a menu item')
    while True:
        if current_state == states.goals.value:
            get_goals()
        elif current_state == states.accounts.value:
            edit_accounts()
        elif current_state == states.monthly_income.value:
            get_monthly_income()
        elif current_state == states.bills.value:
            print_bills(get_bill_amounts())
        elif current_state == states.make_deposit.value:
            deposit()
        if current_state == states.exit_program.value:
            print(f'Exiting program... Have a nice day!')
            break
        print('')
        for state in states:
            print(f'{state.value}: {state.name.replace("_", " ").title()}')
        try:
            current_state = input('What would you like to do?\n')
            current_state = int(current_state)
        except ValueError:
            print(f'Value Error: could not convert {current_state} to int, please enter a number '
                  f'corresponding to a menu item')


if __name__ == "__main__":
    main()