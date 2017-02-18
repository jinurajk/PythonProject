import sys

Str = "this is string example....wow!!!";
Str = Str.encode('utf-8','strict');

print (sys.getdefaultencoding())


print ("Encoded String: " + Str)
#print ("Decoded String: " + Str.decode('ascii','strict'))