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
    if check_table_exists('users'):
        print("Users Table exists")
    else:
        my_cursor.execute("CREATE TABLE users (first_name VARCHAR(255), last_name VARCHAR(255), username VARCHAR("
                          "255), password VARCHAR(255), dob DATE, ssn VARCHAR(255), email VARCHAR(255), PRIMARY KEY("
                          "username));")
        print("Users table created")

    if check_table_exists('banks'):
        print("Banks Table exists")
    else:
        my_cursor.execute("CREATE TABLE banks (name VARCHAR(255), location VARCHAR(255), users_list VARCHAR(255), "
                          "bank_id INT NOT NULL AUTO_INCREMENT,  PRIMARY KEY(bank_id), FOREIGN KEY(users_list) "
                          "REFERENCES users(username));")
        print("Banks table created")
    my_cursor.close()


def delete_tables():
    my_cursor = db.cursor()
    query = f"DROP Table banks"
    my_cursor.execute(query)
    query2 = "drop table users"
    my_cursor.execute(query2)
    my_cursor.close()
    return True


def insert_user(first_name, last_name, username, password, dob, ssn, email):
    my_cursor = db.cursor()
    insert_query = ("insert into users (first_name, last_name, username, password, dob, ssn, email) VALUES "
                    f"('{first_name}', '{last_name}', '{username}', '{password}', "
                    f"STR_TO_DATE('{dob}','%Y-%m-%d'), '{ssn}', '{email}') ")
    my_cursor.execute(insert_query)
    db.commit()
    my_cursor.close()
    print("User successfully inserted into users table\n")


def load_user(username):
    my_cursor = db.cursor()
    select_query = 'SELECT * FROM users WHERE username = %s'
    my_cursor.execute(select_query, (username,))
    record = my_cursor.fetchall()
    first_name = record[0][0]
    last_name = record[0][1]
    username = record[0][2]
    password = record[0][3]
    dob = record[0][4]
    ssn = record[0][5]
    email = record[0][6]
    my_cursor.close()
    user = [first_name, last_name, username, password, dob, ssn, email]
    return user