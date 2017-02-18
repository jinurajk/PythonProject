list1 = [1,2,3,4,"jhj"]

print (list1)

list1[2] = 100

print (list1)

del list1[2]

print (list1)

print ("Length of list" ,len(list1))

print ("Membership of 3 is list " ,3 in list1)
print ("Membership of 2 is list " ,2 in list1)

list2 = [23,45,65, 3,45,65,22]
print ("Maximum value :" ,max(list2))
print ("Minimum value :" ,min(list2))

tuple1 =(23,45,76,"33d","hgd")
list3 = list(tuple1)
print ("Tuple is ", tuple1)
print ("List is ",list3)

list4 =[55,56,86,223,654,66,4,3,556,775]
print ("Before sorting " ,list4)
list4.sort()
print ("Sorted List " ,list4)
list4.sort(reverse=True)
print ("Reverse Sorted List " ,list4)
