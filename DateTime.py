import time

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)

print (time.localtime(time.time()))
localtime =  time.asctime(time.localtime(time.time()))

print ("Local Time is @", localtime)
print ("Local Time is #", time.strptime(localtime,'%a %b %d %H:%M:%S %Y'))

print ("Current CPU time in float :", time.clock())

print ("Ctime ex :", time.ctime())
print ("GM Time example : " , time.gmtime())

#print (time.timezone())
