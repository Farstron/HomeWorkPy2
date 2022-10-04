import random


N = int(input('Введите число:(больше 4)'))
c = 0
lis = []
while N != c:
    c +=1
    lis.append(int(random.randrange(-N,N,1)))
pos = []
file1 = open("file.txt", "r")
while True:
    line = file1.readline()
    if not line:
        break
    pos.append(int(line))
file1.close
print(pos)
res = 1
for i in pos:
    res *= lis[i]
print(lis, res)