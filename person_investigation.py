# person_investigation.py

from Person import Person

p = Person(1, "Alice", "alice@gmail.com")
print (p)

people = [
    Person(1, "Alice", "alice@gmail.com", True), 
    Person(2, "Bob", "bob@gmail.com", False), 
    Person(3, "Carol", "carol@gmail.com", False), 
    Person(4, "Dan", "dan@gmail.com", True), 
    Person(5, "Eve", "eve@gmail.com", True), 
]
print (people)

for person in people:
    print (person.name)

names = [person.name for person in people]
print (names)

active_users = [person for person in people if person.active]
print (active_users)

p = Person(email="fred@gmail", name="Fred", id=99)
print(p)















