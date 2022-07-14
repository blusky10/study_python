N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)

result = 0;

n = M // K
m = M % K

result = data[0] * K * n
result += data[1] * m

print(result)

