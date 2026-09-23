class Student:
    def __init__(self,name,house):
        self.name=name
        self.house=house
#        self.petro=petro

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing name")
        self._name=name
        
    @property
    def house(self):
        return self._house
    @house.setter
    def house(self,house):
        if house not in ["Gryffindor","Huff","Raven","Sylth"]:
                raise ValueError("Invalid house")
        self._house=house

#    def charm(self):
#        match self.petro:
#            case "Stag":
#                return "🐴"
#            case "Otter":
#                return "🦦"
#            case "Jack Russel terrier":
#                return "🐶"
#            case _:
#                return "🪄"

def main():
    student=get_student()
#    student.house="Number Four,Pivet Drive"
    print(student) 
#    print("Expecto Patro!")
#    print(student.charm())   

def get_student():
    name= input("Name: ")
    house=input("House: ")
#    petro=input("Petro: ")
    return Student(name,house)

#   student=Student()
#   student.name=input("Name: ")
#   student.house=input("House: ")
#    return student
    

if __name__=="__main__":
    main()
 