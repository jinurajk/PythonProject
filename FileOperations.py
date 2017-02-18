# Open a file
fo = open("foo.txt", "a+")
print ("Name of the file: ", fo.name)
print ("Mode of file: ", fo.mode)
print ("Is file closed: ", fo.closed)

fo.write( "Python is a great language.\nYeah its great!!\n")
# Close opend file
fo.close()

print ("Is file closed now: ", fo.closed)