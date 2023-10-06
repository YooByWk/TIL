import matplotlib.pyplot as plt


## 참고 xyz 같을 때
plt.plot([1,2,3,4])
# plt.show()

# 참고 : 이때까지 그렸던 plot 지우기
plt.clf() 
#  중요합니다.


# 예제 2 : x,y 가 다를 때
x = [1, 2, 3, 4]
y = [2, 4, 8, 16]
plt.plot(x,y)
# plt.show()
# 어지간하면 x축을 통일하시오.
y = [2, 345, 12, 24]
plt.plot(x,y)
# plt.show()

# 예제 3 : 제목 + 각 축의 설명
plt.plot(x, y)
plt.title("Test Graph")

# x , y 축
plt.ylabel('y label')
plt.xlabel('x label')

# plt.show()
# 한글은 깨집니다.
# 구글링 해보세요.

# 자 가보자 드장고
 

 # 사진을 창이 아닌, 파일로 저장받기
plt.savefig('filename.png')
 # show를 지워야 함.
 # 안그러면 흰색나옴