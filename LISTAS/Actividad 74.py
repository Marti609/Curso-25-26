#74. A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de entre las 2 listas.
lista1=["casa", "mesa", "sal", "sol", "agua"]
lista2=["casa", "luz", "tres", "tren", "sol", "pan"]

repetidas=set(lista1) & set(lista2) 
no_repetidas_lista1=set(lista1)-set(lista2)
no_repetidas_lista2=set(lista2)-set(lista1)
no_repetidas=[*no_repetidas_lista1, *no_repetidas_lista2]

if repetidas:
    print(f"Palabras repetidas en ambas listas: {repetidas}")

if no_repetidas_lista2:
    print(f"Palabras que no estan repetidas: {no_repetidas}")
