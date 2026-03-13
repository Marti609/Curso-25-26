palabras=input("introduce una cadena de texto: ")
palabra_buscada=input("introduce una palabra a buscar: ")
contador=0

lista=palabras.split(" ")
for i in lista:
    if i==palabra_buscada:
        contador+=1
print(f"La palabra '{palabra_buscada}' aparece {contador} veces en la cadena de texto.")
lista_final=",".join(lista)
print(lista_final)

