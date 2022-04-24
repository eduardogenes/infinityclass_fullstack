

tempo = float(input("Quanto tempo de viagem em horas? "))
vel_media = float(input("Qual foi a velcidade media?"))

distancia = tempo * vel_media

litros_usados = distancia / 12

print("\nDADOS DA VIAGEM: ")
print(f"\nVelocidade media: {vel_media}km/h")

print(f"Tempo gasto: {tempo }h")

print(f"Distancia percorrida: {distancia}km")

print(f"Combustivel utilizado: {litros_usados}l")