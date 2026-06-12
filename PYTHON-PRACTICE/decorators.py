# # decorators - these are functions which are take other functions as arguments and modify them

# def dec(fx):
#     def mfx():
#         print("goodmorning")
#         fx()
#         print("good evening")
#     return mfx()



# @dec
# def sum():
#     print("sum is 4")


# # SOME PREDEFINED DECORATORS

# # classmethod - used to fetch class attribute even in the presence of instance attribute

# class arjit (): 
#     a=1
#     @classmethod
#     def prints(cls):
#         print(f"classmethod prioritize class attribute, a = {cls.a}")

# method = arjit()
# method.a = 50
# print(method.prints())   # arjit.prints(method) will not work here-- classmethod works differently or use method.prints

# # property - converts a defined function into an attribute

# class decorators():

#     def __init__(self,first_name, last_name):
#         self.firstname = first_name
#         self.lastname = last_name
    
#     def fullname(self):
#         return(self.firstname,self.lastname)

#     @property           #now email is a attribute like "email =  self.firstname,".",self.lastname,"@gmail.com" "
#     def email(self):
#         print(self.firstname,".",self.lastname,"@gmail.com")


# x = decorators("arjit","verma")

# print(x.email)       #here we used email as a attribute instead of a function,  otherwise we had to write it as print(x.email())

# #------------------------------------------------------------------------------------------------------------------------------------------

# # setter - lets say i want to change value of an forced-attribute (a defined function with property decorator) ,so i use setter 

class decorators():

    def __init__(self,first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name
    
    @property
    def fullname(self):
        return(self.firstname,self.lastname)
    
    @fullname.setter
    def fullname(self, name):            # it took the new name and changed the value of first_name, last_name 
        first_name= name.split(" ")[0]
        last_name = name.split(" ")[1]

        self.firstname = first_name
        self.lastname = last_name




    @property           #now email is a attribute like "email =  self.firstname,".",self.lastname,"@gmail.com" "
    def email(self):
        print(self.firstname,".",self.lastname,"@gmail.com")


x = decorators("arjit","verma")

x.fullname = "Raja Ram"
print(x.email)
d    