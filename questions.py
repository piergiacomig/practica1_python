import random

#Consigna 3: se agrupan palabras por categorías. Al principio mostrar las disponibles y permitir elección al usuario. 
#diccionario: cada clave es una categoria y sus valores una lista de palabras. 
categorias = {
    "animales": ["perro", "gato", "elefante", "jirafa", "tigre"],
    "frutas": ["manzana", "banana", "naranja", "mandarina", "uva"],
    "paises": ["argentina", "brasil", "uruguay", "chile", "peru"]
}
print ("Bienvenido al Ahorcado!")
print()

#muestra las categorías disponibles.
print ("Categorías disponibles:")
for categoria in categorias:
    print (f"- {categoria}")
print()

#pedir al usuario que elija una, y se pasa a minúscula. 
categoria_elegida = input ("Elige una categoría: ").lower()
while categoria_elegida not in categorias:
    print ("Categoría no válida. Elegí una de las disponibles: animales, frutas o países.")
    categoria_elegida = input ("Elige una categoría: ").lower()

#Implementación de random.sample(), para que no se repitan las palabras por cada ronda.
cantidad_palabras = len(categorias[categoria_elegida])     #se obtiene la cantidad de palabras disponibles en la categoría elegida.
palabras_mezcladas = random.sample(categorias[categoria_elegida], cantidad_palabras)     #se mezclan las palabras de la categoría elegida.
for word in palabras_mezcladas:     #cada vez que inicia una ronda.
    print()
    print (f"----NUEVA RONDA----")

    guessed = []
    attempts = 6
    puntaje = 0         #inicializacion de puntaje 

    while attempts > 0:
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

        print (f"Intentos restantes: {attempts}")
        print (f"Letras usadas: {','.join(guessed)}")
        
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
            attempts -= 1
            puntaje -= 1        #resta 1 por cada letra incorrecta.
            print ("Esa letra no está en la palabra.")
        print()

    else:
      print (f"¡Perdiste! La palabra era: {word}")
      puntaje = 0         #puntaje en cero si el jugador pierde.

    #puntaje al final de la ronda.
    print (f"Tu puntaje de esta ronda es: {puntaje}")