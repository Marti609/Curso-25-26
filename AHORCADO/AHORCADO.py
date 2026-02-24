import random
import time
tiempo=time.time()
lista_palabras = ["python", "programacion", "ahorcado", "desarrollo", "inteligencia", "computadora", "juego", "palabra", "adivinar", "letra"]
lista_partidas = []
lista_ahorcado = 6
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
while lista_ahorcado > 0:
    print(f"{lista_ahorcado} intentos restantes")
    print(tablero)
    letra = input("Adivina una letra: ").lower()
    if letra in aciertos:
        print("Ya has adivinado esa letra. Intenta con otra.")
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
        lista_ahorcado -= 1
    if all(letra in aciertos for letra in palabra):
        print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
        print(f" Fallos: {fallos}")
        print(f"Aciertos: {aciertos}")

        break
else:
    print(f" Fallos: {fallos}")
    print(f"Aciertos: {aciertos}")
    print(f"Has perdido. La palabra era: {palabra}")

