#Diseñar un programa que al introducir un número calcule la letra correspondiente, teniendo en cuenta los siguientes puntos:

dni=input("Introduce tu DNI: ")
letras=["T","R","w","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
dni_correctos=[]
dni_erroneos=[]
intentos=[]

while True:
    dni=input("Introduce DNI (8 números): ")

    # Control longitud y numérico

    if len(dni)!=8 or not dni.isdigit():
        print("DNI incorrecto")
        dni_erroneos.append(dni)
        intentos.append(0)
    else:
        numero=int(dni)
        resto=numero%23

    # Control resto válido

    if resto>=len(letras):
        print("Error: resto no válido")
        dni_erroneos.append(dni)
        intentos.append(1)
    else:
        letra=letras[resto]
        nif=dni+"-"+letra
        print("NIF:", nif)
        dni_correctos.append(nif)
        intentos.append(2)

    continuar=input("¿Deseas continuar s/n?: ").lower()

    if continuar=="n":
        break


print("\n--- MENÚ ---")
print("1. DNIs correctos")
print("2. DNIs erróneos")
print("3. Código de intentos")
print("4. Salir")

opcion=input("Elige opción: ")

if opcion=="1":
    print("Correctos:", dni_correctos)
elif opcion=="2":
    print("Erróneos:", dni_erroneos)
elif opcion=="3":
    print("Intentos:", intentos)
else:
    print("Fin del programa")
    