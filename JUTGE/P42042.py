vocales="aeiouAEIOU"

letra=input().strip()

if letra.isupper():
    print("uppercase")
else:
    print("lowercase")
if letra in vocales:
    print("vowel")
else:
    print("consonant")

