age = 28  # QUESTION 1
h = 5.11  # QUESTION 2
complex_number = 5 + 6j  # QUESTION 3
base = float(input("Enter base: "))  # QUESTION 4
height = float(input("Enter height: "))
area = 0.5 * base * height
print("The area of the triangle: ", area)
a = float(input("Enter side a: "))  # Question 5
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
print("The perimeter of the triangle: ", perimeter)
length = float(input("Enter length: "))  # Question 6
width = float(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print("The area of the rectangle: ", area)
print("The perimeter of the rectangle: ", perimeter)
pi = 3.14  # Question 7
r = float(input("Enter radius: "))
area = pi * r * r
circumference = 2 * pi * r
print("The area of the circle: ", area)
print("The circumference of the circle: ", circumference)
m = 2  # Question 8
b = -2
x_intercept = -b / m
print("Slope (m):", m)
print("Y-intercept (b):", b)
print("X-intercept:", x_intercept)
x1, y1 = 2, 2  # Question 9
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
# Calculate the Euclidean distance
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("Slope between the points:", slope)
print("Euclidean distance between the points:", distance)
if m == slope:  # Question 10
    print ("Both slopes are the same.")
else:
    print("The slopes are different.")
def calculate_y(x):  # Question 11
    y = x**2 + 6*x + 9
    return y
x_values = [-10, -5, 0, 1, 2, 3, 4, 5, 10]
for x in x_values:
    y = calculate_y(x)
    print("For x = {}, y = {}".format(x, y))
print("\nAt x = -3, y = 0")
python_length = len('python')  # Question 12
dragon_length = len('dragon')
print("The python length is: ", python_length)
print("The dragon length is: ", dragon_length)
false_comparison = dragon_length < python_length
print(false_comparison)
first_Word = 'python'  # Question 13
second_Word = 'dragon'
if 'on' in first_Word and 'on' in second_Word:
    print("'on' is present in both 'python' and 'dragon'")
else:
    print("'on' is not present in both 'python' and 'dragon'")
sentence = 'I hope this course is not full of jargon'  # Question 14
if 'jargon'in sentence:
    print("'jargon' is present in the sentence")
else:
    print("'jargon' is not present in the sentence")
first_Word = 'python'  # Question 15
second_Word = 'dragon'
if 'on'not in second_Word and 'on' not in first_Word:
    print('False')
text = len('python')  # Question 16
text_float = float(text)
text_string = str(text_float)
number = 8 # Question 17
if number % 2 == 0:
    print (number, "is even")
else:
    print(number, "is odd")
number = 7//3 # Question 18
if number == int(2.7):
    print (number,"is equal to the converted value")
else:
    print (number,"is not equal to the converted value")
if type('10')== type(10): # Question 19
    print ("The types are equal")
else:
    print ("The types are not equal")
number = int(9.8)
if number == 10: # Question 20
    print ("They are equal")
else:
    print ("They are not equal")
hours = float(input ("Enter hours: ")) # Question 21
rate = float(input ("Enter rate per hour : "))
weeky_earnings = hours * rate
print("The weekly earnings is : ", weeky_earnings)
years_lived = int(input("Enter number of years you have lived: "))  # Question 22
seconds_per_minute = 60
minutes_per_hour = 60
hours_per_day = 24
days_per_year = 365
years_max = 100
seconds_lived = years_lived * days_per_year * hours_per_day * minutes_per_hour * seconds_per_minute
print("You have lived for", seconds_lived, "seconds.")
