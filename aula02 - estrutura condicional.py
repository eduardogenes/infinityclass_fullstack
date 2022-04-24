
# ESTRUTURAS CONDICIONAIS IF / ELSE
'''
if
else

'''
'''
if 5 > 4:
    print("5 é maior que 4")
    
    # o afastamento com "tab" mostra onde a funcao "if" vai agir

'''
'''
if 5 > 4:
    print("A condição É verdadeira")
    var = 4
    print(var)
else:
    print("A condição NAO é verdadeira")
    
    #sempre lembrar de tabular!! ou seja, formatar com "tab" e apos o 'else' colocar dois pontos ":"
    
'''
### EXERCICIOS DE IF E ELSE

### ex001 - leia dois numeros e apresente oi maior entre eles
'''
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

if n1 > n2:
   # print("Entre os numeros digitados, o maior é ", n1)
    #ou
   # print(f"Entre os numeros digitados, o maior é {n1}")
    #ou
   print("Entre os numeros digitados, o maior é {}".format(n1))


else:
    # print("Entre os numeros digitados, o maior é ", n2)
    # ou
    # print(f"Entre os numeros digitados, o maior é {n2}")
    # ou
    print("Entre os numeros digitados, o maior é {}".format(n2))
'''
### ex002 - leia uma idade e informe se o usuario é maior de idade ou nao
'''
idade = int(input("Qual a sua idade? "))
if idade >= 18:
    print("Voce é MAIOR de idade!")
else:
    print("Voce é MENOR de idade")
    
'''
### ex003 - leia um numero e informe se ele é par ou impar
'''
numero  = int(input("Digite um numero: "))
if numero%2 == 0:
    print("O numero digitado é PAR")
else:
    print("O numero digitado é IMPAR")

'''
### ex004 - leia uma altura e se a altura for inferior a 1.50, iforme que nao pode entrar no brinquedo
'''
altura = float(input("Qual a sua altura? "))
if altura >= 1.50:
    print("Você PODE entrar no brincado")
else:
    print("Voce NAO pode entrar no brinquedo")
'''
### ex005 - verifique uma senha fornecida pelo usuario e se for diferente de 12345, infomar que o acesso esta negado
'''
senha = input("Digite sua senha de 5 digitos: ")
if senha == '12345':
    print("ACESSO PERMITIDO!")
else:
    print("ACESSO NEGADO!")
       ### senha normalmente é utilizada string
'''
############################################################
# OPERADORES LÓGICOS


# and
# or
# not


'''
altura = 1.66
vestep = altura > 1.30 and altura < 1.70
print(vestep)
'''
'''
estudante = True
professor = False
### exemplos de uso
# meia_entrada = estudante == True or professor == True
# meia_entrada = not (estudante == True) or professor == True

print(meia_entrada)
'''


### elif (else if)


'''
idade < 12               ---- 100% de deconto
idade>= 12 e idade 17    ---- 50% de desconto
idade >= 17 a idade < 22 ---- 25% de desconto
idade >= 22               ---- 0% de desconto
'''
'''
idade = int(input("Digite sua idade: "))

if idade <12:
    print("Voce tem 100% de desconto")
elif idade >= 12 and idade < 17:
    print("Voce tem 50% de desconto")
elif idade >= 17 and idade <= 22:
    print("Voce tem 25% de desconto")
else:
    print("Voce nao tem desconto")
'''

'''
ARENA CASTELAO

categoria - professor, estudante, pcd, nenhum
faixa salario -  0 - 1000, 1001 - 2000, 3000
idade -  0 a 12, 13 - 22, 23 - 60

vip -  pcd, salario > 300 idade 60
camarote - professor, estudante, salario até 2000
pista -  nenhum, 0 -1000, 13 a 22

'''
'''
categoria = int(input("informe sua categoria"
                      "1- professor"
                      "2 - estudante"
                      "3 - pcd"
                      "4- nenhum"))
faixa_sal = float(input("Iforme o seu salario: "))
idade = (int(input("Informe a sua idade: ")))

if categoria == 3 or faixa_sal > 3000 or idade > 60:
    print("Voce vai pra area VIP")
elif categoria == 1 or categoria == 2 or faixa_sal < 2000:
    print("Voce vai para o CAMAROTE")
else:
    print("Voce vai para PISTA")

'''
### ex001 exercicios com elif
# hora entre 6 e 11 (imprimir bom dia)
# hora entre 12 e 17 (imprimir boa tarde)
# hora 18 até as 23 (imprimir boa noite)
# hora entre 23 e 5 (imprimir boa madrugada)
'''
hora = int(input("Que horas sao? "))

if hora >= 6 and hora <= 11:
    print("Bom dia!")
elif hora >= 12 and hora <=17:
    print("Boa tarde!")
elif hora >=18 and hora <=23:
    print("Boa noite!")
else:
    print("Boa madrugada!")
'''
### ex002 ler tres notas e fazer a media
# SE A MÉDIA FOR MAIOR QUE 9 IMPRIMIR APROVADO COM LOUVOR
# SE A MÉDIA FOR MAIOR QUE 7 E MENOR QUE 9 IMPRIMIR APROVADO
# SE A MÉDIA FOR ENTRE 4 E 7 IMPRIMIR RECUPERAÇÃO
# SE A MÉDIA FOR MENOR QUE 4 REPROVADO DIRETO

'''
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
media = (n1 + n2 + n3)/ 3
if media >= 9:
    print("APROVADO COM LOUVOR")
elif media >=7 and media <9:
    print("APROVADO")
elif media >=4 and media <7:
    print("RECUPERAÇÂO")
else:
    print("REPROVADO!")

'''

### ex003 faca um programa que leia a altura e o peso de um uisuario e calcule o seu IMC
# IMC = peso / altura * altura
# IMC< 18.50 = magreza
# IMC = entre 18.5 e 24.9 = normal
# IMC = entre 25 e 29.9 = sobrepeso
# IMC = entre 30 e 39.9 = obesidade
# IMC = maior que 40 = obesidade morbida

'''
altura = float(input("Qual a sua altura? "))
peso = float(input("Qual o seu peso? "))
imc = peso/(altura**2)
print(imc)
if imc < 18.5:
    print("Magreza")
elif imc >= 18.5 and imc <25:
    print("Normal")
elif imc >= 25 and imc < 29.9:
    print("Sobrepeso")
elif imc >= 30 and imc < 39.9:
    print("Obesidade")
else:
    print("Obesidade Morbida")

'''

### ex004 - faca um programa que leia as medidas de um lado de um triangulo e de acordo com essas
#medidas informar se o triangulo é isoceles, equilatero ou escaleno
# EQUILATERO = todos os lados iguais
# ISOCELES =  dois lados iguals
# ESCALENO = todos os lados diferentes

x =  int(input("Digite o lado 'x' "))
y = int(input("Digite o lado 'y' "))
z = int(input("Digite o lado 'z' "))

if x == y and x == z:
    print("Triangulo EQUILATERO: todos os lados são iguais")
elif x != y and x != z and y != z:
  print("Triangulo ESCALENO: todos os lados diferentes")
else:
  print("Triangulo ISOCELES: dois lados iguais")































































