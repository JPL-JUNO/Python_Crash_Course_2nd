bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[0])
print(bicycles[1])
print(bicycles[0].title())
print(bicycles[1].title())

print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0]}."
print(message)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0,'ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
poped_motorcycles = motorcycles.pop()

print(motorcycles)
print(poped_motorcycles)

motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned}.")

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

