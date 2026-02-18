import random
lista_palabras = ["python", "programacion", "ahorcado", "desarrollo", "inteligencia", "computadora", "juego", "palabra", "adivinar", "letra"]
lista_partidas = []
def elegir_palabra():
    palabra = random.choice(lista_palabras)
    return palabra

def mostrar_tablero(palabra, letras_adivinadas):
    tablero = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero.strip()

def jugar_ahorcado():
    palabra = elegir_palabra()
    letras_adivinadas = []
    lista_ahorcado = 6
    
    while lista_ahorcado > 0:
        print(mostrar_tablero(palabra, letras_adivinadas))
        print(f"Ahorcado: {lista_ahorcado} intentos restantes")
        letra = input("Adivina una letra: ").lower()
        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue
        letras_adivinadas.append(letra)
        if letra in palabra:
            print("¡Correcto!")
        else:
            print("¡Incorrecto!")
            lista_ahorcado -= 1
        if all(letra in letras_adivinadas for letra in palabra):
            print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
            return
    print(f"Has perdido. La palabra era: {palabra}")
def mostrar_aciertos_y_errores(palabra, letras_adivinadas):
    aciertos = len([letra for letra in letras_adivinadas if letra in palabra])
    errores = len([letra for letra in letras_adivinadas if letra not in palabra])
    print(f"Aciertos: {aciertos}")
    print(f"Errores: {errores}")

def mostrar_historial():
    if not lista_partidas:
        print("No hay partidas jugadas.")
    else:
        for partida in lista_partidas:
            print(partida)

def main():
    while mostrar_historial():  
        print("1. Jugar al Ahorcado")
        print("2. Ver historial de partidas")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            jugar_ahorcado()
            lista_partidas.append("Partida jugada")
        elif opcion == "2":
            mostrar_historial()
        elif opcion == "3":
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
           