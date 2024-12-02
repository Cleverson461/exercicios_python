""" 
	## Aumento salário funcionário

Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. 
Para os inferiores ou iguais, de
15%.
"""
salario_funcionario = float(input("Informe o seu salário? "))
novo_salario = 0

if salario_funcionario <= 1250.00:
    novo_salario = salario_funcionario * 0.15
    resultado = novo_salario + salario_funcionario
    print(f"Para salarios inferios ou iguais a R${salario_funcionario} tem um aumento de 10% {novo_salario} com novo salario de {resultado:.2f}")
else:
    novo_salario = salario_funcionario * 0.1
    resultado = novo_salario + salario_funcionario
    print(f"Para salarios superiores a R${salario_funcionario} tem um aumento de 15% {novo_salario} com novo salario de {resultado:.2f}")
    