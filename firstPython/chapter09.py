class Dog:
    """개모델"""
    def __init__(self, name, age):
        """name, age 초기화"""
        self.name = name
        self.age = age

    def sit(self):
        """명령"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over")

class ElectCar(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
    

my_dog = Dog('kkk', 6)

my_dog.roll_over()
my_dog.name='ggg'
my_dog.roll_over()

my_EDog = ElectCar("eee", 7)
my_EDog.roll_over()