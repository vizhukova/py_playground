import os

cwd = os.getcwd()  # Get the current working directory (cwd)
file_path = cwd + "/file_reading/data.txt"
data = ""

file_data = open(file_path, "r") # only read
# open("./people.txt", "w") # write
# open("./people.txt", "a") # append (no udate, only add new)
# open("./people.txt", "r+") # read and write

print("All data: " + data)
print("Get line: " + str(file_data.readline()))
# print("Arr of lines: " + str(file_data.readlines()))

if file_data.readable():
    data = file_data.read()

print('All data from the file besides first row: ' + data)
file_data.close() 

file_data = open(file_path, "a") # append (no udate, only add new)
file_data.write("\nToby - QA")
file_data.close()  

file_data = open(file_path, "w") #override all data in file
file_data.write("\nToby - QA")
file_data.close()  

file_path1 = cwd + "/file_reading/data1.txt"
file_data = open(file_path1, "w") #creates a new file
file_data.write("\nToby - QA")
file_data.close()  


