""" 
	## Lista números pares e ímpares de uma lista

	Escreva uma função Python para imprimir os números pares e ímpares em duas listas separadas para cada uma. 
"""


def impa_par(numbers):
    pairs = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            pairs.append(number)
        else:
            odd.append(number)
    return f"Pares {pairs} - Impares {odd}"


print(impa_par([1, 2, 4, 6, 5, 7, 11, 20]))
