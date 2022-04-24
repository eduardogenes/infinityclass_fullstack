


### LISTAS ####
'''
lista_vazia = []

print(f"lista vaziua: {lista_vazia}")
print(f"Tipo da lista: {type(lista_vazia)}")

'''

"""
lista_inteiros = [1, 5, 6, 9, 10, 33, 22, 5]

print(f"lista inteiros: {lista_inteiros}")
"""

"""
lista_tipos_diferentes = ["infinity", 10, -5, 5.3, True, False]

print(f"lista inteiros: {lista_tipos_diferentes}")

"""

# Utilizando função


"""
lista = [26, 1995, "setembro"]

def exibirLista (lst):
    print(f"Exibir a lista {lst}")


exibirLista(lista)

"""
# cria uma lista com 3 variaveis e imprima

"""
mes = 'setembro'
ano = 9
dia = 26
signo = "libra"

aniver = [dia, mes, ano, signo]

def mapa (aniversario):
    print(aniversario)

mapa(aniver)
"""

## mudando o valor de uma variavel da lista usando 'indice'. comeca a partir de zero. e, se quiser
# contar regredindo, o ultimo é "-1"
'''
#               0               1          2

cursos = ['deve full stack', 'Python', 'fotoxopi']
#              -3                -2        -1         

cursos[2] = 'Photoshop'

print(f'Nossos cursos sao: {cursos}')
'''

# somando a lista utilizando indices
# ex: 1
'''
lista1 = [10, 50, 40, 25]
lista2 = [26, 9, 95]

def somar(lista1, lista2):
    print(f'o resultado da soma é {lista1[0] + lista2[-1]}')

somar(lista1, lista2)
'''
# ex professor:
'''
lista1 = [1, 6, 8, 9]
lista2 = [1, 20, 33, 91]


def somarListas(l1, l2):
    print(f'O resultado é: {l1[0] + l2[-1]}')

somarListas(lista1, lista2)

'''
# ex: 2

'''
lista = [1, 2, 6, 5, 8]

def somarLista(lista):
    print(f'Soma da lista: {lista[0] + lista[1] + lista[2] + lista[3] + lista[4]}')

somarLista(lista)
'''
# usando 'sum' para somar tudo da lista
'''
lista = [1, 2, 6, 5, 8]

def somarLista(lista):
    print(f'Soma da lista: {sum(lista)}')

somarLista(lista)
'''
# fateando a lista

"""

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista2 = lista[0:7:2] # [inicio:fim:passo]

print(f'Range: {list(range(0,20,3))}')
print(f'Lista 2: {lista2}')

"""
# concatenando (somando) listas ' + '
"""
l1 = [1, 0, 3]
print(l1)

l2 = [10, 16, 2]
print(l2)

l3 = l1 + l2
print(l3)
"""
# repetindo (multiplicando) a lista ' * '

"""
l1 = [1, 0, 3]
print('Lista l1: ', l1)

l2 = [10, 16, 2]
print('Lista l2:', l2)


l3 = [10,9,7] * 4
l4 = l1 + l2 
print('Lista l3: ', l3)
print('Lista l4: ', l4)
"""
# exercicio soma de lista utilizando return
# eu fiz:
'''
l1 = [1, 0, 3]
l2 = [10, 16, 2]

def somar(lista1, lista2):
    return(f"Concatenando as listas 1 e 2: {l1 + l2}")

soma = somar(l1, l2)
print(soma)
'''
# prof fez:
'''
lista = [1, 2, 3, 4]

def concatenar(x):
    return x + x

novaLista = concatenar(lista)

print(novaLista)
'''

# interação utiliozando o for:
'''
lista = [1, 2, 3, 4, 5]

for item in lista:
    print(f'O valor de item: {item}')

'''

#adicionando um item na lista utilizando ' append(item novo) '

"""
usuarios = ['zezim1337', 'paulimheadshot', 'mamute1337']

print('Lista: ', usuarios)

user = input('Insira o nome do novo usuário: ')

usuarios.append(user)

print(f'Lista atualizada: {usuarios}')

"""
# adicionando um item em uma posição especifica utilizando o ' insert(posição, item novo) '
"""
usuarios = ['zezim1337', 'paulimheadshot', 'mamute1337']

print('Lista: ', usuarios)

user = input('Insira o nome do novo usuário: ')

usuarios.append(user) # inserindo 'user' no final da lista 'usuarios'

print(f'Lista atualizada: {usuarios}')


novo_usuario = input('Informe o novo usuário: ')

usuarios.insert(1, novo_usuario) # Inserindo o novo_usuario no indice 1 da lista usuarios

print(f'Lista atualizada 2: {usuarios}')


"""
# inserir numa lista 5 nomes informado pelo usuario
# eu fazendo:
"""
lista = []

def inserir():
    for i in range(5):
        usuario = input(f"Digite o usuario: ")
        lista.append(usuario)
    return lista

listanova = inserir()

print(listanova)
"""
# prof fazendo

'''
def inserirNaLista():
    lista = []
    for i in range(5):
        var = input('Insira um valor: ')
        lista.append(var)
    print(f'Lista: {lista}')

inserirNaLista()
'''
# crie uma funcao que ira ler tres, armazene em uma lista e ê a media:
# eu fazendo
""" 
def inserir():
    lista = []
    for i in range(3):
        notas = float(input(f"Digite sua nota: "))
        lista.append(notas)
    return lista

lista = inserir()

soma = sum(lista)

print(f"\nSuas notas foram: {lista} \nSua média é: {soma/3:.1f}")
"""

# prof fazendo... utilizou a funcao ' len '
"""
def media():
    notas = []
    for i in range(3):
        n = float(input('Digite sua nota: '))
        notas.append(n)

    med = sum(notas) / len(notas)             #len conta quantos itens tem na lista
    print(f'Média: {med}' )

media()

"""
# apagando itens da lista. uliziando o ' .pop ' - apaga o ultimo ou o indice sinalizado/
# utilizando o del() - ap
'''
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista.pop()

del(lista[0:6:2])

print(lista)
'''

# utilizando o reverse, sort, max, min, remove, len

'''
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista.reverse()
print('Lista reversa: ',lista)

lista.sort()
print('Lista em ordem crescente:', lista)

print('Maior valor: ',max(lista))
print('Menor valor: ', min(lista))
print('Tamanho da lista: ', len(lista))
'''












