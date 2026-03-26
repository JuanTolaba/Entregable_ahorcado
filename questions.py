import random  

# Diccionario con categorías y sus palabras
categories = {
    "Programación": ["python", "programa", "variable", "funcion", "bucle", "cadena", "entero", "lista"],
    "Animales": ["perro", "gato", "elefante", "jirafa", "tigre", "leon", "delfin", "caballo"],
    "Frutas": ["manzana", "banana", "naranja", "pera", "sandia", "kiwi", "uva", "mango"]
}

print("¡Bienvenido al Ahorcado con categorías!\n")

# Mostrar las categorías disponibles
print("Categorías disponibles:")
for i, category in enumerate(categories.keys(), 1):
    print(f"{i}. {category}")

# Pedir al usuario que elija una categoría válida
while True:
    choice = input("\nElige una categoría escribiendo su nombre: ").strip()
    
    if choice in categories:
        #  Mezclamos las palabras SIN repetir usando random.sample
        shuffled_words = random.sample(categories[choice], len(categories[choice]))
        
        index = 0  # Índice para recorrer la lista de palabras
        break
    else:
        print("Categoría no válida. Intenta nuevamente.")

score = 0  # Puntaje total del jugador

# Bucle principal del juego (varias rondas)
while index < len(shuffled_words):

    # Elegimos la palabra actual según el índice
    word = shuffled_words[index]
    index += 1  # Pasamos a la siguiente palabra para la próxima ronda

    guessed = []   # Lista de letras ya usadas
    attempts = 6   # Intentos disponibles

    print("\n--- Nueva ronda ---")

    #  Bucle de una partida (adivinar una palabra)
    while attempts > 0:
        progress = ""

        # Construimos el progreso mostrando letras o guiones
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        
        print("\n" + progress)

        # Si no hay guiones, el jugador ganó
        if "_" not in progress:
            print("¡Ganaste!")
            score += 6  # Sumamos puntos por ganar
            break

        # Mostrar info al jugador
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        # Pedir una letra
        letter = input("Ingresá una letra: ").lower()

        # Validar que sea una sola letra
        if len(letter) == 1 and letter.isalpha():
            
            if letter in guessed:
                print("Ya usaste esa letra.")
            
            elif letter in word:
                guessed.append(letter)
                print("¡Bien! Esa letra está en la palabra.")
            
            else:
                guessed.append(letter)
                attempts -= 1   # Perdemos un intento
                score -= 1      # Restamos puntos por error
                print("Esa letra no está en la palabra.")
        
        else:
            print("Entrada no válida")

    # si no adivinó la palabra
    if "_" in progress:
        print(f"\n¡Perdiste! La palabra era: {word}")

    # Mostrar puntaje después de cada ronda
    print(f"Puntaje actual: {score}")

#  Cuando ya no quedan palabras
print("\nSe terminaron las palabras de la categoría.")
print(f"Tu puntaje final es: {score}")
