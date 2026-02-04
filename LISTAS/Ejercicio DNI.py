#Diseñar un programa que al introducir un número calcule la letra correspondiente, teniendo en cuenta los siguientes puntos:
letras=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]

dni_correctos=[]
dni_erroneos=[]
lista_intentos=[]

while True:
    dni=input("Introduce DNI (8 números): ")

    if len(dni)!=8:
        print("El valor introducido no cumple la longitud correcta")
        dni_erroneos.append(dni)
        lista_intentos.append(0)

    elif not dni.isdigit():
        print("El valor introducido debe ser numérico")
        dni_erroneos.append(dni)
        lista_intentos.append(1)

    else:
        numero=int(dni)
        resto=numero%23

        if resto not in range(len(letras)):
            print("DNI no válido, el resto no existe")
            dni_erroneos.append(dni)
            lista_intentos.append(2)
        else:
            letra=letras[resto]
            nif=dni+"-"+letra
            print(f"NIF correcto: {nif}")
            dni_correctos.append(nif)
            lista_intentos.append(3)

    continuar=input("¿Deseas continuar? (s/n): ").lower()
    if continuar=="n":
        break
#MENÚ
while True:
    print("\nMENÚ")
    print("1. Listar DNI correctos ordenados de menor a mayor")
    print("2. Listar DNI incorrectos ordenados de menor a mayor")
    print("3. Número total de errores producidos")
    print("4. Número total de DNI correctos")
    print("5. Porcentajes de intentos con error y sin error")
    print("6. Salir")

    opcion=input("Elige una opción: ")

    if opcion=="1":
        print(sorted(dni_correctos))

    elif opcion=="2":
        print(sorted(dni_erroneos))

    elif opcion=="3":
        errores=lista_intentos.count(0)+lista_intentos.count(1)+lista_intentos.count(2)
        print(f"Total de errores: {errores}")

    elif opcion=="4":
        print(f"Total de DNIs correctos: {lista_intentos.count(3)}")

    elif opcion=="5":
        total=len(lista_intentos)

        if total==0:
            print("No hay intentos")
        else:
            print(f"Número de intentos: {total}")
            print("% DNIs correctos:", lista_intentos.count(3) * 100 / total)
            print("% Error longitud:", lista_intentos.count(0) * 100 / total)
            print("% Error no numérico:", lista_intentos.count(1) * 100 / total)
            print("% DNI inexistentes:", lista_intentos.count(2) * 100 / total)

    elif opcion=="6":
        print("Fin del programa")
        break
    else:
        print("Opción incorrecta")