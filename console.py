#!/usr/bin/python3
"""Defines the HBnB console"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage, classes
import sys

class HBNBCommand(cmd.Cmd):
    """Simple command processor example for the HBNB project."""
    
    prompt = '(hbnb) '

    def __init__(self, stdout=sys.stdout, stdin=sys.stdin):
        super().__init__(stdout=stdout, stdin=stdin)
        self.storage = FileStorage()
        self.storage.reload()
        self.classes = classes

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

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show the string representation of an instance."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in self.storage.all():
            print("** no instance found **")
            return
        print(self.storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in self.storage.all():
            print("** no instance found **")
            return
        del self.storage.all()[key]
        self.storage.save()

    def do_all(self, arg):
        """Prints all string representations of all instances."""
        args = arg.split()
        if len(args) == 0:
            print([str(obj) for obj in self.storage.all().values()])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in self.storage.all().items() if key.startswith(args[0])])

    def do_update(self, arg):
        """Updates an instance based on class name and id by adding or updating attribute."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in self.storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        obj = self.storage.all()[key]
        attr_name = args[2]
        attr_value = args[3].strip('"')
        
        # Update the attribute if it's not id, created_at, or updated_at
        if attr_name not in ['id', 'created_at', 'updated_at']:
            setattr(obj, attr_name, eval(attr_value))
            obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
