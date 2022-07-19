responses = {}
polling_active = True

while polling_active:
    name = input('\nWhat is your name? ')
    response = input('Which mountain woild you like to climb sonmeday? ')

    responses[name] = response

    repeat = input('Would you like to let another people respand? [Yes/No]: ')
    if repeat == 'No':
        polling_active = False

print('\n-----Poll Results-----')
for name, response in responses.items():
    print(f'{name} would like to climb {response}')
