import random

# Diccionario de categorías con listas de palabras
categories = {
    "Programación": ["python", "programa", "variable", "funcion", "bucle", "cadena", "entero", "lista"],
    "Animales": ["perro", "gato", "elefante", "jirafa", "tigre", "leon", "delfin", "caballo"],
    "Frutas": ["manzana", "banana", "naranja", "pera", "sandia", "kiwi", "uva", "mango"]
}

print("¡Bienvenido al Ahorcado con categorías!\n")

# Mostrar categorías disponibles
print("Categorías disponibles:")
for i, category in enumerate(categories.keys(), 1):
    print(f"{i}. {category}")

# Elegir categoría
while True:
    choice = input("\nElige una categoría escribiendo su nombre: ").strip()
    if choice in categories:
        word = random.choice(categories[choice])
        break
    else:
        print("Categoría no válida. Intenta nuevamente.")

guessed = []  # Letras que el jugador ya adivinó
attempts = 6  # Número de intentos permitidos
score = 0     # Puntaje del jugador

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print("\n" + progress)

    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        score += 6  # Sumar 6 puntos por ganar
        break

    # Mostrar intentos restantes y letras usadas
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    # Pedir al jugador que ingrese una letra
    letter = input("Ingresá una letra: ").lower()

    # Validar que la entrada sea una sola letra
    if len(letter) == 1 and letter.isalpha():
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1  # Restar un intento
            score -= 1     # Restar 1 punto por letra incorrecta
            print("Esa letra no está en la palabra.")
    else:
        print("Entrada no válida")

# Si se terminaron los intentos
if "_" in progress:
    print(f"\n¡Perdiste! La palabra era: {word}")
    score = 0

print(f"\nTu puntaje final es: {score}")
