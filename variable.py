#pointer : share same "address"
a = [1,2,3]
b = a # a and b share same "address"
a[1] = 4
print(a)
print(b)

#figuring out address
print(id(a))
print(id(b))
print(a is b) # if addresses are same

# slice and copy 
c = [1,2,3]
d = c[:] 
d[1]=4
print(c) # [1, 2, 3]
print(d) # [1, 4, 3]
print(id(c))
print(id(d)) # different address

# you can use func
from copy import copy
e = [1,2,3]
f = copy(e)
e[1] = 4
print(e)
print(f)

# assign variable
g , h = ('python', 'life')
#(g,h) = ('python', 'life')
#(g,h) = 'python', 'life'
#[g,h] = 'python', 'life'
print(g)
print(h)

i = j = 'hello'
print(i)
print(j)

#switch
k = 3
l = 5
k,l = l,k
print(k)
print(l)

