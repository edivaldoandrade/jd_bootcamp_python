#Print
print("Seja bem-vindo ao curso de Python!")
print("Olá " + input("Informe o seu nome: ") + "!")

#Exercício 1: Imprima o número de caracteres do nome informado pelo usuário.
nome = input("Informe o seu nome: ")
print(len(nome))

#Exercício 2: Digite 2 valores e retorne a soma
valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("informe o segundo valor: "))
soma = valor1 + valor2
print("a soma dos valores é: " + str(soma))

#------------------------------------------------------------------------
# Desafio
#------------------------------------------------------------------------

# 1. O programa deve começar solicitando ao usuário que insira seu nome.
nome = input("Informe o seu nome: ")

# 2. Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
salario = float(input("Informe o seu salário: "))

# 3. Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
porcentagem_bonus = float(input("Informe a porcentagem do bônus recebido: "))

# 4. O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
bonus = 1000 + salario * (porcentagem_bonus/100)

# 5. Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
print(f"Olá {nome}, o seu valor bônus foi de {bonus}")