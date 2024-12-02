""" 
	Antecessor e Sucessor de um número
Escreva um programa em Python que leia um número e represente o número antecessor e sucessor desse número que foi lido, utilizando operadores de atribuição.	
"""
number = int(input('Informe um número: '))
print(f'O número digitado foi {number} seu antecessor é {number - 1} e o sucessor é {number + 1}')

""" 
	Média de 4 notas
Escreva um programa em Python que leia quatro números e calcule a média entre esses números
"""
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quinta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'A média é {media}')