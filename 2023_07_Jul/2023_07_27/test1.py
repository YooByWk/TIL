class Persona:
    numbers = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Persona.numbers += 1 

    def __str__(self):
        return self.name
    
    @classmethod
    def getnumbers(cls):
        return cls.numbers

class Student(Persona):
    def __init__(self,name,age, number):
        super().__init__(name,age)
        self.number = number

    def __str__(self):
        return f'{self.number}_{self.name}'

class Prof(Persona):
    def __init__(self,name,age):
        super().__init__(name,age)


s1 =Student('김씨', 20, 45649835621)
s2 = Student('박씨', 25, 45612389749)
p1 = Prof('박씨', 99)
p2 = Prof('심씨', 55)
print(s1)
print(s1.name, s1.age)
print(s2.name, s2.age)
print(p1.name, p1.age)
print(p2.name, p2.age)
print(Persona.getnumbers())
print(Student.getnumbers())