# file = open("Text.txt", "x")        #For Creating Purpose

# file = open("Text.txt", "w")        #For Writing Purpose
# file.write("This is an example")
# file.close

file =open("Text.txt", "r")         #For Reading Purpose
print(file.read())
file.close

# file =open("Text.txt" , "a")      #For Append Purpose
# file.write("This is Append")
# file.close