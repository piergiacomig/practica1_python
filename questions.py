import random
words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]

word = random.choise (words)
guessed = []
attemps = 6

print ("Bienvenido al Ahorcado!")
print()

while attemps > 0:
    #Mostrar progreso: letras adividads y guiones para las que faltan
    progress =""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print (progress)
    #verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print ("¡Ganaste!")
        break

    print (f"Intentos restantes: {attemps})")
    print (f"Letras usadas: {','.jouin(guessed)}")
    
    letter = input ("Ingresa una letra:")
    
    if letter in guessed:
        print ("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print ("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attemps -= 1
        print ("Esa letra no está en la palabra.")
    print()

else:
    print (f"¡Perdiste! La palabra era: {word}")