user = int(input("Enter your age: "))  # Question 1
drivingAge = 18
yearsLeft = drivingAge - user
if user >= drivingAge:
    print("You are old enough to drive!")
else:
    print("You have", yearsLeft, "years left to learn to drive")
user = int(input("Enter your age: "))  # Question 2
myAge = 30
if user > myAge:
    ourDiff = user - myAge
    if ourDiff == 1:
        print("You are older than me with", ourDiff, "year")
    else:
        print("You are older than me with", ourDiff, "years")
elif myAge > user:
    ourDiff = myAge - user
    if ourDiff == 1:
        print("You are younger than me with", ourDiff, "year")
    else:
        print("You are younger than me with", ourDiff, "years")
else:
    print("You are the same age with me")
numOne = int(input("Enter number one: "))  # Question 3
numTwo = int(input("Enter number two: "))
if numOne > numTwo:
    print(numOne, "is greater than", numTwo)
elif numOne < numTwo:
    print(numOne, "is lesser than", numTwo)
else:
    print(numOne, "is equal to", numTwo)
# Exercise 2
scores = int(input("Enter Student Score: "))
if scores <= 49:
    print("Your Grade is F")
elif scores <= 59:
        print("Your Grade is D")
elif scores <= 69:
        print("Your Grade is C")
elif scores <= 79:
        print("Your Grade is B")
elif scores <= 100:
        print("Your Grade is B")
else:
    print("Invalid Score")
# Question 2
season = input("Enter month: ").capitalize()
Autumn = {"September", "October", "November"}
Winter = {"December", "January", "February"}
Spring = {"March", "April", "May"}
Summer = {"June", "July", "August"}
if season in Autumn:
    print("The season is Autumn")
elif season in Winter:
    print("The season is Winter")
elif season in Spring:
    print("The season is Spring")
elif season in Summer:
    print("The season is Summer")
else:
    print("Invalid Month")
# Question 3
new_fruit = input("Enter fruit: ").lower()
fruits = ['banana', 'orange', 'mango', 'lemon']
if new_fruit not in fruits:
    fruits.append(new_fruit)
    print("The new fruit is", new_fruit)
    print("The new list is: ", fruits)
else:
    print("The fruit is already part of the list")

# Question 4.
if 'skills' in person:
    skills = person['skills']
    if len(skills) % 2 == 1:
        middle_skill = skills[len(skills) // 2]
        print("Middle skill:", middle_skill)
    else:
        print("The person has an even number of skills.")

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    if 'Python' in person['skills']:
        print("The person has Python skill.")
    else:
        print("The person does not have Python skill.")

# Determine the person's title based on their skills.
if 'skills' in person:
    skills = person['skills']
    if set(skills) == {'JavaScript', 'React'}:
        print("He is a front end developer")
    elif {'Node', 'Python', 'MongoDB'}.issubset(set(skills)):
        print("He is a backend developer")
    elif {'React', 'Node', 'MongoDB'}.issubset(set(skills)):
        print("He is a fullstack developer")
    else:
        print("Unknown title")

# If the person is married and lives in Finland, print the information.
if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']} and is married.")
