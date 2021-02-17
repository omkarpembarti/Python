class start:
    def takeinput(self):
        self.name = input("Enter Employe name: ")
        self.id = input("Enter ID: ")
        EmpObject = Employee(self.name,self.id)


class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.takeProfile()

    def takeProfile(self):
        self.title = input("Enter your designation: ")
        self.printAllData()
    
    def printAllData(self):
        print(self.name)
        print(self.id)
        print(self.title)


begin = start()
begin.takeinput()    

        
