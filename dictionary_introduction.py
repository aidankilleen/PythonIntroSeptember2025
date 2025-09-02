# dictionary_introduction.py


user = {
    'id': 1001,
    'name': 'Alice', 
    'email': 'alice@gmail.com', 
}

print (user)

print (user['name'])
print (user['email'])

print (user.keys())
print (user.values())
print (user.items())

for k in user:
    print (f"{k}={user[k]}")

# dictionaries are mutable
user['id'] = 9999
user['address'] = "101 Grand Canal, Dublin 1"

print (user)
