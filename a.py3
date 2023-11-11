import sys
import math

resultados = []

numero_teste = 1

while True:
    # Leitura de N e M
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break

    temperaturas = [int(input()) for _ in range(N)]

    menor_media = float('inf')
    maior_media = float('-inf')

    for i in range(N - M + 1):
        soma_intervalo = sum(temperaturas[i:i + M])
        media = int(soma_intervalo / M)
        menor_media = min(menor_media, media)
        maior_media = max(maior_media, media)

    resultados.append((numero_teste, (menor_media, maior_media)))

    numero_teste += 1

# Impressão dos resultados
for numero_teste, resultado in resultados:
    print(f"Teste {numero_teste}")
    print(f"{resultado[0]:0.0f} {resultado[1]:0.0f}")
    print()

sys.exit()

