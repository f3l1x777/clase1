import os

def mostrar_menu():
    print("\n==============================")
    print("      📝 GESTOR DE NOTAS      ")
    print("==============================")
    print("1. Ver todas las notas")
    print("2. Agregar una nota")
    print("3. Borrar todas las notas")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("\nElige una opción (1-4): ")

    if opcion == "1":
        if os.path.exists("notas.txt"):
            print("\n--- TUS NOTAS ---")
            with open("notas.txt", "r") as archivo:
                print(archivo.read())
        else:
            print("\n⚠️ No hay notas guardadas todavía.")

    elif opcion == "2":
        nota = input("\nEscribe tu nota: ")
        with open("notas.txt", "a") as archivo:
            archivo.write("• " + nota + "\n")
        print("✅ ¡Nota guardada!")

    elif opcion == "3":
        confirmar = input("\n¿Seguro que quieres borrar todo? (s/n): ")
        if confirmar.lower() == "s":
            if os.path.exists("notas.txt"):
                os.remove("notas.txt")
                print("🗑️ Todas las notas han sido borradas.")
            else:
                print("⚠️ No había archivo para borrar.")

    elif opcion == "4":
        print("\n¡Hasta luego! 🖐️")
        break  # Rompe el bucle y cierra el programa

    else:
        print("\n❌ Opción no válida. Intenta de nuevo.")

