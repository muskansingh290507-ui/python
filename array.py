fruits = ["apple","Mango","apple","apple","apple",]
fruits.append("banana")
fruitscopy = fruits.copy()
fruitscount = fruits.count("apple")
##fruitslength = len(fruits)
# ##print("copy of fruits",fruitscopy)
# print("count of fruits",fruitscount)
# print("length of fruits",fruitslength)
# ##example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
nums = [4,3,5,2,1]
target = 6
result = []
def add(nums,target):
   ## sare array ke index pe check karna hai ki 2 index mila ke target ke equal hote hai ki nhi
   ## ye kaam tb tk chalega jb tk total arr values check nh ho jye ya fir target 2 values ke equal nh ho jye
    i = 0
    while i< len(nums):
        j = i+1
        while j<1 len(nums):
            if(nums[i] + nums[j] == target):
                return [i,j]
            j = j+1
        i = i+1
    return []
result = add(nums,target)
print(result)    
                 
        
      

    
    
