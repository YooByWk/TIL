# 클래스 정의
class Person:  #파스칼케이스
    #속성(변수)
    blood_colour = 'red'
#     클래스 변수 
#  - 클래스 내부에 선언된 변수
#  - 클래스로 생성된 모든 인스턴스들이 공유하는 변수
    count = 0
    #메서드
#     생성자 함수
#  - 객체를 생성할 때 자동으로 호출되는 특별한 메서드
#  - __init__ 이라는 이름의 메서드로 정의되며, 객체의 초기화를 담당
#  - 생성자 함수를 통해 인스턴스를 생성하고 필요한 초기값을 설정
    def __init__(self, name): #생성자 매서드 # 개발자가 직접 호출하지 않음 (기능상 자연스럽게 동작)
           # 인스턴스 변수
        self.name = name  # 인스턴스 생성때 실행됨 / #2위치인자라 꼭 넣어줘야함 name
    # - 인스턴스(객체)마다 별도유지
    # - 인스턴스 마다 독립적 값 ,생성될 때마다 초기화
        Person.count += 1 
        
    @classmethod
    def number_of_population(cls):
        print(f'암튼 {cls.count}입니다.')


    def cantar(self):
        return f'{self.name} canta' #self는 걍 안보인다고 생각합시다.
    
# 인스턴스 생성
cantante1 = Person('bmth') #2에 이어짐 Ln7
cantante2 = Person('DY')

# 메서드 호출 
print(cantante1.cantar()) # bmth canta
print(cantante2.cantar()) # DY canta.

#속성(변수) 사용
print(cantante1.blood_colour) # red
print(cantante2.blood_colour) # red

Person.number_of_population()

'''

'''
class Circle():
    pi = 3.14
    def __init__(self, r):
        self.r = r 

c1 = Circle(5)
c2 = Circle(10)

Circle.pi = 5 # 클래스 변수 변경.
c2.pi = 5 # 인스턴스 변수 변경.

