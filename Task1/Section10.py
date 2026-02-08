#Task10.1
student = {
    'Name': 'Mohamed',
    'Age': 20,
    'Major': 'nothing',
    'GPA':3.85
}
print(student)
print(student['Name'])
student['GPA'] = 3.75
print(student)
student['Year'] = 2026
print(student.keys())
print(student.values())

#Task10.2
# Creating a nested dictionary (phone book)
phone_book = {
        "Arwa": "123-456-7890",
        "Ahmed": "987-654-3210",
        "Mohamed": "123456789",
        "Sama": "987654321"
}
phone_book['Mostafa'] = '1234567890'
print(phone_book)
phone_book.pop('Mohamed')
print(phone_book)
print(phone_book.get('Somaya'))
print(phone_book)
#Task10.3
company = {
    "IT": {"Names": ['mohamed' , 'Mostafa' , 'Toffi'], "Ages": [20,21,22]},
    "HR": {"Names": ['Habeba' , 'Fatma'], "Ages": [18,26]},
    "Sales": {"Names": ['Sama' , 'Khalaf'], "Ages": [20,26]}
}
print(company['IT']['Names'])
print(company['HR']['Ages'][1])
print(company['Sales'])