M, N = map(int,input().split())
a = set()
b = set()
for _ in range(M):
    k = input()
    a.add(k)
# print(a)
for _ in range(N):
    p = input()
    b.add(p)
    
# print(a&b)
asd = len(a&b)
print(asd)
ans = sorted(list(a&b))
for i in ans:
    print(i)