while True:
    violacao = 0
    a, b, c = map(int, input().split())
     
    if a == 0:
        break

    if c > (a/2):
        
     a, b, c = map(int, input().split())
    

    if c < a:

        for i in range(0, b):
            n1, n2 = map(int,input().split())

        for i in range(0, c):
            n1, n2 = map(int,input().split())

        if b == 0:
            violacao = 2
            print(violacao)

        if c == 0:
            violacao = 0
            print(violacao)

        if c > b and b != 0:
            violacao = a - c*2
            print(violacao) 

        elif c != 0 and b != 0:
            violacao = a - b*2
            print(violacao)

