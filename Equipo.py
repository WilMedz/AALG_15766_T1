import random

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partidosGanados = 0
        self.partidosPerdidos = 0
        self.setGanados = 0
        
equipo1 = Equipo("EQUIPO A")
equipo2 = Equipo("EQUIPO B")

def RegistraSet(nombre_equipo):
    if nombre_equipo == 1:
        equipo1.setGanados += 1
        print(equipo1.nombre, "Ganó un set... Sets ganados:", equipo1.setGanados)
        if equipo1.setGanados == 3:
            equipo1.partidosGanados += 1
            equipo2.partidosPerdidos += 1
            print(equipo1.nombre, "Gana el partido...")
            equipo1.setGanados = 0
            equipo2.setGanados = 0
    elif nombre_equipo == 2:
        equipo2.setGanados += 1
        print(equipo2.nombre, "Ganó un set... Sets ganados:", equipo2.setGanados)
        if equipo2.setGanados == 3:
            equipo2.partidosGanados += 1
            equipo1.partidosPerdidos += 1
            print(equipo2.nombre, "Gana el partido...")
            equipo1.setGanados = 0
            equipo2.setGanados = 0
            
def Puntos():
    return random.randint(10,28)
def PuntosEXtras():
    return random.randint(0,6)

def JugarPartido():
    while equipo1.setGanados<3 and equipo2.setGanados<3:
        puntos1=Puntos()
        puntos2=Puntos()
        print(equipo1.nombre, "tiene:", puntos1, "|", equipo2.nombre, "tiene:", puntos2)

        intentos = 0  
        while True:
            if puntos1 >= 25 and puntos1 > puntos2:
                RegistraSet(1)
                break
            elif puntos2 >= 25 and puntos2 > puntos1:
                RegistraSet(2)
                break
            else:
                extra1 = PuntosEXtras()
                extra2 = PuntosEXtras()
                puntos1 += extra1
                puntos2 += extra2
                print(f"{equipo1.nombre}: +{extra1} = {puntos1} | {equipo2.nombre}: +{extra2} = {puntos2}")
                intentos += 1
                if intentos >= 10:
                       if puntos1 > puntos2:
                        print("Empate prolongado. Se otorga el set a:", equipo1.nombre)
                        RegistraSet(1)
                elif puntos2 > puntos1:
                        print("Empate prolongado. Se otorga el set a:", equipo2.nombre)
                        RegistraSet(2)
                else:
                        ganador = random.choice([1, 2])
                        print("Empate total. Se elige ganador del set al azar.")
                        RegistraSet(ganador)
                break

def ResultadoTorneo():
    print("\n**Resultado**")
    print(equipo1.nombre, "Partidos ganados:", equipo1.partidosGanados, "Perdidos:", equipo1.partidosPerdidos)
    print(equipo2.nombre, "Partidos ganados:", equipo2.partidosGanados, "Perdidos:", equipo2.partidosPerdidos)

cantidad = int(input("Ingrese la cantidad de partidos a jugar (presione 0 para salir): "))
if cantidad == 0:
    print("No hay partidos.")
else:
    i = 1
    while i <= cantidad:
        print("\n*** Partido", i, "***")
        JugarPartido()
        i += 1
    ResultadoTorneo()
                  

                   