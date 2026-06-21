import random

# Opciones disponibles del juego
opciones = ["piedra", "papel", "tijera"]

# Bienvenida y nombre del usuario
print("=== PIEDRA, PAPEL O TIJERA ===")
nombre = input("Ingresa tu nombre: ")
print(f"¡Bienvenido {nombre}!")
# Pedir número de rondas
rondas = int(input("¿Cuántas rondas quieres jugar?: "))

# Mostrar reglas del juego
print("\n=== REGLAS DEL JUEGO ===")
print("- Piedra vence a Tijera")
print("- Tijera vence a Papel")
print("- Papel vence a Piedra")
print("========================\n")

# Preguntar si acepta jugar
aceptar = input("¿Aceptas jugar? (si/no): ").lower()
if aceptar != "si":
    print("¡Hasta luego!")
    # Marcador inicial
puntos_jugador = 0
puntos_computadora = 0
ronda_actual = 1

# Bucle de rondas
while ronda_actual <= rondas and aceptar == "si":
    print(f"\n=== RONDA {ronda_actual} de {rondas} ===")
    print(f"{nombre}: {puntos_jugador} puntos | Computadora: {puntos_computadora} puntos")
    
    # Jugador elige
    jugador = input("Elige: piedra, papel o tijera: ").lower()
    
    # Computadora elige aleatoriamente
    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")
    # Determinar ganador de la ronda
    if jugador == computadora:
        print("¡Empate en esta ronda!")
    elif jugador == "piedra" and computadora == "tijera":
        print("¡Ganaste esta ronda! Piedra vence a Tijera")
        puntos_jugador += 1
    elif jugador == "papel" and computadora == "piedra":
        print("¡Ganaste esta ronda! Papel vence a Piedra")
        puntos_jugador += 1
    elif jugador == "tijera" and computadora == "papel":
        print("¡Ganaste esta ronda! Tijera vence a Papel")
        puntos_jugador += 1
    else:
        print("¡Perdiste esta ronda! La computadora ganó")
        puntos_computadora += 1
    
    # Actualizar ronda
    ronda_actual += 1
    # Mostrar marcador final
print("\n=== RESULTADO FINAL ===")
print(f"{nombre}: {puntos_jugador} puntos")
print(f"Computadora: {puntos_computadora} puntos")

# Determinar ganador final
if puntos_jugador > puntos_computadora:
    print(f"\n¡Felicidades {nombre}, ganaste el juego!")
elif puntos_computadora > puntos_jugador:
    print("\n¡La computadora ganó el juego!")
else:
    print("\n¡El juego terminó en empate!")