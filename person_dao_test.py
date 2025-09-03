# person_Dao_test.py
from PersonDAO import PersonDAO

dao = PersonDAO()

people = dao.get_all()

for person in people:
    print (person.name)



dao.close()
