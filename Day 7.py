# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
len(it_companies)  # Question 1
it_companies.add('Twitter')  # Question 2
it_companies.update(['TikTok', 'Zoom'])  # Question 3
it_companies.remove('Google')  # Question 4
#  Discard does nothing if the value is not present.Remove on the other hand presents an error if element is not present
A.update(B)  # Question 1
print(A)
A.intersection(B)  # Question 2
print(A)
C = A.issubset(B)  # Question 3
print(C)
C = A.isdisjoint(B)  # Question 4
print(C)
C = A.union(B)  # Question 5
print(C)
D = B.union(A)
print(D)
E = A.symmetric_difference(B)  # Question 6
print(E)
del A  # Question 7
del B
#Exercise 3
result = set(age)  # Question 1
print(result)
resultLength = len(result)  # Question 2
ageLength = len(age)
print(resultLength)
print(ageLength)
if resultLength > ageLength:
    print("The set is longer than the list")
elif resultLength < ageLength:
    print("The set is shorter than the list")
else:
    print("The set is the same length as the list")
sentence = "I am a teacher and I love to inspire and teach people"  # Question 3
splitSen = sentence.split()
conSen = set(splitSen)
uniSen = len(splitSen)
print(uniSen)
