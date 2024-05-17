# bool 연산

t = bool('python') # 빈 문자열이 아니므로 true
f= bool('') # 빈 문자열이므로 false
print(t) # true
print(f) # false

t = bool([1,2,3])
f = bool([])
print(t)
print(f)

t = bool(3)
f = bool(0) # 0 은 false
print(t)
print(f)