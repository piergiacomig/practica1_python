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
    
    #Primera consigna: se pretende corregir el bug. 
    #Si el usuario ingresa algo incorrecto, se le muestra el mensaje "Entrada no válida. " 
    letter = input ("Ingresa una letra: ").lower()
    if len(letter) != 1 or not letter.isalpha():    #si la extensión de la letra es diferente a 1 o si no es una letra del alfabeto, se muestra el mensaje. 
        print ("Entrada no válida. Por favor, ingresa solo una letra.")
        continue        #con el continue, el usuario no pierde intentos, sino que se le pide que reigrese una letra válida.
    
    #va a continuar solamente si la entrada es una letra del abecedario.
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