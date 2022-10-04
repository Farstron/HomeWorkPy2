import random
# с shuffle
lis = [1,2,3,4,5,6,7,8]
random.shuffle(lis)
print(lis)

#  без shuffle
lis2=[1,2,3,4,5,6,7,8]
i = 1
while i < len(lis2):
    pos = int(random.randrange(0,len(lis2)-1,1))
    temp = lis2[i]
    lis2[i] = lis2[pos]
    lis2[pos] = temp
    i+=1
print(lis2)