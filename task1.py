n = int(input('Введите количество цифр после запятой:'))
numb = float(input('Введите вещественное число:'))
sum = 0
cn = int(numb)
dn = int(round(numb % 1, n) *10**n)
print(dn,cn)
while cn / 10 != 0:
    sum += cn % 10
    cn //= 10
while dn / 10 != 0:
    sum +=dn % 10
    dn //= 10
print(round(sum))