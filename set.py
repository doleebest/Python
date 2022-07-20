# list changes into set
#s1 = set([1,2,3])
s1 = {1,2,3}   # both way work
print(s1)

s2 = set("Hello")
print(s2) # there's no sequence and overlap in set

#intersection
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1 & s2)
print(s1.intersection(s2))

#union
print(s1|s2)
print(s1.union(s2))

# difference
print(s1-s2)
print(s1.difference(s2))

# add
s1.add(7)
print(s1) # {1, 2, 3, 4, 5, 6, 7}

#update
s1.update([7,8,9]) # add multiple elements
print(s1) # {1, 2, 3, 4, 5, 6, 7,8,9}

#remove
s2 = set([1,2,3,4,5,6])
s2.remove(1)
print(s2)

# boolean
a = True
print(type(a))

b = "hello"
if b :     # string = True, blank string("") = False
  print(b) # 안녕

c = [1,2,3,4]
while c : 
  c.pop()
  print(c)

# cs
d = [1,2,3]
e = d
d[1] = 4
print(d)
print(e)
