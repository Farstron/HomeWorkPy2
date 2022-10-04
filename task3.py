n = int(input('Введите число:'))
i = 2
d = round((1+1/n)**n)
res_dict = {1:(1+d)}
while i != n+1:
    res = res_dict.get(i-1)+d
    res_dict.update({i:res})
    i+=1
print(res_dict)