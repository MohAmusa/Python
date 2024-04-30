dog = {}  # Question 1
dog_Part = {'Name': 'PitBull', 'Colour': 'Black', 'Legs': 'Four', 'Age': 'Two'}  # Question 2
studentDictionary = {'first_name': 'Wale', 'last_name':'Edun', 'gender': 'Male', 'age': '22', 'marital_status': 'single', 'skills': 'Boxing', 'country': 'Nigeria', 'city': 'Lagos', 'address': '50 Allen Avenue'}  # Question 3
skillsValue = studentDictionary.get('skills')  # Question 4
typeSkills = type(skillsValue)   # Question 5
print(typeSkills)
studentDictionary['skills'] = 'swimming', 'cycling'  # Question 6
print(studentDictionary)
keyList = list(studentDictionary.keys())  # Question 7
print(keyList)
valueList = list(studentDictionary.values())  # Question 8
print(valueList)
tuple_list = list(studentDictionary.items())  # Question 9
print(tuple_list)
keys_to_delete = []  # Question 10
for key, value in studentDictionary.items():
    if value == '22':
        keys_to_delete.append(key)

for key in keys_to_delete:
    del studentDictionary[key]
print(studentDictionary)
del studentDictionary['gender']  # Question 11
