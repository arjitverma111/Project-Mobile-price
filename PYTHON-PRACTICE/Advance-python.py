# # type hints

# x : int = 5   #whenever i will use x later in my program it will tell its type to me 

# def typehints(x: str, y: str) -> str :
#     print(x+y)

# typehints("hello", "world")

# #--------------------------------------------------------------------------------------------------------------

# # MATCH CASE  (similar to switch you learned in C)

# def status(score):
#     match score:
#         case 100:
#             print("Century")
#         case 200:
#             print("double century")
#         case _:
#             print("good run")
    
# status(50)
# status(100)

# #---------------------------------------------------------------------------------------------------------------

# # to merge to dictionaries 

# d1 = {"a" : 1, "b": 2}
# d2 = {"c" : 3, "d": 4}

# d3 = d1 | d2
# print(d3)

# #---------------------------------------------------------------------------------------------------------------

# #Exception Handling

# print ("Handling exception using try...except...else...finally")
# try:                                               # put suspicious code in the try clause
#     numerator=50
#     denom=int(input("Enter the denominator: "))
#     quotient=(numerator/denom)
#     print ("Division performed successfully")
# except ZeroDivisionError:
#     print ("Denominator as ZERO is not allowed")
# except ValueError:
#     print ("Only INTEGERS should be entered")
# else:                                              # else clause sirf tbhi print hoga jb exception raise nhi hogi
#     print ("The result of division operation is ", quotient)
# finally:                                           #finally clause har situation m print hoga no matter exception has been raised or not 
#     print ("OVER AND OUT")      
# 
# 
# #---------------------------------------------------------------------------------------------------------
#         

# # importing func() from other files

# from module import myfunc

# myfunc()                   # this imported myfunc from module.py

# print(__name__)            # this will print "<name of the file in which it has been called>"

# #------------------------------------------------------------------------------------------------------------

# # Enumerate - it retrieves index and item simuntaneously

# l = [10,15,12,23,26,28,18]

# for index , item in enumerate(l):
#     print(f"index is {index}, item is {item}")

#     ## output index is 0, item is 10
#        # # index is 1, item is 15
#        # # index is 2, item is 12
#        # # index is 3, item is 23
#        # # index is 4, item is 26
#        # # index is 5, item is 28
#        # # index is 6, item is 18

# #------------------------------------------------------------------------------------------------------------
# # List comprehension  --- used replace append function

# l1 = [10,15,12,23,26,28,18]
# l2 = []
# # for i in l1:
# #    l2.append(i*i)

# l2 = [i*i for i in l1]
# print(l2)


# #---------------------------------------------------------------------------------

# # Lambda function  ---  <name of fxn> = lambda <input> : <output>

## def square(n):
##     return(n*n)

## instead we can use lamda function

# square= lambda n :  (n*n)

# print(square(5))

# #---------------------------------------------------------------------------------

## format method

# ({} and {} are really good boys).format("arjit", "sanchit")

# #---------------------------------------------------------------------------------

# # MAP - applies the fucntion to all the elements in a list

l = [1,12,3,5,151,252,26]

square = lambda n : n*n

l2 = map(square,l )


print(list(l2))

# # Filter -- removes those elements from the list which returns false

def even(n):
    if(n%2)==0:
        return True
    return False

l3 = filter(even,l)


print(list(l3))

# # Reduce -- Sequential computation
from functools import reduce

def sum(a,b):
    return a+b

print(reduce(sum, l))

