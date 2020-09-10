import mysql.connector


users_db = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='hhrS15513',
    database='user_accounts'
)
my_cursor = users_db.cursor()
# my_cursor.execute("CREATE TABLE users (first_name VARCHAR(255), last_name VARCHAR(255), username VARCHAR(255), "
#                   "password VARCHAR(255), dob DATE, ssn VARCHAR(255), email VARCHAR(255))")
#
# my_cursor.execute("CREATE TABLE banks (name VARCHAR(255), location VARCHAR(255), users VARCHAR(255))")