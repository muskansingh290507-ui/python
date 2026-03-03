data = {}

n = int(input("enter number 0f elements:"))


for i in range(n):
    key = input(f"enter key {i+1}:")
    value = input(f"enter value {i+1}:")
    data[key] = value

print("\nDictionary Elements:")
for k,v in data.items():
    print(k, ":" ,v)
