# data_structure_introduction.py


team = [
    {
        'id': 1001, 
        'name':'Alice', 
        'email':'alice@gmail.com', 
        'active':True, 
        'languages':('Python', 'C#', 'Java')
    },
    {
        'id': 1002, 
        'name':'Bob', 
        'email':'bob@gmail.com', 
        'active':True, 
        'languages':('Java')
    },
    {
        'id': 1003, 
        'name':'Charlie', 
        'email':'charlie@gmail.com', 
        'active':True,
        'languages':('C#', 'Java')
    },
    {
        'id': 1004, 
        'name':'Donna', 
        'email':'donna@gmail.com', 
        'active':True, 
        'languages':('Python', 'Java')
    }
]

for member in team:
    print (f"name:{member['name']}")
    for lang in member['languages']:
        print (f" - {lang}")

