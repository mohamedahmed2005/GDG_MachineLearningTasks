x = input("Enter a Sentence: ")
x = x.lower()
lista = x.split()
print(len(lista))
lista = sorted(lista, key=len)
print(lista[-1])
counter = {}
for word in lista:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1
print(counter)