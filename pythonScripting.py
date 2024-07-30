import csv
import os
import datetime

with open("user_data.csv") as file:
    for line in file:
        #print(line) #printing this way will add an additional line because print command adds the additional line
        print(line.strip().upper()) #this will strip off the additional line added by the print command


#another way of reading the file into lists
## caution, this may take up lot of memory/cpu power if the file is huge

file1 = open("user_datatest_100.csv")
lines = file1.readlines()
file1.close()

print(lines)
print(lines[50])

print(os.path.getmtime("user_datatest_100.csv"))

timestamp = os.path.getmtime("user_datatest_100.csv")
print(datetime.datetime.fromtimestamp(timestamp))

print(os.path.getsize("user_data.csv"))

print(os.path.abspath("user_data.csv"))

## get cwd and print some messages
print(os.getcwd())

os.rmdir("testdir")
os.mkdir("testdir")


print(os.getcwd())
print(os.chdir("testdir"))

with open("testfile.txt", "w") as file2:
    file2.write("This is my first test file written by python")
    file2.write("Lets hope this works!")

with open("testfile.txt") as file3:
    for line in file3:
        print(line.strip())


dir = "testdir"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    print(fullname)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))

