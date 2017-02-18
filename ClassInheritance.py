class Person():
    def __init__(self,name):
        self.name = name
    def worktype(self):
        print("I can work anywhere")

class MDPerson(Person):
    def __init__(self, name):
        #self.name = "Doctor " +name
        super().__init__(name)

class JDPerson(Person):
    def __init__(self, name, age):
        self.name = "Lawyer " +name + age
    def worktype(self):
        print("I work in Hospital")

    def salary(self):
        print("10000 dollar")

person = Person("Alex")
doctor = MDPerson("Ann")
lawyer = JDPerson("Joex", " 20")

print(person.name)
print(person.worktype())
print(doctor.name)
print(lawyer.name)
print(lawyer.worktype())
print(lawyer.salary())