pizzas = ['pizzaA','pizzaB','pizzaC']
for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print(f"I like {pizza}.")

for pizza in pizzas:
    print(f"I like {pizza}.")
print("I really love pizza!")

pets = ['dog','cat','pig']
for pet in pets:
    print(pet)

for pet in pets:
    print(f"A {pet} would make a great pet.")

for pet in pets:
    print(f"A {pet} would make a great pet.")

print("Any of these animals would make a great pet!")

for i in range(1,21):
    print(i)

#for i in range(1,1000001):
#    print(i)

millions =list(range(1,1000001))
print(min(millions))
print(max(millions))
print(sum(millions))

odd_numbers = list(range(1,21,2))
for numbers in odd_numbers:
    print(numbers)

cubes = list(range(1,11))
for numbers in cubes:
    print(numbers**3)

print([numbers**3 for numbers in range(1,11)])

pizzas.append("pizzaD")
pizzas.append("pizzaE")
pizzas.append("pizzaF")
 
print("The first three items in the list are:")
for pizza in pizzas[:3]:
    print(pizza)

print("Three items from the middle of the list are:")
for pizza in pizzas[2:5]:
    print(pizza)

print("The last three items in the list are:")
for pizza in pizzas[-3:]:
    print(pizza)

friend_pizza = pizzas[:]
pizzas.append("PizzaG")
friend_pizza.append("PizzaH")

print("My favorite pizza are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizza are:")
for pizza in friend_pizza:
    print(pizza)

foods = ("apple","orange","peach","tomato","potato")
for food in foods:
    print(food)

fruits = ("apple","orange","peach","banana","pineapple")
for fruit in fruits:
    print(fruit)