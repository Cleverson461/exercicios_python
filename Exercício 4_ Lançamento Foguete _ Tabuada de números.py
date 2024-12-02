""" 
        ## Contagem Regressiva

Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”.
"""
import winsound

contagem = 10
while contagem >= 0:
    print(contagem)
    contagem -= 1
winsound.Beep(500, 1000)