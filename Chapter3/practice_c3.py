names = ['stephen','ross','tim','ive']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

print(names[-1])
print(names[-2])

print(f"{names[0].title()}, good morning!")
print(f"{names[1].title()}, good morning!")
print(f"{names[2].title()}, good morning!")
print(f"{names[3].title()}, good morning!")

ways = ['bicycle','motorcycle','car']
print(f"I would like to own a {ways[0]}")
print(f"I would like to own a {ways[1]}")
print(f"I would like to own a {ways[2]}")

names = ['stephen','ross','tim','ive']
print(f"{names[0]}, welcome!")
print(f"{names[1]}, welcome!")
print(f"{names[2]}, welcome!")
print(f"{names[3]}, welcome!")

print(names[2])
names[2] = 'Taylor'

print(f"{names[0]}, welcome!")
print(f"{names[1]}, welcome!")
print(f"{names[2]}, welcome!")
print(f"{names[3]}, welcome!")

print("There will have a bigger table for more people to enjoy dinner.")

names.insert(0,"TC")
names.insert(3,"Dame")
names.append('Elizabeth')
print(names)

print("Sorry, the table won't be delivered in time!")

poped_name = names.pop()
print(f"Sorry! {poped_name}")
poped_name = names.pop()
print(f"Sorry! {poped_name}")
poped_name = names.pop()
print(f"Sorry! {poped_name}")
poped_name = names.pop()
print(f"Sorry! {poped_name}")
poped_name = names.pop()
print(f"Sorry! {poped_name}")

print(f"{names[0]}, welcome!")
print(f"{names[1]}, welcome!")

del names[1]
del names[0]
print(names)

place = ['Hong Kong',"Singapore","Pairs","Iceland","Tokyo"]
print(place)

print(sorted(place))
print(place)

print(sorted(place,reverse=True))
print(place)

place.reverse()
print(place)

place.reverse()
place.sort()
print(place)

place.sort(reverse=True)
print(place)

print(len(names))

together = ['山川','河流','USA','Singapore','R','Finance']
print(sorted(together,reverse=True))
together.reverse()
print(together)
print(len(together))
