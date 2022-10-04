import math

def lin(N, count = 1, res_list = [1]):
    if count != N:
        res_list.append(res_list[count-1]*(count+1))
        return lin(N, count + 1,res_list)
    return res_list
N = int(input('Введите число:'))
print(lin(N))

# Вариант с подключенной библиотекой
i = 0
while i != N:
    print(math.factorial(i+1))
    i+=1