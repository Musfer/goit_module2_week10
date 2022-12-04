import connect
import sys
from commands import commands, def_mod


if __name__ == "__main__":
    print("\nWelcome to your personal Python assistant!")
    print(f"Hello! What can I do for you today?")

    while True:
        command = input()
        mode, data = def_mod(command)
        output = commands.get(mode)(data)
        if output != '':
            print(output)
        if output == "Good bye!":
            sys.exit()
