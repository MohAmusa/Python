newTuple = ()  # Question 1
Brothers = ('Bayo', 'Tade', 'Karim', 'Joseph')  # Question 2
Sisters = ('Sade', 'Angela', 'Laide')
Siblings = Brothers + Sisters  # Question 3
find_index = len(Siblings)  # Question 4
print(find_index)
Parents = ('Kayode', 'Asake')  # Question 5
family_members = Siblings + Parents
print(family_members)
# Exercise 2
Siblings = ('Bayo', 'Tade', 'Karim', 'Joseph','Sade', 'Angela', 'Laide' )  # Question 1
fruits = ('Banana', 'Apples', 'Oranges', 'Mangoes')  # Question 2
vegetables = ('Okras', 'Maize', 'Tomatoes')
animalProducts = ('Milk', 'Meat', 'Eggs')
food_stuff_tp = fruits + vegetables + animalProducts
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)  # Question 3
print(food_stuff_tp)
food_stuff_iy = food_stuff_tp[:4] + food_stuff_tp[6:]  # Question 4
print(food_stuff_iy)
food_stuff_ey = food_stuff_tp[3:6] + food_stuff_tp[6:7]  # Question 5
print(food_stuff_ey)
del food_stuff_tp  # Question 6
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')  # Question 7
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)