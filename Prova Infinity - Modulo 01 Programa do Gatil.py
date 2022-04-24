

# Um gatil solicitou o desenvolvimento de um algoritmo que possa organizar os gatos em salas específicas de adoção.
# As regras para alocação dependem da idade, castração, sexo e FivFelv positivo (Aids do gato).

# Os gatos filhotes castrados, independentes de ser fêmea ou macho, ficam na sala A. Se for fêmea e não for castrada
# também pode ficar na sala A, contanto que não tenha FivFelv.

# Os gatos acima de 2 anos, são considerados adultos, portanto ficam na sala B, todos adultos são castrados. Os gatos
# não castrados machos ficam na sala C.

# Por último na sala D ficam os gatos que testaram positivo para FivFelv. com qualquer idade e todos machos. Fêmeas com
# FivFelv não são alocadas neste gatil, sendo direcionadas para outro.

sala_A = 0
sala_B = 0
sala_C = 0
sala_D = 0
outro_gatil = 0

for i in range(int(input("\nQuantos gatos serão analisados? "))):
    idade = int(input("Informe a idade do gato: "))
    castrado = input("Informe se o gato é castrado, escreva 'SIM' ou 'NAO': ")
    sexo = input("Informe se o gato é macho ou fêmea, escreva 'M' ou 'F': ")
    fivFelv = input("Informe se o gato é FivFelv positivo, escreva 'SIM' ou 'NAO': ")

if (idade <=2 and castrado == "SIM" and fivFelv == "NAO") or (idade <=2  and sexo == "F" and fivFelv == "NAO"):
    sala_A += 1
elif (idade > 2  and sexo == "F" and fivFelv == "NAO"):
    sala_B += 1
elif (castrado == "NAO" and sexo == "M" and fivFelv == "NAO"):
    sala_C += 1
elif (sexo == "M" and fivFelv == "SIM"):
    sala_D += 1
elif (sexo == "F" and fivFelv == "SIM"):
    outro_gatil += 1
else:
    print("Voce digitou algo errado. Repita a operação")

print("\nO gatil ficou organizado da seguinte forma: ")
print(f"\tSala A: {sala_A} gatos")
print(f"\tSala B: {sala_B} gatos")
print(f"\tSala C: {sala_C} gatos")
print(f"\tSala D: {sala_D} gatos")
print(f"Os {outro_gatil} gatos femeas com FivFelv Positivos, serão remanegados para outro gatil.")

