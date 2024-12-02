""" 
	## Substituindo caractere repetido
Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere

Ex:
fifa 23 → **fi#a 23**
restart→ resta#t
"""
string = "Fifa 23"
char = string[0].lower()
new_name = string.replace(char, '$')
new_name = char + new_name[1:]
print(new_name)


""" 
	## Substituindo caractere repetido
Escreva um programa Python para obter uma única string de duas strings fornecidas, separadas por um espaço e troque os dois primeiros caracteres de cada string.

Ex:

abc xyz → **xyc abz**
"""
palavra = "abc"
palavra2 = "xyz"

new_palavra = palavra2[:2] + palavra[2:]
new_palavra2 = palavra[:2] + palavra2[2:]
print(new_palavra)
print(new_palavra2)