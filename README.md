
#for read and write in  txt:

with open("file.txt", "r") as file:
print(file.read())



with open("file.txt", "r") as file:
for line in file:
print(line.strip())

with open("test.txt", "w") as file:
    for student in students:                      #must for loop
        file.write(student + " ")
    print(f"the file was created successfuly")


#for read and write in CSV:
import csv
with open('data.csv', newline=' ') as file:
reader = csv.reader(file) for row in reader:
print(row)
// reader = read file data


import csv
with open("data.csv", "w", newline=' ') as file:
writer = csv.writer(file)


#import json

with open("info.json", "r") as file:
data = json.load(file) // load = Read data file



with open("info.json", "w") as file:
json.dump(data, file) 




