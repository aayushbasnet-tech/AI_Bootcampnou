class Person:
    def speak(self):
        print("I can speak")

class Student(Person):
    def study(self):
        print("I can study")

s1 = Student()
s1.speak()
s1.study()