import _thread
import threading
import time

# Defining function
def print_time(threadName, delay):
 count = 0
 print("Inside thread")
 while count < 5:
  time.sleep(delay)
  count +=1
  print("%s: %s" %(threadName, time.ctime(time.time())))
 print("Thread execution method is over")

# Creating 2 threads
try:
 _thread.start_new_thread(print_time, ("Thread1", 2))
 _thread.start_new_thread(print_time, ("Thread2", 4))
 print ("Number of threads :", threading.enumerate())
 print("Name of threads :", threading.getName())
except:
 print("Unable to start thread")

while 1:
 pass