# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
#
# while 'cat' in pets:
#     pets.remove('cat')
#
# print(pets)

# 8.2
def describe_pet(animal_type, pet_name):
    """
    显示宠物信息
    :param animal_type: 宠物类型
    :param pet_name: 宠物名称
    :return: 宠物类型以及宠物名称
    """
    print(f'\nI have a {animal_type}.')
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

describe_pet(animal_type='dog', pet_name='willie')
describe_pet(pet_name='willie', animal_type='dog')
