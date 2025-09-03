# Person.py
class Person:
    # constructor
    def __init__(self, name, email, active):
        self.name = name
        self.email = email
        self.active = active
        
    def __str__(self):
        return f"{self.name} {self.email} {"Active" if self.active else "Inactive"}"
    
    def display(self):
        print (self)

if __name__ == "__main__":
    p = Person("Aidan", "aidan@gmail.com", True)
    print(p)

    p2 = Person("Brenda", "brenda@gmail.com", False)
    print(p2)
