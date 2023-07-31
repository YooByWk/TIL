T = int(input())

for test_case in range(1, T + 1):
    punto = int(input())
    lista = list(map(int, input().split()))
    val = max(lista) - min(lista)
    print(f'#{test_case} {val}')