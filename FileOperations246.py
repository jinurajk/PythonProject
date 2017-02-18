import glob
import os

print(".py files starting with F", glob.glob("F*.py"))

print(".py files starting with Fo", glob.glob("Fo*.py"))
print(".py files starting with C or T", glob.glob("[CT]*.py"))

print ("Current working directory ", os.getcwd())
print("Process id is ", os.getuid())
