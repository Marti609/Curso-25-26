import random
import time
tiempo = time.time()
historial_ganadas = []
historial_perdidas = []
lista_palabras = ["python", "programacion", "ahorcado", "desarrollo", "inteligencia", "computadora", "juego", "palabra", "adivinar", "letra"]
intentos = 8
aciertos = []
fallos = []
print("¡Bienvenido al juego del Ahorcado! Tienes 8 intentos para adivinar la palabra oculta.")
time.sleep(8)
palabra = random.choice(lista_palabras)
tablero = ""
for letra in palabra:       
        if letra in aciertos:
            tablero += letra + " "
        else:
            tablero += "_ "
        tablero.strip()
while intentos > 0:
    print(f"{intentos} intentos restantes")
    print(tablero)
    letra = input("Adivina una letra: ").lower()
    if letra in aciertos:
        print("Ya has adivinado esa letra. Intenta con otra.")
        fallos.append(letra)
        continue
    if letra in palabra:
        print("¡Correcto!")
        aciertos.append(letra)
        tablero = ""
        for letra_palabra in palabra:
            if letra_palabra in aciertos:
                tablero += letra_palabra + " "
            else:
                tablero += "_ "
    else:
        print("¡Incorrecto!")
        fallos.append(letra)
        intentos -= 1
    if all(letra in aciertos for letra in palabra):
        print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
        print(f"Fallos: {fallos}")
        print(f"Aciertos: {aciertos}")
        historial_ganadas.append(palabra)
        fin = time.time()  
        print(f"Tiempo transcurrido: {fin - tiempo:.2f} segundos")
        break
else:
    print(f"Fallos: {fallos}")
    print(f"Aciertos: {aciertos}")
    print(f"Has perdido. La palabra era: {palabra}")
    historial_perdidas.append(palabra)
    fin = time.time()  
    print(f"Tiempo transcurrido: {fin - tiempo:.2f} segundos")

respuesta_historial = input("Antes de preguntarte si quieres jugar otra partida. ¿Quieres ver tu historial de partidas s/n? ")
respuesta_historial_buena = respuesta_historial.lower()
if respuesta_historial_buena == "s":
    print(F"Palabras acertadas: {historial_ganadas}")
    print(f"Palabras perdidas: {historial_perdidas}")

respuesta = input("Quieres jugar otra partida s/n? ")
respuesta_buena = respuesta.lower()

if respuesta_buena == "s":
    while respuesta_buena == "s":
        juego_complicado = input("¿Quieres jugar una partida complicada? s/n ")
        juego_complicado_bueno = juego_complicado.lower()
        if juego_complicado_bueno == "s":
            tiempo = time.time()
            lista_palabras = ["python", "programacion", "ahorcado", "desarrollo", "inteligencia", "computadora", "juego", "palabra", "adivinar", "letra"]
            intentos = 4
            aciertos = []
            fallos = []
            palabra = random.choice(lista_palabras)
            print("¡Has elegido la partida complicada! Tienes 4 intentos para adivinar la palabra oculta.")
            tablero = ""
            for letra in palabra:       
                    if letra in aciertos:
                        tablero += letra + " "
                    else:
                        tablero += "_ "
                    tablero.strip()
            while intentos > 0:
                print(f"{intentos} intentos restantes")
                print(tablero)
                letra = input("Adivina una letra: ").lower()
                if letra in aciertos:
                    print("Ya has adivinado esa letra. Intenta con otra.")
                    fallos.append(letra)
                    continue
                if letra in palabra:
                    print("¡Correcto!")
                    aciertos.append(letra)
                    tablero = ""
                    for letra_palabra in palabra:
                        if letra_palabra in aciertos:
                            tablero += letra_palabra + " "
                        else:
                            tablero += "_ "
                else:
                    print("¡Incorrecto!")
                    fallos.append(letra)
                    intentos -= 1
                if all(letra in aciertos for letra in palabra):
                    print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
                    print(f"Fallos: {fallos}")
                    print(f"Aciertos: {aciertos}")
                    historial_ganadas.append(palabra)
                    fin = time.time()  
                    print(f"Tiempo transcurrido: {fin - tiempo:.2f} segundos")
                    break
            else:
                print(f"Fallos: {fallos}")
                print(f"Aciertos: {aciertos}")
                print(f"Has perdido. La palabra era: {palabra}")
                historial_perdidas.append(palabra)
                fin = time.time()  
                print(f"Tiempo transcurrido: {fin - tiempo:.2f} segundos")
            respuesta_historial = input("Antes de preguntarte si quieres jugar otra partida. ¿Quieres ver tu historial de partidas s/n? ")
            respuesta_historial_buena = respuesta_historial.lower()
            if respuesta_historial_buena == "s":
                print(F"Palabras acertadas: {historial_ganadas}")
                print(f"Palabras perdidas: {historial_perdidas}")
            else:
                continue
            respuesta = input("Quieres jugar otra partida s/n? ")
            respuesta_buena = respuesta.lower()

        elif juego_complicado_bueno == "n":    
            tiempo = time.time()
            lista_palabras = ["python", "programacion", "ahorcado", "desarrollo", "inteligencia", "computadora", "juego", "palabra", "adivinar", "letra"]
            intentos = 8
            aciertos = []
            fallos = []
            palabra = random.choice(lista_palabras)
            tablero = ""
            for letra in palabra:       
                    if letra in aciertos:
                        tablero += letra + " "
                    else:
                        tablero += "_ "
                    tablero.strip()
            while intentos > 0:
                print(f"{intentos} intentos restantes")
                print(tablero)
                letra = input("Adivina una letra: ").lower()
                if letra in aciertos:
                    print("Ya has adivinado esa letra. Intenta con otra.")
                    fallos.append(letra)
                    continue
                if letra in palabra:
                    print("¡Correcto!")
                    aciertos.append(letra)
                    tablero = ""
                    for letra_palabra in palabra:
                        if letra_palabra in aciertos:
                            tablero += letra_palabra + " "
                        else:
                            tablero += "_ "
                else:
                    print("¡Incorrecto!")
                    fallos.append(letra)
                    intentos -= 1
                if all(letra in aciertos for letra in palabra):
                    print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
                    print(f"Fallos: {fallos}")
                    print(f"Aciertos: {aciertos}")
                    historial_ganadas.append(palabra)
                    fin = time.time()  
                    print(f"Tiempo transcurrido: {fin - tiempo:.2f} segundos")
                    break
            else:
                print(f"Fallos: {fallos}")
                print(f"Aciertos: {aciertos}")
                print(f"Has perdido. La palabra era: {palabra}")
                historial_perdidas.append(palabra)
                fin = time.time()  
                print(f"Tiempo transcurrido: {fin - tiempo:.2f} segundos")
            respuesta_historial = input("Antes de preguntarte si quieres jugar otra partida. ¿Quieres ver tu historial de partidas s/n? ")
            respuesta_historial_buena = respuesta_historial.lower()
            if respuesta_historial_buena == "s":
                print(F"Palabras acertadas: {historial_ganadas}")
                print(f"Palabras perdidas: {historial_perdidas}")
            else:
                continue
            respuesta = input("Quieres jugar otra partida s/n? ")
            respuesta_buena = respuesta.lower()

print("¡Hasta la proxima!")

        