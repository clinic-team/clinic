from pyfiglet import figlet_format
from rich import print as rprint
from sys import argv
from typing import Callable

class CLI:
    def __init__(self, name: str):
        self.name = name
        self.commands = []
    def add(self, name: str, args: list, func: Callable):
        self.commands.append((name, args, func))
    def run(self):
        if argv[1] == "help":
            print(figlet_format(self.name))
            for command in self.commands:
                argstring = ""
                for arg in command[1]:
                    argstring += arg
                print(f"{command[0]} {argstring}")
        else:
            for command in self.commands:
                if argv[1] == command[0]:
                    command[2](*argv[2:])

if __name__ == "__main__":
    example = CLI("example")
    example.run()