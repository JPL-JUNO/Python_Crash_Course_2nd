with open('pi_digits.txt') as file_object:
    contents = file_object.read()
# 读取完之后有个空行
print(contents)
print(contents.rstrip())
print('a')

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())


with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
