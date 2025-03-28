import requests

def trivia_fetch(numero):
    respuesta = requests.get(f"http://numbersapi.com/{numero}?json")
    return respuesta.json()

def main():
    print("📚 ¡Bienvenido al Quiz de Trivia Numérica!")
    print("Escribe 'salir' para terminar el programa.\n")

    while True:
        entrada = input("Ingresa un número para conocer una trivia sobre él: ")

        if entrada.lower() == "salir":
            print("👋 ¡Gracias por jugar! Hasta la próxima.")
            break

        try:
            numero = int(entrada)
            trivia = trivia_fetch(numero)
            print(f"\n🧠 ¿Sabías que...? {trivia['text']}\n")
        except ValueError:
            print("❌ Por favor, ingresa un número válido o escribe 'salir' para terminar.\n")
        except Exception as e:
            print(f"⚠️ Ocurrió un error: {e}\n")

if __name__ == "__main__":
    main()