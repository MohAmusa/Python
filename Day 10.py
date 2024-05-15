count = 0
while count < 11:
    print(count)
    count += 1
# Question 2
count = 10
while count >= 0:
    print(count)
    count -= 1
# Question 3
for first in range(1, 8):
    for second in range(first):
        print("#", end="")
    print()
# Question 4
for first in range(8):
    for second in range(8):
        print("#", end="")
    print()
# Question 5
for i in range(11):
    result = i * i
    print(f"{i} x {i} = {result}")
# Question 6
promList = ['Python', 'Numpy','Pandas','Django', 'Flask']
for a in promList:
    print(a)
# Question 7
for a in range(0, 101, 2):
    print(a)
# Question 8
for a in range(1, 101, 2):
    print(a)
# Exercise 2
firstNumber = 0
for a in range(1, 101):
    firstNumber += a
    print(firstNumber)
# Question 2
countriesLand = []
for country in countries:
    if 'land' in countries.lower():
        countriesLand.append(countries)
print(countriesLand)
# Exercise 3
fruitList = ['banana', 'orange', 'mango', 'lemon']
secondList = []
for fruit in range(len(fruitlist) -1, -1, -1):
    secondList.apppend(fruitList[fruit])
print(secondList)
#  Question 3(1)
totalLanguages = 0
for country in data:
    if 'languages' in country:
        totalLanguages += len(country['languages'])
print(totalLanguages)
# 3(2)
language_count = {}

# Count the occurrences of each language
for country in data:
    for language in country["languages"]:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

# Find the most spoken language
max_count = 0
most_spoken_language = ""

for language, count in language_count.items():
    if count > max_count:
        max_count = count
        most_spoken_language = language

print("The most spoken language is:", most_spoken_language)
# 3(3)
country_population = []

# Iterate through each country to extract its name and population
for country in data:
    country_population.append((country['name'], country['population']))

# Sort the list of tuples based on population in descending order
country_population.sort(key=lambda x: x[1], reverse=True)

# Select the top 10 most populated countries
top_10_countries = country_population[:10]

# Print the names and populations of the top 10 most populated countries
print("Top 10 most populated countries:")
for country, population in top_10_countries:
    print(country, ":", population)