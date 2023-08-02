p = int(input()) # 빌딩의 수
for piso in range(p): # 건물 리스트
    lista = list(map(int, input().split()))
print(lista)
diferencia = [0, 0]
for i in range(2,p-2):
    