# Person.py
class Person:
    # constructor
    def __init__(self, id, name, email, active=False):
        self.id = id
        self.name = name
        self.email = email
        self.active = active
        
    def __str__(self):
        return f"{self.id}:{self.name} {self.email} {"Active" if self.active else "Inactive"}"
    
    def __repr__(self):
        return f"[{self.id}:{self.name} {self.email} {"Active" if self.active else "Inactive"}]"
    
    def display(self):
        print (self)

if __name__ == "__main__":
    p = Person(1, "Aidan", "aidan@gmail.com", True)
    print(p)

    p2 = Person(2, "Brenda", "brenda@gmail.com", False)
    print(p2)

    p3 = Person(3, "Carol", "carol@gmail.com")
    print(p3)