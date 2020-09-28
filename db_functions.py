from db_connection import db


def check_table_exists(table):
    query = f"show tables like '{table}'"
    my_cursor = db.cursor()
    my_cursor.execute(query)
    result = my_cursor.fetchone()
    my_cursor.close()
    if result:
        return True
    else:
        return False


def create_tables():
    my_cursor = db.cursor()
    if not check_table_exists('banks'):
        my_cursor.execute("CREATE TABLE banks (bank_name VARCHAR(255), location VARCHAR(255), "
                          "bank_id INT AUTO_INCREMENT,  PRIMARY KEY(bank_id));")
        print("Banks table created")
    if not check_table_exists('users'):
        my_cursor.execute("CREATE TABLE users (first_name VARCHAR(255), last_name VARCHAR(255), username VARCHAR("
                          "255), password VARCHAR(255), dob DATE, ssn VARCHAR(255), email VARCHAR(255), bank INT, "
                          "PRIMARY KEY(username), FOREIGN KEY(bank) REFERENCES banks(bank_id));")
        print("Users table created")

    if not check_table_exists('account_types'):
        my_cursor.execute('create table account_types (account_type varchar(255), bank INT, interest_rate decimal(7,2),'
                          ' monthly_fees decimal(7,2), minimum_balance decimal(7,2), max_withdrawals int, '
                          'account_type_id int not null auto_increment, primary key(account_type_id), foreign key(bank)'
                          ' references banks(bank_id));')
    if not check_table_exists('accounts'):
        my_cursor.execute('create table accounts (account_type varchar(255), balance decimal(14,2), belongs_to '
                          'varchar(255), date_created date, account_id int not null auto_increment, '
                          'account_type_id int, primary key(account_id), foreign key(account_type_id) references '
                          'account_types(account_type_id), foreign key(belongs_to) references users(username));')
    my_cursor.close()


def delete_tables():
    my_cursor = db.cursor()
    query = "drop table users"
    my_cursor.execute(query)
    query = "drop table accounts"
    my_cursor.execute(query)
    query = "drop table account_types"
    my_cursor.execute(query)
    query = f"drop table banks"
    my_cursor.execute(query)
    my_cursor.close()
    return True


def insert_user(user):
    my_cursor = db.cursor()
    if user.bank is None:
        user.bank = "NULL"
    insert_query = ("insert into users (first_name, last_name, username, password, dob, ssn, email, bank) VALUES "
                    f"('{user.first_name}', '{user.last_name}', '{user.username}', '{user.password}', "
                    f"STR_TO_DATE('{user.dob}','%Y-%m-%d'), '{user.ssn}', '{user.email}', '{user.bank}') ")
    my_cursor.execute(insert_query)
    db.commit()
    my_cursor.close()
    print("User successfully inserted into users table\n")


def delete_user(username):
    my_cursor = db.cursor()
    delete_query = f'delete from users where username = "{username}"'
    my_cursor.execute(delete_query)
    db.commit()
    my_cursor.close()
    print('User successfully deleted')


def load_user(username):
    my_cursor = db.cursor()
    select_query = f'select users.first_name, users.last_name, users.username, users.password, users.dob, users.ssn, ' \
                   f'users.email, banks.bank_name from users inner join banks on users.bank = banks.bank_id where ' \
                   f'username = "{username}"'
    my_cursor.execute(select_query)
    record = my_cursor.fetchall()
    row_count = my_cursor.rowcount
    my_cursor.close()
    if row_count > 0:
        first_name = record[0][0]
        last_name = record[0][1]
        username = record[0][2]
        password = record[0][3]
        dob = record[0][4]
        ssn = record[0][5]
        email = record[0][6]
        bank = record[0][7]
        user = [first_name, last_name, username, password, dob, ssn, email, bank]
        return True, user
    else:
        return False, 0


def insert_bank(bank):
    my_cursor = db.cursor()
    insert_query = f'insert into banks (bank_name, location) VALUES ("{bank.name}", "{bank.location}")'
    my_cursor.execute(insert_query)
    db.commit()
    my_cursor.close()
    print("Bank successfully inserted into banks table\n")


def remove_bank(bank):
    my_cursor = db.cursor()
    delete_query = f'delete from banks where bank_id = "{bank.bank_id}"'
    my_cursor.execute(delete_query)
    db.commit()
    update_bank_in_users_query = f'update users set bank = NULL where bank = "{bank.bank_id}"'
    my_cursor.execute(update_bank_in_users_query)
    db.commit()
    update_account_types_query = f'delete from account_types where bank = "{bank.bank_id}"'
    my_cursor.execute(update_account_types_query)
    db.commit()
    my_cursor.close()
    print('Bank successfully deleted')
    return None


def update_bank(bank):
    update_query = f'update banks set bank_name = "{bank.name}", location = "{bank.location}" ' \
                   f'where bank_id = "{bank.bank_id}"'
    my_cursor = db.cursor()
    my_cursor.execute(update_query)
    db.commit()
    my_cursor.close()
    print("Bank has been updated")


def check_bank_exists(bank):
    my_cursor = db.cursor()
    select_query = f'SELECT * FROM banks WHERE bank_name = "{bank.name}" and location = "{bank.location}"'
    my_cursor.execute(select_query)
    record = my_cursor.fetchall()
    row_count = my_cursor.rowcount
    if row_count > 0:
        my_cursor.close()
        return True, record[0]
    else:
        my_cursor.close()
        return False, 0


def load_bank(bank_id):
    select_query = f'select * from banks where bank_id = {bank_id}'
    my_cursor = db.cursor()
    my_cursor.execute(select_query)
    record = my_cursor.fetchall()
    row_count = my_cursor.rowcount
    my_cursor.close()
    if row_count > 0:
        bank_name = record[0][0]
        bank_location = record[0][1]
        bank_id = record[0][2]
        bank = [bank_name, bank_location, bank_id]
        return bank


def load_all_banks():
    banks = []
    select_query = 'select * from banks'
    my_cursor = db.cursor()
    my_cursor.execute(select_query)
    rows = my_cursor.fetchall()
    for row in rows:
        banks.append(row)
    my_cursor.close()
    return banks


def insert_account_type(account_type):
    cursor = db.cursor()
    insert_query = f'insert into account_types (account_type, bank, interest_rate, monthly_fees, minimum_balance, ' \
                   f'max_withdrawals) values ("{account_type.account_type}", "{account_type.bank}", ' \
                   f'"{account_type.interest_rate}", "{account_type.monthly_fees}", "{account_type.minimum_balance}"' \
                   f', "{account_type.max_withdrawals}") '
    cursor.execute(insert_query)
    db.commit()
    cursor.close()
    print('Account type successfully inserted into account_types table')


def remove_account_type(type_id):
    cursor = db.cursor()
    delete_query = f'delete from account_types where account_type_id = "{type_id}"'
    cursor.execute(delete_query)
    db.commit()
    update_referencing_accounts_query = f'update accounts set account_type_id = NULL where account_type_id = ' \
                                        f'"{type_id}"'
    cursor.execute(update_referencing_accounts_query)
    db.commit()
    cursor.close()
    print('Account type successfully deleted')


def load_account_types(bank):
    cursor = db.cursor()
    select_query = f'select * from account_types where bank = {bank.bank_id}'
    cursor.execute(select_query)
    record = cursor.fetchall()
    cursor.close()
    return record

def fetch_account_type(type_id):
    cursor = db.cursor()
    select_query = f'select * from account_types where account_type_id = "{type_id}"'
    cursor.execute(select_query)
    record = cursor.fetchall()
    row_count = cursor.rowcount
    cursor.close()
    if row_count > 0:
        account_name = record[0][0]
        account_bank = record[0][1]
        account_interest = record[0][2]
        account_fee = record[0][3]
        account_min_bal = record[0][4]
        account_max_withdrawal = record[0][5]
        account_id = record[0][6]
        account_type = [account_name, account_bank, account_interest, account_fee, account_min_bal, account_max_withdrawal,
                        account_id]
        return account_type

def update_account_info(account, field_name, value):
    update_query = f'update account_types set {field_name} = "{value}" where account_type_id = "{account.account_type_id}"'
    cursor = db.cursor()
    cursor.execute(update_query)
    db.commit()
    cursor.close()
    print('Account type has been updated')

