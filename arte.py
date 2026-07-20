from art import tprint, text2art

# 1. Imprimir un título gigante en la terminal
tprint("PYTHON", font="block")

# 2. Pedir al usuario su nombre y convertirlo en arte ASCII
nombre = input("Escribe tu nombre: ")
dibujo = text2art(nombre, font="alpha")

print("\n¡Mira tu nombre impreso estilo hacker:")
print(dibujo)

