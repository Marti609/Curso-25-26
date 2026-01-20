#73. Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se repiten y cuales no
lista1=["casa", "mesa", "sal", "sol", "agua"]
lista2=["casa", "luz", "tres", "tren", "sol", "pan"]

repetidas=set(lista1) & set(lista2) 
no_repetidas_lista2=set(lista2)-set(lista1)

if repetidas:
    print(f"Palabras repetidas en ambas listas: {repetidas}")

if no_repetidas_lista2:
    print(f"Palabras que no estan repetidas: {no_repetidas_lista2}")