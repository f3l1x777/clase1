import random

# 1. Configuración inicial
numero_secreto = random.randint(1, 50)
vidas = 5  # <--- Aquí definimos las vidas que tendrá el jugador

print("¡Bienvenido al juego de adivinar el número con VIDAS!")
print("Estoy pensando en un número entre 1 y 50. Tienes 5 vidas para lograrlo.")

# 2. El bucle ahora corre mientras el jugador tenga vidas
while vidas > 0:
    print("\nTe quedan " + str(vidas) + " vidas.")
    intento = int(input("Introduce tu número: "))
    
    if intento == numero_secreto:
        print("¡Felicidades! Adivinaste el número secreto.")
        break  # Gana el juego y sale del bucle
        
    elif intento < numero_secreto:
        print("El número secreto es más GRANDE.")
        
    else:
        print("El número secreto es más PEQUEÑO.")
        
    # Si llegó aquí, falló el intento, así que le restamos una vida
    vidas = vidas - 1

# 3. Si el bucle termina y las vidas llegaron a 0, significa que perdió
if vidas == 0:
    print("\n☠️ ¡Game Over! Te has quedado sin vidas.")
    print("El número secreto era: " + str(numero_secreto))

