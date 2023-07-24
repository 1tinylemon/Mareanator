import os
import random
import Actions.Spawn as Spawn
import Actions.Help as Help

state = "Start"

# Función para seleccionar un texto aleatorio de splash.txt
def splash():
    with open("splash.txt", "r") as file:
        lines = file.readlines()
        random_line = random.choice(lines)
        return random_line.strip()

# Función para comparar una respuesta con un texto y ejecutar la acción correspondiente
def compare(response, text, action):
    if response.lower() == text:
        action()
        return True
    return False

# Función principal que maneja la entrada del usuario y ejecuta los comandos
def main():
    initial_text = "Mareanator\n" + splash() + "\n-> "
    response = input(initial_text)

    while response.lower() not in ["exit", "q", "killme"]:
        if not compare(response, 'help', Help.show_help):
            compare(response, 'spawn', Spawn.naturalSpawn)
            compare(response, 'stfu', os.system("figlet que"))
        else:
            print('Unknown Command. Type "help" for help')

        response = input("-> ")

    print("Exiting...")

if __name__ == "__main__":
    main()
