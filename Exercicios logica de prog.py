## (EASY) Faça um Programa que converta metros para centímetros. (Dica: peça um valor em metros e mostre o valor em centímetros)
"""
m = float(input("Informe sua altura em centimetros: "))
cm = m / 100

print(f"Covertendo para metros, é: {cm}")
"""
## (EASY) Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. (Valor de PI x R^2) (Como se calcula a área do círculo? Vamos pesquisar!)
"""
raio = float(input("Qual o raio do circulo em metros? "))
# Pi = 3,14 (aproximadamente)
area = 3.14 * (raio ** 2)

print(f"A area do circulo é de: {area:.2f}metros²")
"""
## (HARD) Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. Utilize a biblioteca MATH para conseguir o valor de PI.
"""
import math

raio = float(input("Qual o raio do circulo em metros? "))
area = math.pi * (raio ** 2)

print(f"A area do circulo é de: {area:.2f}metros²")
"""
## (EASY) Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9)
"""
fahr = float(input("Informe a temperatura em graus Fahrenheit: "))
celsius = 5 * ((fahr - 32) / 9)

print(f"Convertendo para celsius, a temperatura é: {celsius}ºC")
"""
## (HARD) Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""
celsius = float(input("Informe a temperatura em graus Celsius: "))
fahr = ((celsius * 9) / 5) + 32

print(f"Convertendo para celsius, a temperatura é: {fahr}ºF")
"""
## (EASY) Imprima um número em tela
"""
print("10")
"""
## (EASY) Crie uma variável com um número inteiro, imprima a variável
"""
n = 10

print(n)
"""
## (EASY) Peça ao usuário um número e depois imprima o número em tela
"""
n = int(input("Digite um numero: "))

print(n)
"""
## (EASY) Faça um Programa que peça dois números e imprima a soma.
"""
x = int(input("Digite um numero: "))
y = int(input("Digite outro numero: "))

soma = x + y

print(f"A soma dos numeros é: {soma}")
"""
## (EASY) Faça um Programa que peça as 4 notas e calcule a média. Ao final do programa, mostre todas as notas e por fim, a média.
'''
n1 = int(input("Digite sua primeira nota : "))
n2 = int(input("Digite sua segunda nota : "))
n3 = int(input("Digite sua terceira nota : "))
n4 = int(input("Digite sua quarta nota : "))

media = (n1 + n2 + n3 + n4) / 4

print(
    f"Sua primeira nota foi {n1}, a segunda foi {n2} a terceira foi{n3} a quarta foi {n4}. Sua media geral foi {media:.2}")
'''
## (HARD) Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
area = float(input("Informe qual a area de onde deseja pintar (em m²): "))

qnt = area // 54
if area % 54 > 0:
    qnt += 1
gasto = qnt * 80

print(f"Voce precisara comprar {qnt:.0f} latas. O valor total é da sua compra será de R${gasto:.0f}")
'''
## (HARD) Peça ao usuário uma velocidade em Km/h (Quilômetro por hora) e converta para M/s (Metros por segundo).
# A fórmula utilizada é Km = M * 3.6 (K é a velocidade em Km/h e M a velocidade em M/s)
'''
km = float(input("Informe a velocidade em km/h: "))

m = km / 3.6

print(f"Convertendo, a velocidade é de: {m:.2f}m/s")
'''
## (HARD) Altere o programa acima para que a velocidade solicitada ao usuário seja em M/s, e então, converta para Km/h.
'''
ms = float(input("Informe a velocidade em m/s: "))

km = ms * 3.6

print(f"Convertendo, a velocidade é de: {km:.2f}k/h")
'''
## (EASY) Peça três número inteiros e imprima a soma entre eles.
'''
n1 = int(input("Digite um numero inteiro: "))
n2 = int(input("Digite outro numero inteiro: "))
n3 = int(input("Digite mais um numero inteiro : "))

soma = n1 + n2 + n3

print(f"A soma é igual a: {soma}")
'''
## (HARD) Um funcionário recebeu um aumento de 25% no seu salário. Peça o salário atual e mostre em tela o salário com o aumento.
'''
salario = float(input("Informe o seu salario atual: "))

aumento = salario + (salario * 0.25)

print(f"Seu salario passará a ser: R${aumento:.2f}")
'''
## (HARD) Um prêmio da loteria de R$ 540.000 será dividido entre três pessoas. Informe o valor recebido por cada pessoa.
'''
premio = 540000 / 3

print(f"Cada um receberá R${premio:.0f}")
'''
## (HARD) O prêmio acima foi entregue à três ganhadores de um concurso. O primeiro receberá: 47% O segundo receberá: 31% O terceiro receberá o restante
# Calcule e mostre em tela o valor recebido por cada ganhador.


## (HARD) Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

# o produto do dobro do primeiro com metade do segundo .

# a soma do triplo do primeiro com o terceiro.

# o terceiro elevado ao cubo.

## (HARD) Peça três valores (um int, um float, uma string) ao usuário e ao final, mostre em tela o valor e o TIPO de cada um.

## (HARD) Mostre em tela o valor da divisão de um número inteiro digitado pelo usuário por dois. OBS: A operação é por módulo: número MÓDULO 2.