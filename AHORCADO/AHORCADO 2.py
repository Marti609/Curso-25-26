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
if __name__ == "__main__":    main()                
           