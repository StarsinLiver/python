# 클래스란?

class Calcluator :
  def __init__ (self) :
    self.result = 0
  
  def add (self , num) :
    self.result += num
    return self.result
  

cal1 = Calcluator()

print(cal1.add(1))

# * * * 클래스 구조 만들기 * * *

# ** self
class OneClass :
  # pass # pass 를 활용하여 빈 클래스를 만들 수 있다.

  # ** self 란?? FourCal 객체를 의미한다
  # ** 따라서 setData(객체 , first , second) 라는 식이며 메서드를 호출 할 때 자기자신인 객체를 인수로 넣기때문에
  # 호출 할 때는 setData(1,2) 인수 2개로 가능하다.
  def setData(self , first , second) :
    self.first = first
    self.second = second
    
  def toString(self) :
    return f"{{ first = {self.first} , second = {self.second} }}"
    

a = OneClass()
a.setData(2,3)
print(a.toString())

# ** 생성자 constructor
# 파이썬에서는 메서드 이름으로 __init__을 사용하면 이 메서드는 생성자로 가능하다

class TwoClass :
  def __init__ (self , first , second) :
    self.first = first
    self.second = second
    
  def toString(self) :
    return f"{{ first = {self.first} , second = {self.second} }}"
    
t = TwoClass(1 , 2)
print(t.toString())


# ** 클래스의 상속 (Inheritance)
class ThreeClass(TwoClass) : 
  pass


# ** 클래스의 변수
# 이쯤되면 의문이 든다
# self.first [객체변수] 와 클래스의 변수는 차이가 뭘까?
# 객체변수는 다른 객체들에 영향을 받지 않고 독립적으로 그 값을 유지한다는 점이 있다.

class FourClass :
  lastName = '감'
  firstName = '자'

a = FourClass()
b = FourClass()
print(a.firstName)
print(b.firstName)

print(id(a.firstName)) # 2901153847856
print(id(b.firstName)) # 2901153847856

# 이때 firstName 을 바꾸면?
FourClass.firstName = "자에 싹이 나서 잎이 나서"

print(a.firstName) # 자에 싹이 나서 잎이 나서
print(b.firstName) # 자에 싹이 나서 잎이 나서

# 즉 클래스 변수는 클래스로 만든 모든 객체에 공유가 된다는 특징이 있다.
print(id(a.firstName)) # 2901153847856
print(id(b.firstName)) # 2901153847856

# 왠만하면 객체 변수를 사용하는 비율이 높다.