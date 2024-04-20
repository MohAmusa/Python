word = ['Thirty', 'Days' 'of' 'Python']  # Question 1
result = ' '.join(word)
print(result)
connect = ['Coding', 'for', 'of', 'all']  # Question 2
result_One = ' '.join(connect)
print(result)
company = 'Coding for all'  # Question 3
print(company)  # Question 4
company_length = 'Coding for all'  # Question 5
print(len(company_length))
company = 'Coding for all'  # Question 6
company_upper = company.upper()
print(company_upper)
company = 'Coding for all'  # Question 7
company_lower = company.lower()
print(company_lower)
company = 'Coding for all'  # Question 8
company_capitalize = company.capitalize()
company_title = company.title()
company_sc = company.swapcase()
print(company_capitalize)
print(company_title)
print(company_sc)
string_title = 'Coding for all'  # Question 9
first_string = string_title.index(" ")
cut_string = string_title[first_string+1:]
print(cut_string)
string_title = 'Coding for all'  # Question 10
print(string_title.find('Coding'))
string_title = 'Coding for all'  # Question 11
print(string_title.replace('Coding', 'Python'))
string_title = 'Python for everyone'  # Question 12
print(string_title.replace('Python for everyone', 'Python for all'))
company = 'Coding for all'  # Question 13
print(company.split())
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"  # Question 14
print(tech_companies.split(','))
string_title = 'Coding for all'  # Question 15
string_letter = string_title[0]
print(string_letter)
string_title = 'Coding for all'  # Question 16
last_index = len(string_title)-1
print(last_index)
string_title = "Coding for all"  # Question 17
string_letter = string_title[10]
def fxn(sentence):  # Question 18
    acronym = sentence.split()
    output = ''
    for word in acronym:
        output += word[0]
    output = output.upper()
    return output
string = 'Python for Everyone'
print(fxn(string))
def fxn(tense):  # Question 19
    acronym = tense.split()
    output = ''
    for word in acronym:
        output += word[0]
    output = output.upper()
    return output
string = 'Coding For All'
print(fxn(string))
challenge = 'Coding For All'# Question 20
print(challenge.find('C'))
challenge = 'Coding For ALL'# Question 21
print(challenge.find('F'))
challenge = 'Coding For All People'# Question 22
print(challenge.rfind('I'))
sentence = 'You cannot end a sentence with because because because is a conjunction' # Question 23
print(challenge.find('because'))
sentence = 'You cannot end a sentence with because because because is a conjunction' # Question 24
print(challenge.rfind('because'))
sentence = 'You cannot end a sentence with because because because is a conjunction' # Question 25
startSen = sentence.find('because because because')
endSen = startSen + len('because because because')
spliceSen = sentence[:startSen] + sentence[endSen:]
print(spliceSen)
sentence = 'You cannot end a sentence with because because because is a conjunction' # Question 26 is same with 23. Take a look
position = sentence.find('because')
print(position)
sentence = 'You cannot end a sentence with because because because is a conjunction' # Question 27 is the same with 25
startSen = sentence.find('because because because')
endSen = startSen + len('because because because')
spliceSen = sentence[:startSen] + sentence[endSen:]
print(spliceSen)
sentence = 'Coding For All'   # Question 28
checkSen = sentence.startswith('Coding')
print(checkSen)
sentence = 'Coding For All'   # Question 29
checkSen = sentence.endswith('coding')
print(checkSen)
string = '   Coding For All      '
trimmed_string = string.strip()  # Question 30
print(trimmed_string)
challenge = '30DaysOfPython' # Question 31
print(challenge.isidentifier())
secCha = 'thirty_days_of_python'
print(secCha.isidentifier())
pythonLib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']  # Question 32
hashJoin = '# '.join(pythonLib)
print(hashJoin)
sentence = 'I am enjoying this challenge.\nI just wonder what is next.' #Question 33
print(sentence)
sentence = 'Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki' #Question 34
print(sentence)
radius =  10  #Question 35
area = 3.14 * radius ** 2
result = 'The area of a circle with radius {} is {} square meters.' .format(str(radius), str(area))
print(result)
addition = 8 + 6  #Question 36
substraction = 8 - 6
multiplication = 8 * 6
division = 8 / 6
modulus = 8 % 6
floor_division = 8 // 6
exponetiation = 8 ** 6
print('8 + 6 = {}'.format(addition))
print('8 - 6 = {}'.format(substraction))
print('8 * 6 = {}'.format(multiplication))
print('8 / 6 = {:.2f}'.format(division))
print('8 % 6 = {}'.format(modulus))
print('8 // 6 = {.2f}'.format(floor_division))
print('8 ** 6 = {}'.format(exponetiation))