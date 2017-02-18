# Open a file
fo = open("foo.txt", "r+")
print ("Reading data from file foo.txt \n\n")

str1 = fo.read(10)
print (str1)

# Check current position
position = fo.tell()
print ("Current file position : ", position)

position = fo.seek(0);
#str = fo.read( )
print ("\n\n",fo.read( ))

# Close opend file
fo.close()

print ("Is file closed now: ", fo.closed)