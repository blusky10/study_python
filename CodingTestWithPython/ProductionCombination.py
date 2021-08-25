from itertools import combinations_with_replacement, product

data = ['A', 'B', 'C']

# 2개 뽑는 순열(중복허용)
result = list(product(data, repeat=2))
print(result)

# 2개 뽑는 조합(중복허용)
result = list(combinations_with_replacement(data, 2))
print(result)


import math

# 최대 공약수
print(math.gcd(21,14))

def lcm(a,b):
    return a*b // math.gcd(a,b)

# 최소 공배수
print(lcm(21,14))