# person_Dao_test.py
from Person import Person
from PersonDAO import PersonDAO

dao = PersonDAO()

p = Person(-1, "Yvonne", "yvonne@gmail.com", True)
p = dao.add(p)
print (p)

p.name = "Yvonne Changed"
p.email = "yvonne.changed@gmail.com"
p.active = not p.active

dao.update(p)

people = dao.get_all()

print(people[-1])








""" p.name = "CHANGED"

p = dao.update(p)

people = dao.get_all()

for person in people:
    print (person.name)

 """

dao.close()
