import csv

students =[["Name","Age","Class"],
           ["Hanan",30,"MS"],
           ["Njad",4,"D"],
           ["Fahad",40,"D"]]

with open("test.csv","w", newline ="") as file:
    writer = csv.writer(file)
    writer.writerows(students)
print("file was created successfully")

with open("test.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader) #split hader from data output don't show header
    for row in reader:
        print(row)