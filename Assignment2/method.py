class Employee:
    def __init__(self, name):
        self.name=name

    def greet(self):
        print("Hello",self.name)

e1=Employee("Aayush")

e1.greet()