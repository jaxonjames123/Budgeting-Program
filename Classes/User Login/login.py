

def login():
    username = input('Username: ').rstrip().lower()
    pt_password = getpass.getpass()
    user_info = load_user(username)[1]
    if load_user(username)[0] and check_encrypted_password(pt_password, user_info[3]):
        print(f'Login Successful!\n')
        return user_info
