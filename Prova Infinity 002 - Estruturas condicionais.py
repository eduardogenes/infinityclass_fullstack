
#ESTRUTURAS CONDICIONAIS
'''
[LP-A02] Crie um algoritmo que recebe como entrada o dia e o mês de nascimento e retorna o signo, seguindo as faixas de valores informados:
- Áries: de 21 março a 20 abril;
- Touro: de 21 abril a 20 maio;
- Gêmeos: de 21 maio a 20 junho;
- Câncer: de 21 junho a 22 julho;
- Leão: de 23 julho a 22 agosto;
- Virgem: de 23 agosto a 22 setembro;
- Libra: de 23 setembro a 22 outubro;
- Escorpião: de 23 outubro a 21 novembro;
- Sagitário: de 22 novembro a 21 dezembro;
- Capricórnio: de 22 dezembro a 20 janeiro;
- Aquário: de 21 janeiro a 18 fevereiro;
- Peixes: de 19 fevereiro a 20 março.
'''

dia = int(input("Informe o dia em que voce nasceu (1 a 31):  "))
mes = int(input("Informe o mes em que voce nasceu (1 a 31): "))

if (dia >= 21 and dia <=31 and mes == 3) or (dia >= 1 and dia <= 20 and mes == 4):
    print("Seu signo é de Aries")
elif (dia >= 21 and dia <=30 and mes == 4) or (dia >= 1 and dia <= 20 and mes == 5):
    print("Seu signo é de Touro")
elif (dia >= 21 and dia <=31 and mes == 5) or (dia >= 1 and dia <= 20 and mes == 6):
    print("Seu signo é de Gemeos")
elif (dia >= 21 and dia <=30 and mes == 6) or (dia >= 1 and dia <= 22 and mes == 7):
    print("Seu signo é de Cancer")
elif (dia >= 23 and dia <=31 and mes == 7) or (dia >= 1 and dia <= 22 and mes == 8):
    print("Seu signo é de Leão")
elif (dia >= 23 and dia <=31 and mes == 8) or (dia >= 1 and dia <= 22 and mes == 9):
    print("Seu signo é de Virgem")
elif (dia >= 23 and dia <=30 and mes == 9) or (dia >= 1 and dia <= 22 and mes == 10):
    print("Seu signo é de Libra")
elif (dia >= 23 and dia <=31 and mes == 10) or (dia >= 1 and dia <= 21 and mes == 11):
    print("Seu signo é de Escorpião")
elif (dia >= 22 and dia <=30 and mes == 11) or (dia >= 1 and dia <= 21 and mes == 12):
    print("Seu signo é de Sagitário")
elif (dia >= 22 and dia <=31 and mes == 12) or (dia >= 1 and dia <= 20 and mes == 1):
    print("Seu signo é de Capricórnio")
elif (dia >= 21 and dia <=31 and mes == 1) or (dia >= 1 and dia <= 18 and mes == 2):
    print("Seu signo é de Aquário")
elif (dia >= 19 and dia <=28 and mes == 2) or (dia >= 1 and dia <= 20 and mes == 3):
    print("Seu signo é de Peixes")
else:
    print("Voce digitou dados incorretos")
