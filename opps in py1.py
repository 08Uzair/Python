class Employe:
    # increment=1.5
    def init (self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        self.increment=1.4
    # def increace(self):
    #     self.salary=int(self.salary*self.increment)

harry=Employe('harry','jackson',44000)
rohan=Employe('rohan','das',44000)

# print(harry.salary,rohan.salary) 
# harry.increase()
# rohan.increace()
# print(harry.salary,rohan.salary) 
