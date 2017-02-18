# Function definition is here
def printme( str ):
   print (str)
   return;

# Function definition is here
def printme( str ):
   print (str)
   return;

# Function definition is here
def printinfo( name, age ):
   print ("Name: ", name)
   print ("Age ", age)
   return;

# Function definition is here
def printinfo( name, age = 35 ):
   print ("Name: ", name)
   print ("Age ", age)
   return;


# Now you can call printme function
printme("Welcome to Python")


# Now you can call printme function
printme( str = "My string")

# Now you can call printinfo function
printinfo( age=50, name="miki" )


# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )