
# utilizando o WHILE - condicional:
'''

x = 1

while x < 5:
    print(x)
    #x = x + 1
    x += 1

print("Execução while parou!")

'''

'''
x = 10

while x > 0:
    print(x)
    #x = x - 1
    x -= 1

print("Execução while parou!")

'''
'''
qtd = int(input("\nInforme quantas notas deseja enviar pro sistema: "))

media = 0
i = 0

while i < qtd:
    nota = float(input("Informe o valor da nota: "))
    media += nota
    i += 1  #i = i + 1

print (f"Sua media é {media/qtd}")

'''

'''
i = 1

while i <= 10:
    if i == 3 or i == 7:
        i += 1
        continue

    print('valor de i: ', i)
    i += 1
'''

#Calculadora

'''
while True:
    operando1 = int(input('Digite o primeiro valor: '))
    operando2 = int(input('Digite o segundo valor: '))

    # Operacões aceitas: / * + -
    operacao = input('Digite a operação que deseja fazer: ')

    if operacao == '/':
        print('Resultado = ', operando1 / operando2)
    elif operacao == '*':
        print('Resultado = ', operando1 * operando2)
    elif operacao == '+':
        print('Resultado = ', operando1 + operando2)
    elif operacao == '-':
        print('Resultado = ', operando1 - operando2)

    else:
        print('Opção inválida')

    sair = int(input('Deseja sair: 1 - sim, 0 - não: '))

    if sair == 1:
        print('Tchau!!!')
        break
    else:
        continue

'''


### 1) Faça um algoritmo que apresente todos os números de 0 ao número recebido pelo teclado.
'''
num = int(input("Digite um número "))
i = 0
while i <= num:
    print(i)
    i += 1
'''
### 2) Faça o algoritmo definido acima apresentar somente os números pares.
'''
num = int(input("Digite um número "))

i = 0

while i <= num:
    print(i)
    i += 1
    if i%2==1:
        i +=1
        continue
'''

### 3) Apresentar o resultado de uma tabuada para um número qualquer.
'''
num = int(input("Digite um número "))

i = 0

while i <= 10:
    print(f"{i} x {num} = {num * i}")
    i += 1
'''

### 4) Leia várias idades e calcule a média entre as idades (usar uma variável para idade).

'''
qnt = int(input("Quantas pessoas voce quer analisar? "))

i = 1
media = 0

while i <= qnt:
    idades = int(input(f"Digite a idade da {i}ª pessoa: "))
    i += 1
    media += idades

print(f"A media de idade é igual a: {media//qnt}")
'''

### 5) Ler 10 números e imprimir quantos são pares e quantos são ímpares.
'''
i = 1

num_par = 0
num_impar = 0
while i <= 10:
    num = int(input("Digite um numero: "))
    i += 1
    if num % 2==0:
        num_par += 1
    else:
        num_impar += 1


print(f"Voce digitou {num_par} números pares e {num_impar} números ímpares.")

'''
### 6) Utilizando a estrutura de repetição, faça um programa que receba 10 números e conte quantos deles estão no intervalo
# 10,20] e quantos deles estão fora do intervalo, escrevendo estas informações.
'''
i = 1
dentro = 0
fora = 0

while i <= 10:
    num = int(input("Digite um número: "))
    i += 1
    if num >= 10 and num <= 20:
        dentro += 1
    else:
        fora += 1
print(f"Voce digitou {dentro} dentro do intervalo de 10-20. E {fora} fora desse intervalo.")


'''

### 7) Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados de idade, sexo (M/F) e salário.
# Faça um programa que calcule e mostre:

# a) A média dos salários do grupo;
# b) A maior e a menor idade do grupo;
# c) A quantidade de mulheres na região;
# d) A idade e o sexo da pessoa que possui o menor salário;
# Finalize a entrada de dados ao ser digitada uma idade negativa.

i = 1

idade = 0

masc = 0
fem = 0

qnt = int(input("Foi coletado os dados de quantas pessoas? "))

while i <= qnt:
    print(f"A seguir, insira os dados da {i}ª pessoa.")
    salario1 = float(input("Digite o salario: "))
    sexo = input("Identifique o sexo com 'M' para masculino e 'F' para feminino: ")
    idade = int(input("Digite a idade: "))
    i +=1
    if sexo == 'M':
        masc += 1
    elif sexo == 'F':
        fem += 1
    else:
        print("Voce digitou algo errado. Reinicie o programa!")
        continue
    media_salario = salario1 / qnt

print(f"Item a) A media salarial da região é: {media_salario}")
print(f"Item b) ")
print(f"Item c) Na região tem {fem} mulheres")
print(f"Item d) ")





