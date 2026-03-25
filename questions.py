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

puntaje = 0         #inicializacion de puntaje 

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
        puntaje += 6      #si el jugador adivina la palabra completa, se le suman 6 puntos.
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

    #Consigna 2: mostrar puntaje del jugador. Incorrecta resta 1, palabra completa suma 6, perder deja puntaje en cero.
    if letter in guessed:
        print ("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print ("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attemps -= 1
        puntaje -= 1        #resta 1 por cada letra incorrecta.
        print ("Esa letra no está en la palabra.")
    print()

else:
    print (f"¡Perdiste! La palabra era: {word}")
    puntaje = 0         #puntaje en cero si el jugador pierde.

#puntaje al final de la partida.
print (f"Tu puntaje final es: {puntaje}")