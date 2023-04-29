"""
Escriba un programa que muestre una partida de dados entre dos jugadores, se debe ingresar la cantidad
 de turnos que se van a jugar, cada jugador tira un dado. Si un jugador saca un valor mayor que el otro,
  gana los puntos de ambos dados. Si los dos jugadores sacan el mismo valor, ninguno recibe puntos. Si en
el ultimo turno hay un empate, esos puntos se pierden y termina la partida. Debe mostrar quien gana la
partida, quien gana cada turno y la puntuación acumulada por cada jugador.

Para el examen pueden usar la librería random (import random) y utilizar el método random.randint(desde,
 hasta) que toma números enteros de forma aleatorias según rango dado.
"""
import random

turnos=int(input("Ingresa la cantidad de turnos: "))
contadorJugador1=0
contadorJugador2=0
for i in range(0,turnos):
    print("/////////////////////")
    print("turno ",i+1)
    print("///////////////////////")
    print("Lanza el jugador # 1")
    jugador1 = random.randint(1, 6)
    print("sacaste ", jugador1)
    print("///////////////////////")
    print("Lanza el jugador # 2")
    jugador2 = random.randint(1, 6)
    print("sacaste ", jugador2)
    print("/////////////////")
    if jugador1>jugador2:
        contadorJugador1=contadorJugador1+(jugador1+jugador2)
        print("/////////////////")
        print("Turno Ganado por el Jugador 1")

    elif jugador2>jugador1:
        contadorJugador2 = contadorJugador2 + (jugador1 + jugador2)
        print("Turno Ganado por el Jugador 2")

    else:print("Empate")
    print("jugador 1 llevas ",contadorJugador1," puntos.")
    print("jugador 2 llevas ", contadorJugador2, " puntos.")

ganador=""
mensaje=""
puntos=0

if contadorJugador1 > contadorJugador2:
    ganador="jugador 1"
    puntos=contadorJugador1
elif contadorJugador1 < contadorJugador2:
    ganador= "jugador 2"
    puntos=contadorJugador2
else:
    mensaje= "Empate"
print("///////////////////////////")
print("la partida la gana "+ganador)
print("Con ",puntos," puntos")




