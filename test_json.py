import json


student = {"Name" :"Hanan",
           "Age": 30,
           "Class":"D"}


with open("test.json","w")as file:
    json.dump(student, file, indent = 4)
    print("file add successful")

with open("test.json", "r") as file:
    data = json.load(file)
    print(data)