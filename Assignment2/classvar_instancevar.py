class Student:
    school="ABC School"      # Class Variable

    def __init__(self,name):
        self.name=name       # Instance Variable

s1=Student("Aayush")
s2=Student("Rahul")

print(s1.school)
print(s2.school)
print(s1.name)
print(s2.name)