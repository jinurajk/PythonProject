import os
chk = os.path.exists("foo.txt")
print("Is file foo.txt exist? ", chk)
print("Is file ajhjdh.hh exist? " ,os.path.exists("ajhjdh.hh"))

print("Is Tkinter.py a file? ", os.path.isfile("Tkinter.py"))
print("Is Tkinter.py a directory? " , os.path.isdir("Tkinter.py"))

print(os.path.isdir("Phone"))
print("\Phone\__pycache__ Is it absolutepath -- ", os.path.isabs("\Phone\__pycache__"))

print(os.path.abspath("Tkinter.py"))
print("Files in \Phone\__pycache__ folder ", os.listdir("Phone\__pycache__"))