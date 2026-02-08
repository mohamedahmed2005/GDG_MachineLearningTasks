#Task7.1
x = ["banana","apple","mango" , "pineapple" , "Watermelon"]
print(x)
print(x[0])
print(x[len(x)-1])
x.append("grapes")
print(x)
x.pop(1)
print(x)
#Task7.2
numbers = [10, 20, 30, 40, 50]
print(len(numbers))
print(sum(numbers))
print(max(numbers))
print(min(numbers))
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
#Task7.3
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(letters[0:3])
print(letters[-3:])
print(letters[2:6])
print(letters[::2])
print(letters[::-1])