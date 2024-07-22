import random

def maquina():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

def determinar_ganador(jugador, maquina):
    if jugador == maquina:
        return "Empate"
    elif (jugador == "piedra" and maquina == "tijera") or \
         (jugador == "papel" and maquina == "piedra") or \
         (jugador == "tijera" and maquina == "papel"):
        return "Jugador"
    else:
        return "Maquina"
    

def juego():
    nombre_player = input("Ingresa tu nombre: ")
    print(f"Hola, {nombre_player}! Vamos a jugar a piedra, papel o tijera")
    
    victorias_player = 0
    victorias_maquina = 0
    rondas_jugadas = 0
    rondas_totales = 5
    
    while rondas_jugadas < rondas_totales and victorias_player < 3 and victorias_maquina < 3:
        jugada_maquina = maquina()
        jugada_player = input("Elige entre piedra, papel o tijera: ").lower()
        
        if jugada_player not in ["piedra", "papel", "tijera"]:
            print("Jugada inválida. Intenta de nuevo.")
            continue
        
        print(f"La computadora eligió: {jugada_maquina}")
        
        ganador = determinar_ganador(jugada_player, jugada_maquina)
        if ganador == "Jugador":
            victorias_player += 1
            print(f"{nombre_player} ha ganado esta ronda!")
        elif ganador == "Maquina":
            victorias_maquina += 1
            print("La computadora ha ganado esta ronda!")
        else:
            print("Es un empate!")
            
        rondas_jugadas += 1 
        print(f"Rondas restantes: {rondas_totales - rondas_jugadas}")
        print(f"Victorias de {nombre_player}: {victorias_player}, Victorias de la computadora: {victorias_maquina}")
        
    if victorias_player > victorias_maquina:
        print(f"¡{nombre_player} es el ganador!")
    elif victorias_maquina > victorias_player:
        print("¡La computadora es la ganadora!")
    else:
        print("Es un empate en el total de partidas!")

if __name__ == "__main__":
    juego()
