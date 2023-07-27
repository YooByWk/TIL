class Person: #여기 바뀌면 아래도 변경해야해서 유연함이 좀 떨어짐.
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def talk(self):
        print(f'Hola, {self.name}')
    

# # 그냥 상속받기
# class Professor(Person):
#     def __init__(self, name, age, department):
#         self.name = name
#         self.age = age
#         self.department = department

# 뭐 두개가 거의 같다 입니다. 

class Student(Person):
    def __init__(self, name, age, gpa):
        # Person.__init__(self, name, age) #얘는 부모 클래스가 많아질수록 유연성이 떨어진다.
        super().__init__(name, age)  #일단 단일 상속이라서  결과는 부모 클래스인 Person임, Person의 __init__을 가져옴 #self도 숙청
        #super()는 부모 클래스의 메서드를 호출하기 위해 사용되는 내장 함수.
        self.gpa = gpa

#
class Professor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department


p1 = Professor('박교수', 49, '컴공')
s1 = Student('김학생', 20, 4.5)

p1.talk()
s1.talk()