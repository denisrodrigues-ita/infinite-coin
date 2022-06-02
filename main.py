q = 25
d = 10
n = 5
p = 1
cq = cd = cn = cp = 0

lista = []

num = int(input("digite a quantidade: "))

while True:
    if num >= q:
        cq += 1
        num -= q
    elif num >= d:
        cd += 1
        num -= d
    elif num >= n:
        cn += 1
        num -= n
    else:
        cp += 1
        num -= p
    if num == 0:
        break

lista.append(cq)
lista.append(cd)
lista.append(cn)
lista.append(cp)
print(lista)
