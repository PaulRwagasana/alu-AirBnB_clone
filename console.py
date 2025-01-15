#!/usr/bin/python3
"""Command interpreter"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Command Interpreter Classes"""
    prompt = "(hbnb) "

    classes = [
        'BaseModel',
        'User',
        'Amenity',
        'City',
        'Review',
        'Place',
        'State',
    ]

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation
        of an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation
        of all instances based or not on the class name"""
        if arg and arg not in self.classes:
            print("** class doesn't exist **")
        else:
            objects = storage.all()
            if arg:
                objects = {
                    k: v for k, v in objects.items() if k.startswith(arg)
                    }
            print([str(obj) for obj in objects.values()])

    def do_update(self, arg):
        """Updates an instance based on the
        class name and id by adding or updating attribute"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                obj = storage.all()[key]
                attr_name = args[2]
                attr_value = args[3].strip('"')
                if hasattr(obj, attr_name):
                    attr_type = type(getattr(obj, attr_name))
                    setattr(obj, attr_name, attr_type(attr_value))
                else:
                    setattr(obj, attr_name, attr_value)
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
