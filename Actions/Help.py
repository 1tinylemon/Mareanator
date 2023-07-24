import random

def show_help(term=None):
    commands = {
        'spawn': 'Spawn elements in a random biome.',
        'help': 'Show available commands and descriptions.',
    }
    
    if term:
        if term in commands:
            print(f"{term}: {commands[term]}")
        else:
            print(f"Unknown term: {term}")
    else:
        print("==== Help ====")
        print("Commands:")
        for command, description in commands.items():
            print(f"- {command}: {description}")
