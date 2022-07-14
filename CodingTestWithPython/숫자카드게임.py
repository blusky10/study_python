N, M = map(int, input().split())

result = 10000

for _ in range(0,N):
    data = list(map(int, input().split()))
    data.sort
    result = min(result, data[0])

print(result)