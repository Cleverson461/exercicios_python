""" 
	## Cálculo da Distância

Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
0,35 para viagens mais longas.
"""
distancia_corrida = float(input("Informe a distância que deseja percorrer? "))
valor = 0

if distancia_corrida <= 200:
    valor = distancia_corrida * 0.50
    print(f"O valor da sua corrida em uma distância de {distancia_corrida}KM, é de R${valor:.2f}")
else:
    valor = distancia_corrida * 0.35
    print(f"O valor da sua corrida em uma distância de {distancia_corrida}KM, é de R${valor:.2f}")
    