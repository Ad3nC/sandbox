import os

print("The files in {} are:".format(os.getcwd()))
items = os.listdir('.')
for item in items:
    print(item)
