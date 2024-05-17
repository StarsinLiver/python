# ** 중요 복사 **

# ** 얕은 복사
a = [1,2]
b = a

# 같은 주소값을 가짐
print(id(a)) # 2069870401792
print(id(b)) # 2069870401792

# * * * 깊은 복사 * * *
# ** 1번 [:]
a = [1,2]
b = a[:]
print(id(a)) # 2223254327680
print(id(b)) # 2223256651776

# ** 2번 copy 묘듈
from copy import copy
a = [1,2,3]
b = copy(a)
print(id(a)) # 2492648503744
print(id(b)) # 2492648182144