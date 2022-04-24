
# FUNÇÕES
'''

def somar(valor_1, valor_2, valor_3):
    print(f"O resultado da soma de {valor_1 + valor_2 + valor_3}")

def somar_2():
    valor_1 = int(input("informe o valor1: "))
    valor_2 = int(input("informe o valor1: "))
    print(f"O resultado da soma de {valor_1 + valor_2}")

somar(3,5,10)
# vai na ordem dos parametros estabelciodos no "def"
'''

### 01. Crie uma função que recebe um parâmetro e informe se ele é par ou ímpar

'''
def par_ou_impar(num):
    if num%2 == 0:
        print("Este valor é Par")
    else:
        print("Este valor é Impar")

var = int(input("Digite um numero:"))
par_ou_impar(var)
# ou print(par_ou_impar(int(input("Digite um numero: "))))

'''

### 02. Crie uma função que recebe dois parâmetros (nome, mensagem) e imprima na tela uma saudação
# com o nome da pessoa e a mensagem passada
'''
def saudação(nome, msg):
    print(f"Olá, meu nome é {nome}. {msg}")

saudação("Infinity", "Somos uma escola premium")
'''
        # ou
'''
def saudação(nome, msg):
    print(f"Olá, meu nome é {nome}. {msg}")

nome = input('Entre com o seu nome: ')
msg = input('Entre com a sua mensagem: ')
saudação(nome, msg)
'''

### 03. Criar uma função que recebe três notas como parâmetros e imprima a média

'''
def media(num_1,num_2,num_3):
    print(f"A media dos valores é: {(num_1 + num_2 + num_3)/3:.2f}")

num_1 = float(input("informe o valor1: "))
num_2 = float(input("informe o valor2: "))
num_3 = float(input("informe o valor3: "))

media(num_1,num_2,num_3)

'''


### 04. Criar uma função para calcular  o IMC do usuário
# IMC = peso / altura ** 2
'''
def calc_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f'Seu imc é: {imc:.2f}')

peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))

calc_imc(peso, altura)

'''
##########################################################################

# RETURN
'''
def somar(valor1, valor2):
    return valor1 + valor2

soma = somar(12,18)

print(f"O resultado da soma é: {soma}")
'''


'''
def autenticacao(login, senha):
    if login.lower() == 'adm' and senha == '123':
        return True
    else:
        return False

def segunda_etapa(autenticacao):
    if autenticacao == True:
        print('Logado com sucesso!!!')
    else:
        print('Dados incorretos!!!')

login = input('Informe seu login: ')
senha = input('Informe a sua senha: ')

autentic = autenticacao(login, senha)

segunda_etapa(autentic)
'''
# Diga se o numero é positivo ou negativo
"""
def maior_ou_menor(num1, num2):
    if num1<num2:
        print(f"O numero {num2} é maior.")
    elif num2<num1:
        print(f"O numero {num1} é maior.")
    else:
        print("Os numeros sao iguais")

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

maior_ou_menor(num1, num2)
"""

# Some a e b e veja se ele e menor que o limite estabelecido
'''
def numero(num1):
    if num1<0:
        print(f"O numero {num1} é negativo.")
    else:
        print(f"o numero {num1} é positivo")

num1 = int(input("Digite um numero: "))

numero(num1)

'''
# Some a e b e veja se ele e menor que o limite estabelecido
'''
def soma(a, b, limite):
    if (a + b) < limite:
        return True
    else:
        return False

a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
limite = int(input("Informe o limite: "))

resultado = soma(a, b, limite)
print(resultado)

'''
"""
def teste(a, b, limite):
    contador = 0
    if a > limite or b > limite:
        contador += 1
    elif a > limite and b > limite:
        contador += 2
    else:
        contador = 0
    print(contador)

a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
limite = int(input("Informe o limite: "))

resultado = teste(a, b, limite)
"""


def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return n

f = int(input("Digite um numero: "))

resultado = fizzbuzz(n)
print(resultado)












