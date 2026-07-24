import os

print("=== 📝 MI GESTOR DE NOTAS ===\n")

# 1. Opción de menú
print("1. Leer mis notas")
print("2. Agregar nueva nota")
opcion = input("\nElige una opción (1 o 2): ")

if opcion == "1":
    # Comprobar si el archivo existe antes de leerlo
    if os.path.exists("notas.txt"):
        print("\n--- TUS NOTAS GUARDADAS ---")
        with open("notas.txt", "r") as archivo:
            contenido = archivo.read()
            print(contenido)
    else:
        print("\n⚠️ Aún no tienes notas guardadas.")

elif opcion == "2":
    nueva_nota = input("\nEscribe la nueva nota: ")
    
    # Abrir el archivo en modo "a" (append/añadir al final)
    with open("notas.txt", "a") as archivo:
        archivo.write("• " + nueva_nota + "\n")
        
    print("\n✅ ¡Nota guardada con éxito en 'notas.txt'!")

else:
    print("\n❌ Opción no válida.")

