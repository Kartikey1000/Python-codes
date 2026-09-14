#list
students=['hermo','harry','roon']

for i in range(0,len(students)):
    print(students[i])
for student in students:
    print(student)


#Dictionary
#students=["a","b","c","d"]
#houses = ["G","G","G","s"]

students={
    "H":"  G",
    "ha":" G",
    "Ron":"G",
    "D":"  S"
}

for student in students:
    print(student,students[student])


students=[

    {"name":"A","House":"a","Perto":"1"},
    {"name":"B","House":"b","Perto":"2"},
    {"name":"C","House":"c","Perto":"3"},
    {"name":"D","House":"d","Perto":None}
]

for student in range(len(students)):
    print(students[student]) 

#can be done in neat manner
students = [
    {"name": "A", "House": "a", "Perto": "1"},
    {"name": "B", "House": "b", "Perto": "2"},
    {"name": "C", "House": "c", "Perto": "3"},
    {"name": "D", "House": "d", "Perto": None}
]

for student in students:
    print(f"{student['name']} is in house {student['House']} and has pet {student['Perto']}")
