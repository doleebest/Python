dic = {'name':'Eric', 'age':15}
print(dic['name'])

a = {1:'a'}
a['name'] = "익명"  # put new value and key
print(a)

del a[1]
print(a) # delete 1:'a' 

#warning : the keys should not be duplicated.
b = {1:'a', 1:'b'}
print(b) # {1:'b'} remains only

#value can be duplicated
c = {1:'a', 2:'a'}
print(c) # {1: 'a', 2: 'a'} prints well


d = {1:'파랑구름', 2 : '이현준', 3:'민준'}
print(d.keys())    # print keys only
print(d.values())  # print values only
print(d.items())   # print keys and values in forms of tuple

d.clear()
print(d)

#get function
#print(c[3])     #error
print(c.get(3))  #None
print(c.get(3, '없음')) # print 없음 instead of 'None'


# boolean
print(1 in a) 