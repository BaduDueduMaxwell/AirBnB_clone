#!/usr/bin/python3
"""
Console for AirBnB project
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import shlex

class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB"""
    prompt = "(hbnb) "
    file_storage = FileStorage()

    def __init__(self, *args, **kwargs):
        """Initialize command interpreter"""
        super().__init__(*args, **kwargs)
        self.storage = HBNBCommand.file_storage
        self.storage.reload()

    def do_create(self, arg):
        """Create a new instance of a class"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.storage.classes():
            print("** class doesn't exist **")
            return
        cls = self.storage.classes()[args[0]]
        new_instance = cls()
        for i in range(1, len(args), 2):
            if i + 1 < len(args):
                setattr(new_instance, args[i], args[i + 1].strip('"'))
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show an instance of a class"""
        args = shlex.split(arg)
        if len(args) < 2:
            print("** class name or id missing **")
            return
        if args[0] not in self.storage.classes():
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in self.storage.all():
            print("** no instance found **")
            return
        print(self.storage.all()[key])

    def do_destroy(self, arg):
        """Destroy an instance of a class"""
        args = shlex.split(arg)
        if len(args) < 2:
            print("** class name or id missing **")
            return
        if args[0] not in self.storage.classes():
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in self.storage.all():
            print("** no instance found **")
            return
        del self.storage.all()[key]
        self.storage.save()

    def do_update(self, arg):
        """Update an instance of a class"""
        args = shlex.split(arg)
        if len(args) < 4:
            print("** class name, id, or attribute missing **")
            return
        if args[0] not in self.storage.classes():
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in self.storage.all():
            print("** no instance found **")
            return
        setattr(self.storage.all()[key], args[2], args[3].strip('"'))
        self.storage.all()[key].save()

    def do_all(self, arg):
        """Show all instances of a class"""
        args = shlex.split(arg)
        if args and args[0] not in self.storage.classes():
            print("** class doesn't exist **")
            return
        if args:
            instances = [str(value) for key, value in self.storage.all().items() if key.startswith(args[0])]
        else:
            instances = [str(value) for key, value in self.storage.all().items()]
        print(instances)

    def do_count(self, arg):
        """Count the number of instances of a class"""
        args = shlex.split(arg)
        if not args or args[0] not in self.storage.classes():
            print("** class doesn't exist **")
            return
        count = sum(1 for key in self.storage.all().keys() if key.startswith(args[0]))
        print(count)

    def do_quit(self, arg):
        """Quit the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Exit on End Of File"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
