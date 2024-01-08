import os
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

filename = "sample.txt"
filename2 = "readme.md"

# read file
myfile = open(filename, "r")
print(myfile.read())


# read file only some characters
print(myfile.read(5))

# readlines - wiill read first two lines
print(myfile.readline())
print(myfile.readline())


for x in myfile:
    print(x)

myfile.close()

# -----------------------WRITE FILE--------------------------------
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content
#  x to create new file

f = open(filename, "a")
f.write("Now the file has more content!")
f.close()

# open and read the file after the appending:
f = open(filename, "r")
print(f.read())

f = open(filename, "w")
f.write("Woops! I have deleted the content!")
f.close()

# open and read the file after the overwriting:
f = open(filename, "r")
print(f.read())


