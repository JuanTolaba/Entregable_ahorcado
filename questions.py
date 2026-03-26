import random

# Lista de palabras para el juego
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

# Elegir una palabra aleatoria de la lista
word = random.choice(words)
guessed = []  # Letras que el jugador ya adivinó
attempts = 6  # Número de intentos permitidos

print("¡Bienvenido al Ahorcado!")
print()

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)

    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        break

    # Mostrar intentos restantes y letras usadas
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    # Pedir al jugador que ingrese una letra y convertirla a minúscula
    letter = input("Ingresá una letra: ").lower()

    # Validar que la entrada sea una sola letra
    if len(letter) == 1 and letter.isalpha():
        if letter in guessed:
            # La letra ya fue adivinada anteriormente
            print("Ya usaste esa letra.")
        elif letter in word:
            # La letra está en la palabra
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            # La letra no está en la palabra
            guessed.append(letter)
            attempts -= 1  # Restar un intento
            print("Esa letra no está en la palabra.")
    else:
        # Entrada inválida: más de una letra, número o símbolo
        print("Entrada no válida")

    print()
else:
    # Si se terminaron los intentos, mostrar la palabra correcta
    print(f"¡Perdiste! La palabra era: {word}")
