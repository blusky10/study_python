# index가 필요 없는 반복문일 경우 _ 사용, 배열 초기화시 사용
array = [[0] * 3 for _ in range(10)]
print(array)

## 공백으로 input 값 받는 방법
data = list(map(int, input().split(",")))

print(data)

## for문
result = 0
for i in range(0,10) :
    result +=i
print(result)
