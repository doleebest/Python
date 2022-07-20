# you can change the component in case of list, unlike tuple. That's the difference between list and tuple

t1 = (1,2,'a','b')
#del t1[0] 
# 'tuple' object doesn't support item deletion

t1[0] = 'c'
#'tuple' object does not support item assignment

#we can print and slice the tuple 
print(t1[0])
print(t1[0:2])

#also adding and multipling tuple is possible
t2 = (3,4)
print(t1+t2)
print(t1*3) # write t1 three times
