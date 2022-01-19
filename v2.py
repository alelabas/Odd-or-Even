"""
PROBLEMAS A SOLUCIONAR
1. El juego no termina
2. El usuario puede apostar mas canicas de las que tiene
3. Compresion dificil

ACTUALIZACIONES:
1. Introduccion de la funcion filtrar_numero que hace que el codigo sea reutilizable y mas optimo

OBSERVACIONES:
1. Podria separar el if else que define quien acerto y armar una funcion aparte
2. Se podria cambiar la resta o suma de canicas creando una funcion aparte
"""

import random


bolitas_jugador = 10
bolitas_ia = 10

def filtrar_numero(eleccion):
    #Filtramos esa eleccion dividiendo por modulo. Si el resultado es igual a 0 significa que el numero es par.
    #Caso contrario damos por hecho que es impar
    if (eleccion % 2 == 0):
        eleccion_filtrada = "P"
    else:
        eleccion_filtrada = "I"
    return eleccion_filtrada


def turno_random(bolitas_jugador, bolitas_ia):
    print("Turno del jugador random: \n")

    #El jugador random elige un numero random de canicas para apostar
    eleccion_ia = random.randint(1, 10)
    
    #Se filtra la eleccion random
    eleccion_ia_filtrada = filtrar_numero(eleccion_ia)

    apuesta_jugador = None
    eleccion_jugador = None

    print("El jugador 1 ya ha apostado sus canicas. Apuesta tus canicas.\n")
    
    apuesta_jugador = int(input("Actualmente tienes {} canicas. > ".format(bolitas_jugador)))
    while eleccion_jugador != "P" and eleccion_jugador != "I":
        eleccion_jugador = input("Muy bien. Apostaste {} canicas. Ahora el rival tiene un numero par o impar? [P / I] > ".format(apuesta_jugador))
    
    #Comparar las elecciones de cada jugador para determinar el ganador

    if eleccion_jugador == eleccion_ia_filtrada:
        print("Acertaste. Como apostaste {} canicas, se las sacas a tu rival".format(apuesta_jugador))

        bolitas_ia = bolitas_ia - apuesta_jugador
        bolitas_jugador = bolitas_jugador + apuesta_jugador

        print(f"Canicas Jugador random: {bolitas_ia}\nCanicas Jugador 1: {bolitas_jugador}\n")
        print("Ahora es tu turno\n")

        turno_jugador(bolitas_jugador, bolitas_ia)

    else:
        print(f"No acertaste. El jugador random tenia un numero {eleccion_ia_filtrada} de canicas\n")
        print("Como el jugador random aposto {} canicas, pierdes esa cantidad".format(eleccion_ia))

        bolitas_jugador = bolitas_jugador - eleccion_ia
        bolitas_ia = bolitas_ia + eleccion_ia

        print(f"Canicas jugador random: {bolitas_ia}\nCanicas jugador 1: {bolitas_jugador}")
        print("Ahora es tu turno\n")

        turno_jugador(bolitas_jugador, bolitas_ia)
    

def turno_jugador(bolitas_jugador, bolitas_ia):
    print("Tu turno:\n")
    print("Elige la cantidad de canicas a apostar\n")
    apuesta_del_jugador = int(input("Actualmente tienes {} canicas. > ".format(bolitas_jugador)))

    filtrar_jugador = filtrar_numero(apuesta_del_jugador)

    #Apuesta del jugador random
    opciones = ["P", "I"]
    apuesta_random = random.randint(1, 10)
    adivinanza_random = random.choice(opciones)
    
    if adivinanza_random == filtrar_jugador:
        print("El jugador random acerto. Su apuesta fue de {} canicas. Se te restan del inventario".format(apuesta_random))
        
        bolitas_jugador = bolitas_jugador - apuesta_random
        bolitas_ia = bolitas_ia + apuesta_random

        print(f"Canicas Jugador random: {bolitas_ia}\nCanicas jugador 1: {bolitas_jugador}\n")
        turno_random(bolitas_jugador, bolitas_ia)
    else:
        print("El jugador random no acerto. Como tu apuesta fue de {} canicas se te suman a tu inventario".format(apuesta_del_jugador))

        bolitas_jugador = bolitas_jugador + apuesta_del_jugador
        bolitas_ia = bolitas_ia - apuesta_del_jugador

        print(f"Canicas Jugador random: {bolitas_ia}\nCanicas jugador 1: {bolitas_jugador}\n")
        turno_random(bolitas_jugador, bolitas_ia)


def main():
    print("Bienvenido al juego Par o Impar")
    #Se elige un orden aleatorio para empezar el juego
    while bolitas_jugador or bolitas_ia != 0:
        orden = random.randint(1, 2)

        if orden == 1:
            turno_random(bolitas_jugador, bolitas_ia)
            
        else:
            turno_jugador(bolitas_jugador, bolitas_ia)
         

#if __name__ == "__main__":
#    main()