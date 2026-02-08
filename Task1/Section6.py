#Task6.1
age = int(input("What is your age? "))
if 18 <= age <= 65:
    print("Eligible")
else:
    print("Not eligible")

#Task6.2
a = True
b = False
c = True
print(a and b)
print(a or b)
print(not a)
print((a and b) or c)
print(a and (b or c))