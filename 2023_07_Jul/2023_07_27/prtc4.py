# ws_8_1.py , 2 and 3

# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0
    def __init__(self):
        Animal.num_of_animal += 1 

class Dog(Animal):
    sound = '멍멍'

    def __init__(self):
        super().__init__()

    def bark(self):
        return print('멍멍!')


class Cat(Animal):
    sound = '야옹'
    def __init__(self):
        super().__init__()

    def meow(self):
        return print('야옹!')

class Pet(Dog, Cat):

    @classmethod
    def access_num_of_animal(cls):
        return f'동물의 수는 {cls.num_of_animal}마리 입니다'
    
    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.' #인스턴스
class Pet2(Cat, Dog):

    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.' #인스턴스

# dog = Dog()
# print(Pet.access_num_of_animal())
# cat = Cat()
# print(Pet.access_num_of_animal())

dog1 = Dog()
dog1.bark()

cat1 = Cat()
cat1.meow()

# pet1 = Pet("그르르")
# pet1.make_sound()
# pet1.bark()
# pet1.meow()
# pet1.play()
pet3 = Pet()
pet4 = Pet()
pet1 = Pet2()
pet2 = Pet2()
print(pet3)
print(pet1)