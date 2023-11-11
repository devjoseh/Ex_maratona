def subquencia(n1, n2):

  i = 0
  j = 0
  
  while i < len(n1) and j < len(n2):
    if n1[i] == n2[j]:
        j += 1
    i += 1
  return j == len(n2)


while True:
    a, b = map(int, input().split(" "))

    if a == 0 and b == 0: break

    n1 = list(map(int, input().split(" ")))
    n2 = list(map(int, input().split(" ")))

    if(subquencia(n1, n2)):
       print("Sim")
    else:
       print("Nao")