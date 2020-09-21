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
                          "bank_id INT NOT NULL AUTO_INCREMENT,  PRIMARY KEY(bank_id));")
        print("Banks table created")
    if not check_table_exists('users'):
        my_cursor.execute("CREATE TABLE users (first_name VARCHAR(255), last_name VARCHAR(255), username VARCHAR("
                          "255), password VARCHAR(255), dob DATE, ssn VARCHAR(255), email VARCHAR(255), bank INT, "
                          "PRIMARY KEY(username), FOREIGN KEY(bank) REFERENCES banks(bank_id));")
        print("Users table created")
    my_cursor.close()


def delete_tables():
    my_cursor = db.cursor()
    query2 = "drop table users"
    my_cursor.execute(query2)
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
    select_query = 'SELECT * FROM users WHERE username = %s'
    my_cursor.execute(select_query, (username,))
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
        user = [first_name, last_name, username, password, dob, ssn, email]
        return user


def insert_bank(bank):
    my_cursor = db.cursor()
    insert_query = f'insert into banks (bank_name, location) VALUES ("{bank.name}", "{bank.location}")'
    my_cursor.execute(insert_query)
    db.commit()
    my_cursor.close()
    print("Bank successfully inserted into banks table\n")


def remove_bank(bank):
    my_cursor = db.cursor()
    bank_id = get_bank_id(bank)
    delete_query = f'delete from banks where bank_id = "{bank_id}"'
    my_cursor.execute(delete_query)
    db.commit()
    update_bank_in_users_query = f'update users set bank = NULL where bank = "{bank_id}"'
    my_cursor.execute(update_bank_in_users_query)
    db.commit()
    my_cursor.close()
    print('Bank successfully deleted')


# Should return the id of the bank that is passed into the constructor
def get_bank_id(bank):
    query = f'Select bank_id from banks where bank_name = "{bank.name}" and location = "{bank.location}"'
    my_cursor = db.cursor()
    my_cursor.execute(query)
    record = my_cursor.fetchall()
    my_cursor.close()
    return record[0][0]

def update_bank(bank, bank_id):
    update_query = f'update banks set bank_name = "{bank.name}", location = "{bank.location}" ' \
                   f'where bank_id = "{bank_id}"'
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
        return False, print('')

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
        bank = [bank_name, bank_location]
        return bank
