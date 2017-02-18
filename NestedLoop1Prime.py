# To check if a number is prime

i = 2
while(i < 20):
   j = 2
   while(j <= (i/j)):
      if not(i%j): 
       print("Hello", i%j)
       break
      j = j + 1
   if (j > i/j): 
    print("%d is prime" %(i))
   i = i + 1
print ("Good bye!")