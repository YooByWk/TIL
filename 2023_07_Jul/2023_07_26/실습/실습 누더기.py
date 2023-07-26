# 1, 2, 3 4, 5 
# 5 최종결과

# 아래 클래스를 수정하시오.

class Shape:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return(self.width * self.height)

    def calculate_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def print_info(self):
        self.area = self.calculate_area()
        self.peri = self.calculate_perimeter()
        return print(f'Width : {self.width}\nHeight : {self.height}\nArea : {self.area}\nPerimeter : {self.peri}')

    def __str__(self):
        return f'Shape: width={self.width}, height={self.height}'


shape1 = Shape(5, 3)
print(shape1)


