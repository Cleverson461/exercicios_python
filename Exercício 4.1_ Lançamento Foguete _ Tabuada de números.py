""" 
	## Tabuada

Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário
"""

numero = int(input("Tabuada de: "))
begin = int(input("De: "))
end = int(input("Até: "))

x = begin

while x < end:
    print(f"Tabuada de {numero} x {x} = {numero * x}")
    x += 1
