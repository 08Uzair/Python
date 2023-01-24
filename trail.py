class Employee :
    def init (self,fname,lname,salary):
     self.fname=fname
     self.lname=lname
     self.salary=salary
harry=Employee('Uzer','Qureshi',1000000)
rohan=Employee('rohan','das',4400)
print(harry.fname,rohan.fname)