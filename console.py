#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


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

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        """
        if not arg:
            print("** class name missing **")
        elif arg not in globals():
            print("** class doesn't exist **")
        else:
            new_instance = globals()[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            obj_dict = storage.all()
            if key in obj_dict:
                print(obj_dict[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            obj_dict = storage.all()
            if key in obj_dict:
                del obj_dict[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        """
        obj_dict = storage.all()
        if not arg:
            print([str(obj_dict[key]) for key in obj_dict])
        elif arg not in globals():
            print("** class doesn't exist **")
        else:
            print([str(obj_dict[key]) for key in obj_dict if key.startswith(arg + '.')])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + '.' + args[1]
            obj_dict = storage.all()
            if key in obj_dict:
                instance = obj_dict[key]
                setattr(instance, args[2], args[3])
                instance.save()
            else:
                print("** no instance found **")

    # Additional methods for User class
    def do_create_user(self, arg):
        """
        Creates a new instance of User, saves it (to the JSON file) and prints the id.
        """
        new_user = User()
        new_user.save()
        print(new_user.id)

    def do_show_user(self, arg):
        """
        Prints the string representation of a User instance based on the user id.
        """
        args = arg.split()
        if not args:
            print("** user id missing **")
        else:
            user_id = args[0]
            obj_dict = storage.all()
            key = "User." + user_id
            if key in obj_dict:
                print(obj_dict[key])
            else:
                print("** no instance found **")

    def do_destroy_user(self, arg):
        """
        Deletes a User instance based on the user id (save the change into the JSON file).
        """
        args = arg.split()
        if not args:
            print("** user id missing **")
        else:
            user_id = args[0]
            obj_dict = storage.all()
            key = "User." + user_id
            if key in obj_dict:
                del obj_dict[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all_user(self, arg):
        """
        Prints all string representations of all User instances.
        """
        obj_dict = storage.all()
        user_instances = [str(obj_dict[key]) for key in obj_dict if key.startswith("User.")]
        print(user_instances)

    def do_update_user(self, arg):
        """
        Updates a User instance based on the user id by adding or updating an attribute.
        """
        args = arg.split()
        if not args:
            print("** user id missing **")
        elif len(args) < 2:
            print("** attribute name missing **")
        elif len(args) < 3:
            print("** value missing **")
        else:
            user_id = args[0]
            obj_dict = storage.all()
            key = "User." + user_id
            if key in obj_dict:
                user_instance = obj_dict[key]
                setattr(user_instance, args[1], args[2])
                user_instance.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
