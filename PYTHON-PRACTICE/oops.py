# class Employee :
#     salary = 12000
#     age = 30

# arjit = Employee()

# print(arjit.salary , arjit.age)

#----------------------------------------------------------------------------------------

# class Employee :
#     salary = 12000      # it is class attribute
#     experience = 13     # it is class attribute

# harsh = Employee()

# harsh.name ="Harsh"     # it is onject attribute
# harsh.salary= 13000     # it is a instance attribute

# print(harsh.name, harsh.salary, harsh.experience)   #preference always given to intsance attribute

#---------------------------------------------------------------------------------------

# class Employee:
#     salary = 12000      # it is class attribute
#     experience = 13

#     def function1(self):    #function defined (self parameter)
#      print(self.salary,self.experience) 

# harry = Employee()
# Employee.function1(harry)


#------------------------------------------------------------------------------------------


# class Employee:
#     salary = 12000      # it is class attribute
#     experience = 13
#     age=30

#     def __init__(self):     #function calls on itself (dunder method)
#        print(self.salary,self.experience) 

#     def function1(self):    #function defined (self parameter)
#      print(self.salary,self.experience) 

#     @staticmethod           #this states that the function has no need to have self parameter 
#     def goodmorning():
#        print("good morning")  

#     def itself(self,salary,experience,age):
#        print(f"age is {self.age}, salary is {self.salary}, experience is {self.experience}")

# harry = Employee()
# Employee.function1(harry)

#----------------------------------------------------------------------------------------

# class Employee:
#     salary = 12000      # it is class attribute
#     experience = 13
#     age=30



#     def __init__(self, sal, ex, ag):
#        self.salary = sal
#        self.age = ag
#        self.experience = ex
#        print(f"age is {self.age}, salary is {self.salary}, experience is {self.experience}")

# harry = Employee(1500,2,20)   # IT WILL PRINT 1500,2,20 - WE KINDA PROVIDED A INSTANCE ATTRIBUTE
# print(harry.salary, harry.age)

#---------------------------------------------------------------------------------------

# whenever we have to intake values in a class use dunder method

class calculator:
    def __init__(self,x,y):
        self.x = x
        self.y =y

    def sum(self):
        print(f"sum is {self.x + self.y}")

cal = calculator(3,7)

calculator.sum(cal)





