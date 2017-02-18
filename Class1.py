class Employee:
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print ("Total Employee %d" %(Employee.empCount))

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)


emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
emp3 = Employee("Ahjd", 534)
emp4 = Employee("Eddw", 5454)
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp4.displayEmployee()
print ("Total Employee %d" %Employee.empCount)

# Returns true if 'name' attribute exists
print("Emp1 one has the attribute 'name'?", hasattr(emp1, 'name'))
# Returns value of 'age' attribute  
print("Emp3 name is :", getattr(emp3, 'name'))
# Set attribute 'age' at 8
setattr(emp2, 'name', "XXXX")
print("Newly set name for Emp2 : ", getattr(emp2, 'name'))
# Delete attribute 'name' for Emp4
#delattr(emp4, 'name')
#emp4.displayEmployee()
