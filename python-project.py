# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 17:34:38 2019

@author: Ammar
"""

print("Project_1")
print("======================================================================")
import statistics
from functools import reduce
class Person():
    def __init__(self,Name,Address):
        self.__Name = str(Name)
        self.__Address=str(Address)
    def getName (self):
        return self.__Name
    def setName (self,newName):
        self.__Name = newName
        return print (self.getName(),"new Name :",self.getName())
    def getAddress (self):
        return self.__Address
    def setAddress (self,newAddress):
         self.__Address = newAddress
         return print (self.getName(),"new Address :",self.getAddress())
# =============================================================================
#    def __del__ ( self ):
#        print ("Has been deleted")
# =============================================================================
class Employee (Person):
    def __init__(self,EmployeeNumber,Name,Address,salary,jobTitle,loans):
        super().__init__(Name,Address)
        self.EmployeeNumber = int(EmployeeNumber)
        self.__salary = float(salary)
        self.__jobTitle = str(jobTitle)
        self.__loans = list(loans)
    def getSalary(self):
        return self.__salary
    def setSalary(self,newSalary):
        self.__salary = newSalary
    def getJobTitle(self):
        return self.__jobTitle
    def setJobTitle(self,newJobTitle):
        self.__jobTitle = newJobTitle
    def getTotalLoans(self):
        return sum(self.__loans)
    def getloans(self):
       return self.__loans
    def loanstotal(self):
       total=sum(self.__loans)
       return total
    def MaxLoans(self):
        if(len(self.__loans))==0:
            maxLoans="Empty"
        else:
           maxLoans=max(self.__loans)
        return maxLoans
    def MinLoans(self):
        if(len(self.__loans))==0:
           minLoans="Empty"
        else:
           minLoans=min(self.__loans)
        return minLoans
    def setLoans(self,newLoans):
        self.__loans = newLoans
    def LowestAndHighe(self):
        low = 0
        high = 0
        if self.__loans:
            low = reduce(lambda a,b : a if a < b else b , self.__loans)
            high = reduce(lambda a,b : a if a > b else b , self.__loans)
        return (low,high)
    def printEmployeeInfo(self):
        print ("Employee Number :",self.EmployeeNumber)
        print ("salary :",self.__salary)
        print ("jobTitle :",self.__jobTitle)
        print ("loans :",self.__loans)
#    def __del__(self):
#        print ("i have been deleted")
Employee1 = Employee(1000,"ahmad yazan","amman,jordan",500,"HR consultant",[434,200,1020])
Employee2 = Employee(2000,"Hala Rana","Aqaba,jordan",750,"Deparment Manager",[150,3000,250])
Employee3 = Employee(3000,"Mariam Ali","Mafraq,jordan",600,"HR S consultant",[304,1000,250,300,500,235])
Employee4 = Employee(4000,"Yasmeen Mohammad","Karak,jordan",865,"Director",[])
print(Employee1.printEmployeeInfo())
print("======================================================================")
print(Employee2.printEmployeeInfo())
print("======================================================================")
print(Employee3.printEmployeeInfo())
print("======================================================================")
print(Employee4.printEmployeeInfo())
print("======================================================================")
class Student(Person):
    def __init__(self,number,Name,Address,Subject,Marks):
        super().__init__(Name,Address)
        self.Number = int(number)
        self.__Subject = str(Subject)
        self.__Marks=dict(Marks)
    def getSubject(self):
        return self.__Subject
    def setSubject(self,newSub):
        self.__Subject = newSub
    def getMarks(self):
        return self.__Marks
    def setMarks(self,newMarks):
        self.__Subject = newMarks
    def getAvarage(self):
        return statistics.mean(self.__Marks[key] for key in self.__Marks)
    def getAMarks(self):
        thedict={key:value for (key,value) in self.__Marks.items() if value >= 90}
        return thedict
    def Studentinfo(self):
        print("Student Number :" ,self.Number )
        print("Name :" ,self.getName())
        print("Address :" ,self.getAddress())
        print("Subject :",self.__Subject)
        print("Marks :",self.__Marks)
        print("Avarage :",self.getAvarage())
        print("HighMark :",self.getAMarks())
#     def __del__ ( self ):
#        print ("Has been deleted")
# =============================================================================
student1 = Student(20191000,"khalid ali","irbid,jordan","History",{'English':80,'Arabic':90,'Art':95,'Mangemnt':75})
student2 = Student(20181000,"Reem Hani","Zarqa,jordan","SoftwareEng",{'English':80,'Arabic':90,'Calculus':85,'Mangemnt':75,'OS':73,'programming':90})
student3 = Student(20161000,"Nawrass Abdulla","Amman,jordan","Arts",{'English':83,'Arabic':92,'Art':90,'Mangemnt':70})
student4 = Student(20171000,"Amal Raed","Tafelah,jordan","Computer Eng",{'English':83,'Arabic':92,'Calculus':80,'Mangemnt':75,'OS':79,'programming':91})
print(student1.Studentinfo())
print("======================================================================")
print(student2.Studentinfo())
print("======================================================================")
print(student3.Studentinfo())
print("======================================================================")
print(student4.Studentinfo())
print("======================================================================")
print("Exc1")
EmployeeList=[]
EmployeeList.append(Employee1)
EmployeeList.append(Employee2)
EmployeeList.append(Employee3)
EmployeeList.append(Employee4)
#=============================================================================
print("\n")
print("Exc2")
StudentList=[]
StudentList.append(student1)
StudentList.append(student2)
StudentList.append(student3)
StudentList.append(student4)
#=============================================================================
print("\n")
print("Exc3")
def numberofEmployee (EmployeeList):
     print(len(EmployeeList))
print(numberofEmployee(EmployeeList))
#=============================================================================
print("\n")
print("Exc4")
def numberOfStudent(StudentList):
     print(len(StudentList))
def infofEmployee(StudentList):
     for index,student in enumerate( StudentList):
         print(StudentList[index].print_info())
print(numberOfStudent(StudentList))
#=============================================================================
print("\n")
print("Exc5")
def infoOfEmployee(EmployeeList):
    for index,Employee in enumerate(EmployeeList):
        print(EmployeeList[index].printEmployeeInfo())
print(infoOfEmployee(EmployeeList))
#=============================================================================
print("\n")
print("Exc6")
def getAllStudentsInfo():
    for x in StudentList:
        print (x.Studentinfo(),"\n----------------------------")
    return ""
print (getAllStudentsInfo())
#=============================================================================
print("\n")
print("Exc7")
highestAvarege=[]
def getHighestAvarege():
    for x in StudentList:
        highestAvarege.append(x.getAvarage())
    print ("The Highest Avarege Is :",max(highestAvarege))
    return ""
print (getHighestAvarege())
#=============================================================================
print("\n")
print("Exc8")
def minloan(EmployeeList):
     minlist=[]
     for index,Employee in enumerate( EmployeeList):
          if type(EmployeeList[index].MinLoans())==int:
             minlist.append(EmployeeList[index].MinLoans())
     print (min(minlist))
print(minloan(EmployeeList))
#=============================================================================
print("\n")
print("Exc9")
def maxloan(EmployeeList):
     maxlist=[]
     for index,Employee in enumerate( EmployeeList):
          if type(EmployeeList[index].MaxLoans())==int:
             maxlist.append(EmployeeList[index].MaxLoans())
     print (max(maxlist))
print(maxloan(EmployeeList))
#=============================================================================
print("\n")
print("Exc10")
def listOfLoan(EmployeeList):
    totalList=[]
    result=0
    for index,Employee in enumerate(EmployeeList):
        totalList.append(EmployeeList[index].getloans())
        totalList.append(EmployeeList[index].loanstotal())
    for index,Employee in enumerate( EmployeeList):
          result=EmployeeList[index].loanstotal()+result
    print("The grant total loans across all employees =",result)
    print(totalList)
print(listOfLoan(EmployeeList))
#=============================================================================
print("\n")
print("Exc11")
def loanDic(EmployeeList):
     loanDic={}
     for index,Employee in enumerate( EmployeeList):
          loanDic[ EmployeeList[index].EmployeeNumber]=EmployeeList[index].getloans()
     print (loanDic)
print(loanDic(EmployeeList))
#=============================================================================
print("\n")
print("Exc12")
for key in range(len(EmployeeList)):
    print (EmployeeList[key].LowestAndHighe())
#=============================================================================
print("\n")
print("Exc13")
for x in StudentList:
    print("\n")
    print("StudentName",x.getName())
    print("\n")
    print("StudentSubject",x.getSubject())
    print("\n")
    print("StudentAmarks ",x.getAMarks())
    print("\n")
#=============================================================================
print("\n")
print("Exc14")
maxSalary =0
for x in EmployeeList:
    if x.getSalary() > maxSalary:
        maxSalary = x.getSalary()
print("Highest Salary is : ",maxSalary)
#=============================================================================
print("\n")
print("Exc15")
minSalary= Employee1.getSalary()
for x in EmployeeList:
    if x.getSalary() < minSalary:
        maxSalary = x.getSalary()
print("Lowest Salary is : ",minSalary)
#=============================================================================
print("\n")
print("Exc16")
sumSalary =0
for x in EmployeeList:
    sumSalary += x.getSalary()
print("Sum of all salaries is : ",sumSalary)
#=============================================================================
print("\n")
print("Exc17")
# =============================================================================
# for x in EmployeeList:
#     x.__del__()
# for y in StudentList:
#     y.__del__()
# =============================================================================
#=============================================================================