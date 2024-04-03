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