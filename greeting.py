# greeting.py

def greet(name="", times=1):
    """
    ### greet
    this function prints a greeting  
    it takes the name and creates a   
    personalised greeting
    ~Parameters:~
    - 'name': name to greet - default = ""
    - 'times': how many times to print the greeting 1 by default
    """
    for i in range(times):
        print (f"Hello {name}")

# this detects is the module being run directly
# or is it being imported
if __name__ == "__main__":
    print (f"__name__:{__name__}")
    # test code
    greet("Aidan", 2)
    greet("Bob")




