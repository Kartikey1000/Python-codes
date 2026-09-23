'''def main():
    name=get_name()
    house=get_house()
    print(f"{name} from {house}")

def get_name():
    name=input("Name: ")
    return name


def get_house():
    house=input("House: ")
    return house


if __name__=="__main__":
    main()
'''
def main():
    student=get_student()
    if student[0]=="Padma":
        student[1]="Ravenclaw"
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name,"house": house}
#    student["name"]= input("Name: ")
#    student["house"]= input("House: ")
#    student={}
#    return student
#    house=input("House: ")
#    name=input("Name: ")
#    return [name,house]



if __name__=="__main__":
    main()
