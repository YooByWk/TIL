class Dog:
    sound = '멍멍'

class Cat:    
    sound = '야옹'

class Pet(Cat, Dog ):

    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.' #인스턴스

pet3 = Pet()
pet4 = Pet()

print(pet3)
print(pet4)