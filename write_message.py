filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('I love data analysis.\n')
    file_object.write('I love programming.\n')

with open(filename, 'a') as file_object:
    file_object.write('I also love finding meangin in large datasets.\n')
    file_object.write('I love creating apps that can run in a browser.')

