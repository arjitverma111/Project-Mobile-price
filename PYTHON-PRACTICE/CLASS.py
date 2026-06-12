#TO WRITE A CLASS CALCULATOR
x= int(input("Enter 1st number:"))
y= int(input("Enter 2nd number:"))
class calculator :
   sum = x+y 
   division = x/y
   multiplication = x*y
   subtraction = x-y

   def sum1(self):
      print(f"sum of {x}&{y} is {self.sum}")

   def multi(self):
      print(f"multi of {x}&{y} is {self.multiplication}")

   def div(self):
      print(f"div of {x}&{y} is {self.division}")

   def subt(self):
      print(f"subt of {x}&{y} is {self.subtraction}")

calc= calculator()
ch= input("choose operation: ")
operation= {"div" : calculator.div , "multi" : calculator.multi , "sum1" : calculator.sum1, "subt" : calculator.subt}

print(operation[ch](calc)) 


