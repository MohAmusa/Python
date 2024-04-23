dayFive = myList()  # Question 1
cars = ['Toyota', 'Mazda', 'Honda', 'BMW', 'Volkswagen']  # Question 2
print(len(cars))   # Question 3
cars = ['Toyota', 'Mazda', 'Honda', 'BMW', 'Volkswagen']  # Question 4
firstItem = cars[0]
middleItem = cars[2]
lastItem = cars[4]
print(firstItem, middleItem, lastItem)
mixed_data_types = ['Mohammed', '28', '5.10', 'Single', 'Ibadan']  # Question 5
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'] # Question 6
print(it_companies)  # Question 7
print(len(it_companies))  # Question 8
firstCompany = it_companies[0]  # Question 9
middleCompany = it_companies[2]
lastCompany = it_companies[4]
print(firstCompany, middleCompany, lastCompany)
it_companies[0] = 'Meta'  # Question 10
print(it_companies)
it_companies.append('Meta')  # Question 11
print(it_companies)
it_companies.insert(4, 'Meta')  # Question 12
print(it_companies)
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']  # Question 13
it_companies[1] = it_companies[1].upper()
print(it_companies)
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']  # Question 14
joinCompanies = '#' + '#'.join(it_companies)
print(joinCompanies)
checkCompanies = 'Google' in it_companies  # Question 15
print(checkCompanies)
it_companies.sort()  # Question 16
print(it_companies)
it_companies.reverse()  # Question 17
sliceCompanies = it_companies[3:7]  # Question 18
print(sliceCompanies)
sliceCompanies = it_companies[:4]  # Question 19
print(sliceCompanies)
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']  # Question 20
sliceCompanies = len(it_companies) // 2
resultCompanies = it_companies[sliceCompanies]
print(resultCompanies)
del it_companies[0]  # Question 21
print(popCompanies)
del it_companies[3]  # Question 22
print(it_companies)
del it_companies[7]  # Question 23
print(it_companies)
del it_companies[0:7]  # Question 24
print(it_companies)
it_companies.clear()  # Question 25
print(it_companies)
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']  # Question 26
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print('Languages:', front_end)
full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']  # Question 27
full_stack = full_stack[:5] +['Python', 'SQL'] + full_stack[5:]
print(full_stack)
#Exercise 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]  # Question 1
sortAges = sorted(ages)
minAge = sortAges[0]
maxAge = sortAges[9]
print(minAge)
print(maxAge)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]  # Question 2
sorted_ages = sorted(ages)
num_ages = len(sorted_ages)
middle_index = num_ages // 2
if num_ages % 2 == 1:
    median_age = sorted_ages[middle_index]
else:
    median_age = (sorted_ages[middle_index - 1] + sorted_ages[middle_index]) / 2
print("Median age:", median_age)
total_age = sum(ages) # Question 3
num_ages = len(ages)
average_age = total_age / num_ages
print("Average age:", average_age)
max_age = max(ages)  # Question 4
min_age = min(ages)
age_range = max_age - min_age
print("Range of ages:", age_range)
min_average_diff = abs(min_age - average_age)  # Question 5
max_average_diff = abs(max_age - average_age)
if min_average_diff > max_average_diff:
    print("Absolute difference between min and average is greater.")
elif min_average_diff < max_average_diff:
    print("Absolute difference between max and average is greater.")
else:
    print("Absolute differences between min and average, and max and average are equal.")

print("Absolute difference between min and average:", min_average_diff)
print("Absolute difference between max and average:", max_average_diff)
countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia',
    'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria',
    'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad',
    'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire",
    'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic',
    'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia',
    'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece',
    'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India',
    'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya',
    'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho',
    'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia',
    'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova',
    'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands',
    'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama',
    'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia',
    'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe',
    'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia',
    'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname',
    'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga',
    'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine',
    'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City',
    'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe',
]


num_countries = len(countries)
middle_index = num_countries // 2
if num_countries % 2 == 0:
    middle_countries = [countries[middle_index - - 1], countries[middle_index]]
else:
    middle_countries = [countries[middle_index]]
    print("Middle country(ies):", middle_countries)

num_countries = len(countries)
split_index = num_countries // 2

if num_countries % 2 == 0:
    first_half = countries[:split_index]
    second_half = countries[split_index:]
else:
    first_half = countries[:split_index + 1]
    second_half = countries[split_index + 1:]
print("First half:", first_half)
print("Second half:", second_half)
first_country, second_country, third_country, *other_countries = countries  # Last Question

print("First country:", first_country)
print("Second country:", second_country)
print("Third country:", third_country)
print("Other countries:", other_countries)
