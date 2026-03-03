##string slicing and joining
##string indexing 1
s="python"
print(s[0])  #p
print(s[-1]) #n

##string slicing 2
## syntax : string[start : end : step]
##example
s = "python"
print(s[0:4])    #pyth
print(s[2:])
print(s[:3])
print(s[ ::-1])  #for reverse


s = "pythonprogramminglanguage"
print(s[0:6])    
print(s[5:])
print(s[:6])
print(s[ ::-1])  #for reverse

## joining string(the join() method joins element of a list or tuple into astring)

words = ["python", "is", "easy"]
sentence = "".join(words)
print(sentence)

## formatting strings : used to insert variables into strings
#method 1..Usingformate()
 #name = "muskan"
  #age = 20
  #print("name:{} age:{}".formate(name,age))
# method 2..Using f-string(recommended)
 #print("f name:{name} age:{age}")
# method 3...Using % operator
 #print("name: %s age:  %d" (name,age) )

##         Lists(mutable collection python) : a list in python used to store multiple value in single element 

numbers = [10,20,30]

numbers.append(40) #add element
numbers.insert(1,15) # insert at index
numbers.remove(20) 
numbers.pop()   #remove last element
numbers.sort()   #sort list
numbers.reverse()

print(numbers)


##                             interview types question                              ##
# what is python?
# who developed python?
# what are the feactures of python ?
# Is python compiled or interpreted?
# what are keywords?
# what are identifier?
# what are the basic data types in python?
# what is type conversion?
# what is variable?
# what is the difference between = and ==?
# what  are operator in python?
# what is indentation in pyhton?
# what is loop?
# difference between for loop and while loop?
# what is break statement?  terminate the loop immediately
# what is continue statement?  skip the current iteration and moves to the next iteration
# what is pass statement?   does noting and is used as a placeholder
# what is string?   is a sequence of characters enclosed in single , double and triple quotes
# what is string slicing?   used to extract a part of a string using index position
# what is function?    block of reusable code that perform task
# what is input() function?   is used to take inputfrom the Usingformate
# what is print() function?  used to display output on the screen 
# what is list in python? is an ordered , mutable collection of element 
# difference between list and tuple? list is mutable and tuple is immutable

#                    commonly used method  in list function
# append()
# insert()
# remove()
# sort()   arrange element in ascending order
# reverse()

