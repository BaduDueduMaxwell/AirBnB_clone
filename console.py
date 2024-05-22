#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class defines the command interpreter for the HBNB project.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def help_quit(self):
        """
        Help message for the quit command
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        Exit the program
        """
        print("")
        return True

    def emptyline(self):
        """
        Do nothing on empty line
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
