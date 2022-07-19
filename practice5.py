car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("Is car == 'audi'? I predict True.")
print(car == 'audi')

A = 'stephen'
B = 'ross'
print(A == B) 

print(A.lower() == B)

#5-3
alien_color = 'red'
if alien_color == 'green':
	print("Alien_color is green.")
	print("You got 5 points!")

alien_color = 'green'
if alien_color == 'green':
	print("Alien_color is green.")
	print("You got 5 points!")

#5-4

alien_color = 'red'

if alien_color == 'green':
	print("You got 5 points because you shot!")
else :
	print("You got 10 points!")

alien_color = 'green'

if alien_color == 'green':
	print("You got 5 points because you shot!")
else :
	print("You got 10 points!")

#5-5
alien_color = 'red'

if alien_color == 'green':
	print("You got 5 points!")
elif alien_color == 'yellow':
	print("You got 10 points!")
else :
	print("You got 15 points!")

alien_color = 'green'

if alien_color == 'green':
	print("You got 5 points!")
elif alien_color == 'yellow':
	print("You got 10 points!")
else :
	print("You got 15 points!")

alien_color = 'yellow'

if alien_color == 'green':
	print("You got 5 points!")
elif alien_color == 'yellow':
	print("You got 10 points!")
else :
	print("You got 15 points!")

#5-6
age = 23
if age < 2 :
	print("这个人是婴儿。")
elif age < 4 :
	print("这个人是幼儿。")
elif age < 13 :
	print("这个人是儿童。")
elif age < 20 :
	print("这个人是青少年。")
elif age < 65 :
	print("这个人是成年人。")
else :
	print("这个人是老年人。")

favorite_food = ['apple','banana','orange']
if 'banana' in favorite_food :
	print("You really like banana.")
if 'apple' in favorite_food :
	print("You really like apple.")
if 'pineapple' in favorite_food :
	print("You really like pineapple.")
if 'orange' in favorite_food :
	print("You really like orange.")
if 'strawberry' in favorite_food :
	print("You really like strawberry.")

#5-8
users = ['stephen','ross','tc','admin','jaden']

for user in users :
	if user == 'admin' :
		print(f"Hello {user}, would you leike to see a status report?")
	else :
		print(f"Hello {user.title()}, thank you for logging in again.") 

#5-9
if users :
	del users
else :
	print("We need to find some users!")

#5-10

current_users = ['stephen','ross','tc','joker','jaden','queen']

new_users = ['queen','marry','jaden','tim','John']
for user in current_users :
	current_users_lowers = user.title()

for user in new_users :
	if user.title() in current_users_lowers :
		print("Sorry, please sign up with other name!")
	else :
		print(f"Ok, you can sign up with {user}") 

#5-11
numbers = list(range(1,11))
for number in numbers :
	if number == 1 :
		print(f"{number}st")
	elif number == 2 :
		print(f"{number}nd")
	elif number == 3 :
		print(f"{number}rd")
	else :
		print(f"{number}th")

#5-12

#5-13