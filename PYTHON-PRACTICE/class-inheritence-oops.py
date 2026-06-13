

# # multi-level inheritence

# class employer:
#     name= "Arjit"
    
#     def na(self):
#         print(f"name of employee is {self.name}")

# class employee(employer):
#     name1= "sanchit"
#     age = 19
    
#     def empl(self):
#         print(f"name of employer is {self.name1} and his age is {self.age}")

# class randomm(employee):
#     a=3

#     def random1(self):
#         print(f"name if employer is {self.name}, employee is{self.name1}, value of a is{self.a}")

# x = randomm()
# print(x.name)
# print(x.name1)
# print(randomm.random1(x))

# y=employer()
# print(x.na())

#-------------------------------------------------------------------------------------------------------------

#multiple inheritence

# class X():
#     a= 1

# class y():
#     b = 2

# class z(X,y):
#     c= 3
#     def p(self):
#         print(f"a= {self.a}, b= {self.b}, c= {self.c}")

# inheritence = z()
# print(z.p(inheritence))

#--------------------------------------------------------------------------------------------------------------

# # SUPER

# class employee():
#     def __init__(self):
#         print("constructor of employee")

# class programmer(employee):
#     def __init__(self):
#         print("constructor of programmer")

# class manager(programmer):
#     def __init__(self):
#         super().__init__()                    #get constructer of programmer     # THIS WAY IT WILL PRINT T
        
#         print("constructor of manager")

# super_inheritence = manager()

#------------------------------------------------------------------------------------------------------------



