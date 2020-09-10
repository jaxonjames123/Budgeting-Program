from security import encrypt_password
import json

filename = './AdminLogin.json'
username = 'noxaj123'
password = encrypt_password('hhrS15513')
with open(filename, 'w') as f:
    json.dump({username: password}, f)
