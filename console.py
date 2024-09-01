#!/usr/bin/python3
"""Defines the HBnB console"""


import cmd

class HBNBCommand(cmd.Cmd):
    """Simple command processor example for the HBNB project."""
    
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Overrides the default behavior to do nothing when an empty line is entered."""
        pass

    def default(self, line):
        """Handles unrecognized commands."""
        print(f"*** Unknown syntax: {line}")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
