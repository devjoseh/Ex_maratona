
while True:
    valores = list(map(int, input().split(" ")))
    v = valores[0]
    if (v == 0 ):
        break

    a = valores[1]
    b = valores[2]
    c = valores[3]

    quantia = 0

    for valor in [a, b, c]:
        if v >= valor:
            quantia += 1
            v -= valor
        else:
            continue

    print(quantia)