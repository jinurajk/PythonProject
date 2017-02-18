class Person():
    def __init__(self,name):
        self.hidden_name = name
    def get_name(self):
        print("Inside the getter")
        return self.hidden_name
    def set_name(self,name):
        print("Inside the setter")
        self.hidden_name=name
    name = property(get_name, set_name)

# variable starts with two underscore camnnot be accessed outside the class
class Duck():
    def __init__(self,name):
        self.__name = name
    @property
    def name(self):
        print("Inside getter")
        return self.__name
    @name.setter
    def name(self,name):
        print("Inside setter")
        self.__name = name

abcd = Duck("AAAAA")
print(abcd.name)
abcd.name = "Donald"
print(abcd.name)
#Cannot access  abcd.__name

fowl = Person("Howard")
print(fowl.name)
fowl.name = "Abcgde"
print(fowl.name)