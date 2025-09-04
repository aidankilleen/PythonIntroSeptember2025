# PersonDAO.py
# read and write Person objects to and from a database
# DAO - Data Access Object

import sqlite3
from Person import Person

class PersonDAO():

    def __init__(self):
        self.conn = sqlite3.connect("./users.db")

    def close(self):
        self.conn.close()


    def get_all(self):
        sql = "SELECT * FROM users"
        cursor = self.conn.cursor()
        res = cursor.execute(sql)
        # use a list comprehension to extract from the db to an array of Person objects
        return [Person(record[0], record[1], record[2], record[3]) for record in res]

    def get_all_original(self):
        """get all of the Person objects from the database"""
        sql = "SELECT * FROM users"
        cursor = self.conn.cursor()
        res = cursor.execute(sql)
        people = []
        for record in res:
            p = Person(record[0], record[1], record[2], record[3])
            people.append(p)
        return people

    def delete(self, id):  
        sql = f"DELETE FROM users WHERE id = {id}"
        cursor = self.conn.cursor()
        res = cursor.execute(sql)

    def add(self, person: Person):
            sql = "INSERT INTO users (name, email, active) VALUES (?, ?, ?)"
            cursor = self.conn.cursor()
            cursor.execute(sql, (person.name, person.email, int(person.active)))
            self.conn.commit()
            # fetch the auto-generated id and update the object
            person.id = cursor.lastrowid
            return person

    def update(self, person: Person):
        sql = "UPDATE users SET name = ?, email = ?, active = ? WHERE id = ?"
        cursor = self.conn.cursor()
        cursor.execute(sql, (person.name, person.email, int(person.active), person.id))
        self.conn.commit()
        return cursor.rowcount > 0  # returns True if a row was updated

if __name__ == "__main__":
    pd = PersonDAO()

    people = pd.get_all()
    print (people)

    ##pd.delete(people[0].id)

    #people = pd.get_all()
    #print (people)
    pd.close()




