#4.4.3
my_foods = ['pizza','falafel','carrot cake']
friedns_foos = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy_friend's favorite foods are:")
print(friedns_foos)

my_foods.append("cannoli")
friedns_foos.append("ice cream")
print("My favorite foods are:")
print(my_foods)

print("\nMy_friend's favorite foods are:")
print(friedns_foos)

friedns_foos = my_foods

my_foods.append("cannoli")
friedns_foos.append("ice cream")

print("My favorite foods are:")
print(my_foods)

print("\nMy_friend's favorite foods are:")
print(friedns_foos)

for food in my_foods:
	print(food)

for food in friedns_foos:
	print(food)