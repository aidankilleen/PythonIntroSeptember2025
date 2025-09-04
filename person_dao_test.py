# person_Dao_test.py
from Person import Person
from PersonDAO import PersonDAO

dao = PersonDAO()

p = Person(-1, "Zoe2", "zoe@gmail.com", True)


p = dao.add(p)

print (p)

p.name = "CHANGED"

p = dao.update(p)

people = dao.get_all()

for person in people:
    print (person.name)



dao.close()
