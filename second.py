skincolor = ""
age = 0
height = 0
def miss(skincolor,age,height):
    if(skincolor == "fair"):
        return "skincolor not match"
        if(age >= 18):
            return "she is minor" 
        if(height > 5):
            return "height not match"
    else:
        return "she is not eligiable"
result = miss("dark",20,6)
##print(result)        
## write progrem to return multiple values using function 
def multiple(a,b):
    return a+b,a-b,a*b

add,sub,mul = multiple(10,12)
##print("addition:",add)
##print("substraction:",sub)
##print("mutliplication:",mul)

## write a program to print squre of number
def square(num):
    return num ** 2

result = square(5)
print(result)    
## to find muptiple number squre
