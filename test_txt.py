students = ["Ahmad", "Noura", "Sara", "Mona "]


with open("test.txt", "w") as file:
    for student in students:                      #must for loop
        file.write(student + " ")
    print(f"the file was created successfuly")


with open("test.txt","r") as file:
    reader = file.read()
    print(reader)