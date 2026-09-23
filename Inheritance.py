class wizrad:
    def __init__(self,name):
        if not name:
            raise ValueError("Missing name")
        self.name=name



class Student(wizrad):
    def __init__(self,name,house):
        super().__init__(name)
        self.house=house


class Professor(wizrad):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject

Wizard = wizrad("Albus")
student= Student("Harry","Gryyf")
professor = Professor("Seve","defence")