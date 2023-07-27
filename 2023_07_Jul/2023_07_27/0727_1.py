class Person:
    gene = "XYZ"
    def __init__(self, name):
        self.name = name

    
    def greeting(self):
        return(f'Hola, {self.name}')
    

class Mum(Person):
    gene = 'XX'
    
    # def __init__(self, name): #권장사항임
    #     super().__init__(name) #권장사항임


    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'

#super의 특징은 찾는 순서를 자동으로 쓲싺 

class FirstChild(Mum, Dad):

    dad_gene = Person.gene

    def __init__(self, name):
        Dad.__init__(self,name)
        # dad의 것을 가져온 것, super()로는 불러올수없다. mum이 앞이라서. . .
        # super는 mro의 순서로 잘 찾아서 해줌.
        # 다만 명시적으로 하는게 틀린건 아님.

    def swim(self):
        return '첫째가 수영'
    
    def cry(self):
        return '첫째가 응애'
    
baby1 = FirstChild('아가')
print(baby1.cry()) # 첫째가 응애
print(baby1.swim()) # 첫째가 수영
print(baby1.walk()) # 아빠가 걷기
print(baby1.gene) # FirstChild의 상속 순서 (dad, mum) or (mum, dad) 에 따라 xy, xx 로 바뀜
print(baby1.dad_gene)
 
print(FirstChild.mro())
# [<class '__main__.FirstChild'>, <class '__main__.Mum'>, <class '__main__.Dad'>, <class '__main__.Person'>, <class 'object'>] 
# 이것이 탐색 순서임.
