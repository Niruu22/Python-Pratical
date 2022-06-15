class Emp:
    
    empCount=0
    def init_(self,name,salary):
        self.name=name
        self.salary=salary
        Emp.empCount +=1

    def displayCount(self):
        print("Total Employee %d" %Emp.empCount)

    def displayEmp(self):
        print("Name: ", self.name, "salary = ",self.salary)
