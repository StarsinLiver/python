# 튜플 자료형 == ()
# 리스트는 생성 , 수정 , 삭제가 가능하나 튜플은 그 값을 바꿀 수 없다
# 한마디로 튜플의 요솟값은 한 번 정하면 지우거나 변경할 수 없다

# 튜플 요소값을 삭제하려 할 때
# t1 = (1 ,2 , 'a' , 'b')
# del t1[0] # 튜플 t1의 첫번째 요소를 지우려고 시도

# 튜플의 요솟값을 변경하려 할 때
# t1 = (1 , 2, 'a' , 'v')
# t1[0] = 'c'

# 에러
#Traceback (most recent call last):
  # File "c:\ALL_WORKSPACE\1_STUDY\04_pyton\code1\tuple.py", line 8, in <module>
    # del t1[0] # 튜플 t1의 첫번째 요소를 지우려고 시도
        # ~~^^^
# TypeError: 'tuple' object doesn't support item deletion

# *********************************

# ** 튜플 슬라이싱
t1 = (1 , 2 , 'a')
print (t1[:1])
print (t1[0:])
print (t1[0:2])

# ** 튜플 더하기
t1 = (1 , 2 , 'a')
t2 = (1 , 2 , 'a')
t3 = t1 + t2
print(t3) # (1, 2, 'a', 1, 2, 'a')

# ** 튜플 곱하기
t2 = t1 * 3
print(t2) # (1, 2, 'a', 1, 2, 'a', 1, 2, 'a')

# ** 튜플 길이 구하기 (len)
len(t1)