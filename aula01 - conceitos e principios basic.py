
# 795.720.350-70
'''
print('795', end='.')
print('720', end='.')
print('350', end='-')
print('70')


print("795", "720", "350", sep = ".", end="-")
print("70")

'''

########################################
'''
srting   - <str>  - qlqr valor dento de aspas (duplas oouy simples)
inteiro - <int>   - valores que sao inteiros, com ou sem sinal. 
float   - <float> - numeros quebrados, com ponto flutuante
boolean - <bool>  - true ou false
'''
'''
print("Infinity", type("infinity")) #funcao para descobrir a classe
print(0.26, type(0.26))
print(5, type(5))
print(10==10, type(10==10))

'''
'''
variaveis - espaco reservado na memoria para armazenar processos especificos

como criar uma variavel:
1 nome da variavel
2 operador de atribuicao =
3 valor que ela ira poossuir
'''
'''
nome = "infinity school"
quantidade_de_alunos = 28
altura_media = 1.73
resultado = True

print("Ola, somos a", nome, "Temos", quantidade_de_alunos, "alunos")
'''
'''
nome = "Eduardo"
i = 26
c = "full stack"

print("Ola, meu nome é {}, tenho {} e faço o curso de {}.".format(nome, i, c))
#ou
print(f"Ola, meu nome é {nome}, tenho {i} e faço o curso de {c}.")
'''
#####################################

'''
operadores aritimeticos e entrada de dados


# +   adicao
# -   subtração
# *   multiplicação
# /   divisao
# **  
# %   modulo (ou resto) da divisao
# //  divisao inteira (semo resto)
# ()  precede todas as operações

incrementos: 
+=
-=
/=
*=
%=

## ex: 

operdadores relacionais

!= diferente 
== igual
>  maior
>= maior ou igual
<  menor
<= menor ou igual

 ---> resultado em bolean (true or false)
 
'''

a = float(input("Qual a sua altura? "))
p = float(input("Qual o seu peso? "))
imc = p/a**2
print("Seu IMC é ", imc)
'''

l = float(input("Quanto mede o lado? "))
a = l**2
print("A aréa do quadrado é: ", a)
'''
































