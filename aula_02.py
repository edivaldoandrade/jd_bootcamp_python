
import math

# Inteiros (int)
# Escreva um programa que soma dois números inteiros inseridos pelo usuário.
numero1 = int(input("Informe o primeiro número inteiro: "))
numero2 = int(input("Informe o segundo número inteiro: "))
soma = numero1 + numero2
print(f"A soma dos números é: {soma}")
# Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero_usuario = int(input("Informe um número inteiro: "))
resto_divisao = numero_usuario % 5
print(f"O resto da divisão por 5 é: {resto_divisao}")
# Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
multiplicando = int(input("Informe o primeiro número para multiplicação: "))
multiplicador = int(input("Informe o segundo número para multiplicação: "))
produto = multiplicando * multiplicador
print(f"O produto dos números é: {produto}")
# Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
dividendo = int(input("Informe o dividendo (número a ser dividido): "))
divisor = int(input("Informe o divisor (número pelo qual será dividido): "))
divisao_inteira = dividendo // divisor
print(f"A divisão inteira é: {divisao_inteira}")
# Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero_quadrado = float(input("Informe um número para calcular seu quadrado: "))
quadrado = numero_quadrado ** 2
print(f"O quadrado do número é: {quadrado}")


# Números de Ponto Flutuante (float)
# Escreva um programa que receba dois números flutuantes e realize sua adição.
numero_float1 = float(input("Informe o primeiro número flutuante: "))
numero_float2 = float(input("Informe o segundo número flutuante: "))
soma_float = numero_float1 + numero_float2
print(f"A soma dos números flutuantes é: {soma_float}")
# Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
media = (numero_float1 + numero_float2) / 2
print(f"A média dos números flutuantes é: {media}")
# Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input("Informe a base: "))
expoente = float(input("Informe o expoente: "))
potencia = base ** expoente
print(f"A potência é: {potencia}")
# Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Informe a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit}")
# Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Informe o raio do círculo: "))
area = math.pi * raio ** 2
print(f"A área do círculo é: {area:.2f}")

# Strings (str)
# Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
string_usuario = input("Informe uma string: ")
string_maiuscula = string_usuario.upper()
print(f"A string em maiúsculas é: {string_maiuscula}")
# Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_completo = input("Informe seu nome completo: ")
nome_minusculo = nome_completo.lower()
print(f"Seu nome em minúsculas é: {nome_minusculo}")
# Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Informe uma frase: ")
frase_sem_espacos = frase.strip()
print(f"A frase sem espaços é: {frase_sem_espacos}")
# Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Informe uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split("/")
print(f"Dia: {dia}, Mês: {mes}, Ano: {ano}")
# Escreva um programa que concatene duas strings fornecidas pelo usuário.
string1 = input("Informe a primeira string: ")
string2 = input("Informe a segunda string: ")
concatenacao = string1 + string2
print(f"A concatenação das strings é: {concatenacao}")

# Booleanos (bool)
# Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
expressao1 = input("Informe a primeira expressão booleana (True/False): ")
expressao2 = input("Informe a segunda expressão booleana (True/False): ")
resultado_and = (expressao1 == "True") and (expressao2 == "True")
print(f"O resultado da operação AND é: {resultado_and}")    
# Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
expressao_or = (expressao1 == "True") or (expressao2 == "True")
print(f"O resultado da operação OR é: {expressao_or}")
# Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
expressao_invertida = not (expressao1 == "True")
print(f"O valor invertido é: {expressao_invertida}")
# Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))
numeros_iguais = numero1 == numero2
print(f"Os números são iguais? {numeros_iguais}")
# Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
numeros_diferentes = numero1 != numero2
print(f"Os números são diferentes? {numeros_diferentes}")