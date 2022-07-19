class Dog:
    """
    一次模拟小狗的简单尝试
    """
    def __init__(self, name, age):
        """
        初始化属性
        :param name: 姓名
        :param age: 年龄
        :return:
        """
        self.name = name
        self.age = age

    def sit(self):
        """
        模拟小狗收到命令时蹲下
        :return:
        """
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """
        模拟小狗收到命令时打滚
        :return:
        """
        print(f'{self.name} rolled over!')


my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

your_dog = Dog('Lucy', 3)
print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
my_dog.roll_over()
