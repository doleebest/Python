number = 10
day = "three"
a = "I ate %d apples. so I was sick for %s days." % (number,day)
print(a)

b = "djfkaljdfa {} jfkdjsdlj". format("안녕하세요.")
print(b)

c = "My name is {name}, and i'm {age} years old. ". format(name = "이소정", age = 23) # 순서 바꿔써도 올바르게 입력
print(c)

names = "int"
g = f"나의 이름은 {names}입니다." # 복잡하지 않게 f만 붙이면 format 안써도 됨
print(g)


# 정렬 -> 잘 안쓰임
d = "%10s" % "hi" # %10s는 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽 정렬하고 그 앞의 나머지는 공백으로 남겨두라는 의미
print(d) 

e = "%-10sjane" % 'hi' # 반대로 왼쪽 정렬은 -10
print(e) 

f = "%10.4f" % 3.141592 # 소수점 네번째 자리까지, 전체길이가 10개인 문자열 공간에서 오른쪽 정렬 + 반올림
print(f)
