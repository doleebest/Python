a = 'hobby'
#count
print(a.count('b')) # hobby에서 b가 몇 개 있는지 

#find
print(a.find('b')) # hobby에서 b가 가장 먼저 나오는 index
print(a.find('x')) # x는 없으므로 -1이 출력됨

#index
print(a.index('o'))
#print(a.index('4')) # 없으면 error

#join
b = ",".join("abcd") # abcd 문자열의 각각의 문자 사이에 ','를 삽입한다.
print(b)
c = ",".join(['a','b','c','d']) # tuple로도 가능
print(c)

#upper & lower
d = "hi"
print(d.upper())
print(d.lower())

print("---------------------")
#strip (lstrip & rstrip)
e = " hi "
print(e.lstrip())
print(e.rstrip())
print(e.strip())

#replace
f = "Life is too short"
print(f.replace("Life", "Your leg"))

#split : 문자열 자료형이 있으면 띄어쓰기 기준으로 자르는 함수
g = "Life is too short"
print(g.split())
h= "a:b:c:d"
print(h.split(':'))