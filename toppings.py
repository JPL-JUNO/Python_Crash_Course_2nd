requested_topping = "mushrooms"
if requested_topping != "anchovies":
	print("Hold the anchovies")

age = 18
print(age==18)

age_0 = 22
age_1 = 18
print((age_0 >= 21) and (age_1 >= 21))

age_1 = 22
print((age_0 >= 21) and (age_1 >= 21))

print((age_0 >= 21) or (age_1 >= 21))

age_1 = 18
age_0 = 18
print((age_0 >= 21) and (age_1 >= 21))

requested_topping = ['mushrooms','onions','pineapple']
print('mushrooms' in requested_topping)
print('pepperoni' in requested_topping)

if 'mushrooms' in requested_topping:
	print("Adding mushrooms")
if 'pepperoni' in requested_topping:
	print("Adding pepperoni")
if 'extra cheese' in requested_topping:
	print("Adding extra cheese")

print('\nFinished making your pizza!')

if 'mushrooms' in requested_topping:
	print("Adding mushrooms")
elif 'pepperoni' in requested_topping:
	print("Adding pepperoni")
elif 'extra cheese' in requested_topping:
	print("Adding extra cheese")
print('\nFinished making your pizza!')

requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings :
 	print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")

for requested_topping in requested_toppings :
	if requested_topping == 'green peppers' :
		print("Sorry, we are out of green peppers right now.")
	else :
	 	print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")

requested_toppings = []

if requested_toppings :
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}")
	print("\nFinished making your pizza!")
else :
	print("Are you sure your want a plain pizza?")

available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']

requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings :
	if requested_topping in available_toppings :
		print(f"Adding {requested_topping}.")
	else :
		print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")