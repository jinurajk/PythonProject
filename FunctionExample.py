
# Function definition 1
def newfunct(str):
 print(str)
 return
# Function definition 2
def changeme( mylist ):
   #"This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print ("Values inside the function: ", mylist)
   return


# Call function
newfunct("Welcome to Python")
newfunct("This is Python funtion example")

mylist = [10,20,30];
changeme( mylist );
print ("Values outside the function: ", mylist)