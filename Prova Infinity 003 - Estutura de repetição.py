
# [LP-A03] Escreva um programa que leia diversos números até que o usuário informe que deseja parar.
# Ao final do programa, informe a soma de todos os números e também a média.
soma = 0
i = 0

print("\n Informe suas notas, caso queira finalizar a contagem e ver a media, digite -1\n ")
while True:
    nota = float(input(" Digite sua nota: "))
    soma += nota
    i += 1
    if nota == -1:
        break

media = soma/(i-1)

print(f"\n\n A soma das suas notas é: {soma} \n Portando, sua média é: {media:.1f}")