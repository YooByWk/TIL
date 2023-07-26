class Estudiante:
    hoja = []

    def __init__(self, nombre, edad): # self는 불문율
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return(self.nombre + ' ' + str(self.edad))
    
    def __lt__(self, other): #other은 비교를 위해 필요하다.
        return(self.edad < other.edad)
    
    def __len__(self):
        return self.edad

    def asistir(self, fecha):
        print(f'{self.nombre} ha asistido en {fecha}')
        Estudiante.hoja.append((self.nombre, fecha))

    @classmethod
    def obthoja(cls): # 암튼 본인 받음
        return cls.hoja #Estudiante 넣어도 되긴 하는데 . . .
    



s1 = Estudiante('Kim', 25) 
s2 = Estudiante('Lee', 124)
print(s1.nombre, s2.nombre)
s1.asistir("2023_07_26")
s2.asistir("2023_07_26")
print(Estudiante.hoja)
print(Estudiante.obthoja())

print(s1)
print(s1 < s2)

print(len(s1))
# s1  = Estudiante()  # 얘가 __init__을 호출해줬음 . . .

# s1.name = "김씨"
# print(s1.name) # 문법적으로는 허용하나 class의 개념에서는 좋지 않음
# # s1 할당 > s1.name 할당 순 

# Estudiante.name = '클래스이름'
# print(s1.name)
# print(Estudiante.name)
# # 제발 이러지 마세요. 
