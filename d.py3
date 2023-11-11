def verificar(palavra1, palavra2):

  tamanho_menor = min(len(palavra1), len(palavra2))
  for i in range(tamanho_menor):
    if palavra1[i] != palavra2[i]:
      return i
  return tamanho_menor


while True:
    carac1 = input()
    if(carac1 == "0"): break

    palavra1 = input()
    carac2 = input()
    palavra2 = input()

    numeros = verificar(palavra1, palavra2)
    print(numeros)
