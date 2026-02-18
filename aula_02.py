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


# Exemplo que causa TypeError
# resultado = len(5)
# print(resultado)
try:
    resultado = len(5)
except TypeError as e:
    print(e)  # Imprime a mensagem de erro

numero = 10.0
if isinstance(numero, float):
    print("A variável é um float.")
else:
    print("A variável não é um float.")

numero_inteiro = 5
numero_flutuante = 2.5
# Converte o inteiro para flutuante e realiza a soma
soma = float(numero_inteiro) + numero_flutuante
print(soma)  # Resultado: 7.5

try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que executa se a exceção ZeroDivisionError for levantada
    print("Divisão por zero não é permitida.")

idade = 20
if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Exatamente 18 anos")
else:
    print("Maior de idade")

# Exercícios
# Aqui estão cinco exercícios que envolvem TypeError, verificação de tipo (type check), 
# o uso de try-except para tratamento de exceções e a utilização da estrutura condicional if. 
# Esses exercícios aumentam progressivamente em dificuldade e abordam situações práticas onde você pode aplicar esses conceitos.

# Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
# O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, 
# garantir que a entrada seja numérica, tratando qualquer ValueError. 
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.
try:
    celsius = float(input("Informe a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"A temperatura em Fahrenheit é: {fahrenheit}")
except ValueError:
    print("Entrada inválida. Por favor, insira um número para a temperatura em Celsius.")   

# Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, 
# desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. 
# Dica: Utilize a função isinstance() para verificar o tipo da entrada.
try:
    entrada = input("Informe uma palavra ou frase para verificar se é um palíndromo: ")
    if not isinstance(entrada, str):
        raise ValueError("Entrada inválida. Por favor, insira uma string.")
    
    # Remove espaços e pontuações para verificar o palíndromo
    entrada_limpa = ''.join(char for char in entrada if char.isalnum()).lower()
    
    if entrada_limpa == entrada_limpa[::-1]:
        print("A entrada é um palíndromo.")
    else:
        print("A entrada não é um palíndromo.")
except ValueError as e:
    print(e)

# Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
# Use try-except para lidar com divisões por zero e entradas não numéricas. 
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
# Imprima o resultado ou uma mensagem de erro apropriada.
try:
    numero1 = float(input("Informe o primeiro número: "))
    numero2 = float(input("Informe o segundo número: "))
    operador = input("Informe o operador (+, -, *, /): ")

    if operador == "+":
        resultado = numero1 + numero2
    elif operador == "-":
        resultado = numero1 - numero2
    elif operador == "*":
        resultado = numero1 * numero2
    elif operador == "/":
        if numero2 == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        resultado = numero1 / numero2
    else:
        raise ValueError("Operador inválido. Por favor, use +, -, * ou /.")

    print(f"O resultado da operação é: {resultado}")

except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)

# Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. 
# Utilize try-except para assegurar que a entrada seja numérica e 
# utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". 
# Adicionalmente, identifique se o número é "par" ou "ímpar".
try:
    numero = float(input("Informe um número: "))
    if numero > 0:
        print("O número é positivo.")
    elif numero < 0:
        print("O número é negativo.")
    else:
        print("O número é zero.")

    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")

except ValueError:
    print("Entrada inválida. Por favor, insira um número.")

# Exercício 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
# O programa deve converter a string de entrada em uma lista de números inteiros. 
# Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. 
# Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. 
# Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

entrada = input("Informe uma lista de números separados por vírgula: ")
numeros_str = entrada.split(",")
numeros_int = []

try:    
    for num_str in numeros_str:
        num_str = num_str.strip()  # Remove espaços em branco

        numero = int(num_str)  # Tenta converter para inteiro
        if isinstance(numero, int):
            numeros_int.append(numero)
        else:
            raise ValueError("O número não é um inteiro válido.")

    print(f"A lista de números inteiros é: {numeros_int}")
except ValueError as e:
    print(e)
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")


#------------------------------------------------------------------------
# Desafio
#------------------------------------------------------------------------

# 1. O programa deve começar solicitando ao usuário que insira seu nome.
# 2. Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
# 3. Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
# 5. Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
# 4. O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
try:
    nome = input("Informe o seu nome: ")
    if nome.isdigit():
        raise ValueError("Entrada inválida. Por favor, insira um nome válido.")
    
    salario = float(input("Informe o seu salário: "))
    if isinstance(salario, float):
        porcentagem_bonus = float(input("Informe a porcentagem do bônus recebido: "))
        if not isinstance(porcentagem_bonus, float):
            raise ValueError("A porcentagem do bônus deve ser um número decimal.")
    else:
        raise ValueError("O salário não é um número válido.")
    
    bonus = 1000 + salario * (porcentagem_bonus/100)
    
    print(f"Olá {nome}, o seu valor bônus foi de {bonus}")

except ValueError as v:
    print(v)
    exit()
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
    exit()