def add_two_numbers():
    numOne = 2
    numTwo = 3
    totalNumber = numOne + numTwo
    return totalNumber
print(add_two_numbers())
# Question 2
def area_of_circle (r):
    PI = 3.14
    totalArea = PI * r * 2
    return totalArea
print(area_of_circle(10))
# Question 3
def add_all_nums (*nums):
    total = 0
    for num in nums:
        if not isinstance(num, (int, float) ):
           return f"Error! The input '{num}' is not a number"
        total += num
    return total
print(add_all_nums(3, 4, 5))
# Question 4
def convert_celsius_to_fahrenheit (c):
    f = (c * 9 / 5 + 32)
    return f
print(convert_celsius_to_fahrenheit(30))
# Question 5
def check_season (month):
    month = month.capitalize()
    if month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['September', 'October', 'November']:
        return 'Autumn'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    else:
        return 'Invalid Input'

print(check_season())
# Question 6
def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        return "The line is vertical, slope is undefined."
    else:
        slope = (y2 - y1) / (x2 - x1)
        return slope
print(calculate_slope(1, 2, 3, 4))
# Question 7
import math

def solve_quadratic_eqn(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        if discriminant == 0:
            return (root1,)
        else:
            return (root1, root2)

print(solve_quadratic_eqn(1, -3, 2))

# Question 8
def print_list(lst):
    for element in lst:
        print(element)
example_list = [1, 1, 2, 3]
print_list(example_list)
print(print_list)
# Question 9
def reverse_list (list):
    reverse_arr =[]
    for element in range(len(list)-1, -1, -1):
        reverse_arr.append(list[element])
    return reverse_arr
the_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(the_list)
the_list1 = ["A", "B", "C"]
reversed_list1 = reverse_list(the_list1)
print(reversed_list)
print(reversed_list1)
# Question 10
def capitalize_list_items (list):
    listed_fruits = []
    for element in list:
        listed_fruits.append(element.capitalize())
    return listed_fruits
fruits = ['mangoes', 'bananas', 'apples', 'oranges']
capitalize_fruits = capitalize_list_items(fruits)
print(capitalize_fruits)
# Question 11
def add_item (list, list1):
    return list + [list1]
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))
numbers = [2, 3, 7, 9]
print(add_item(numbers, '5'))
# Question 12
def add_item (list, list1):
    new_list = list.copy()
    if list1 in new_list:
       new_list.remove(list1)
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Milk'))
numbers = [2, 3, 7, 9]
print(add_item(numbers, '3'))
# Question 13
def sum_of_numbers (num):
    return sum(range(1, num + 1))
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

# Question 14
def add_num (num):
    total = 0
    for num1 in range (1, num + 1):
        if num1 % 2 != 0:
           total += num1
    return total
print(add_num(5))
print(add_num(10))
print(add_num(100))
# Question 15
def add_num (num):
    total = 0
    for num1 in range(1, num + 1):
        if num1 % 2 == 0:
            total += num1
    return total
print(add_num(5))
print(add_num(10))
print(add_num(100))

# Exercise 2
# Question 1
def evens_and_odds (n):
    evens = 0
    odds = 0
    for num in range(n + 1):
        if num % 2 == 0:
            evens += 1
        else:
            odds += 1
    return evens, odds
evens, odds = evens_and_odds(100)
print(evens)
print(odds)
# Question 2
def factorial (n):
    if n == 0:
        return 1
        result = 1
    for num in range(1, n + 1):
        result *= num
        return result

print(factorial(5))
# Exercise 3
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
print(is_prime(2))

# Question 2
def all_unique(items):
    return len(items) == len(set(items))

print(all_unique([1, 2, 3, 4, 5]))
# Question 3
def all_same_type(items):
    if not items:
        return True

    first_type = type(items[0])
    for item in items:
        if type(item) != first_type:
            return False

    return True
print(all_same_type([1, 2, 3, 4, 5]))
# Question 4
def all_same_type(items):
    if not items:
        return True

    first_type = type(items[0])
    for item in items:
        if type(item) != first_type:
            return False

    return True
print(all_same_type([1, 2, 3, 4, 5]))