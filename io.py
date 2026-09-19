
name=input("what's your name? ")



with open("names.txt","a") as file:
    file.write(f"{name}\n")


with open("names.txt","r") as file:
    lines= file.readlines()

for line in lines:
    print("Hello,",line.rstrip())


with open("names.txt","r") as file:
    for line in file:
        print("Hello,",line.rstrip())

names=[]
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello,{name}")

with open("names.csv") as file:
    for line in file:
        row=line.rstrip().split(",")#name,house
        print(f"{row[0]} is in {row[1]}")#instead of row0,1 we can use name,house 

students=[]

with open("names.csv") as file:
    for line in file:
        name,house=line.rstrip().split(",")
#       students.append(f"{name} is in {house}")
        student={"name":name,"house":house}
        #student["name"]=name
        #student["house"]=house
        students.append(student)
# def get_name(student):
#     return student["name"]

for student in sorted(students,key=lambda student: student["name"]):
   print(f"{student['name']} is in {student['house']}")

import csv 
students=[]

with open("names.csv") as file:
   #reader= csv.reader(file)
   reader= csv.DictReader(file)
   for row in reader:
      students.append({"name":row["name"],"house":row["house"]})
    

for student in sorted(students,key=lambda student: student["name"]):
   print(f"{student['name']} is in {student['house']}")


import csv

name=input("what's you name? ")
home =input("where your home")

with open("names.csv","a",newline="") as file:
    writer = csv.DictWriter(file,fieldnames=["name","home"])
    writer.writerow({"name":name,"home":home})



