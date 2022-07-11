#change list
a = ["이소정", "이유진", "김소현"]
a[0:2]  = ["박소정","김유진"]
print(a)


#delete list
#1
a[0:2] = [] 
print(a)

#2
del a[0]
print(a)


#append : 요소 추가
b = ["박주하", "잠수", "문재성"]
b.append("시우버")
print(b)


#sort : 숫자, 문자 모두 가능
c = ['a', 'c', 'b']
c.sort()
print(c)
c.reverse()
print(c)


#insert
d = [1,5,3]
d.insert(0,4) # insert 4 in 0th index
print(d)


#remove
e = [1,2,3,1,2,3]
e.remove(3) # 3이라는 값을 제거하라 (가장 먼저 걸리는거 하나)
print(e)


#pop
f = [1,3,5]
print(f.pop()) # pop the last value = 3
print(f)


#count
g = [1,5,3,1,1]
print(g.count(1))


#extend
h = [1,2,3]
print(h.extend([2,3]))
print(h)