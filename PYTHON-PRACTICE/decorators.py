# decorators


# classmethod - used to fetch class attribute even in the presence of instance attribute

class arjit (): 
    a=1
    @classmethod
    def prints(cls):
        print(f"classmethod prioritize class attribute, a = {cls.a}")

method = arjit()
method.a = 50
print(method.prints())   # arjit.prints(method) will not work here-- classmethod works differently or use method.prints