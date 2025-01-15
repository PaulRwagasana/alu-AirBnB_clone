#!/usr/bin/python3
<<<<<<< HEAD
<<<<<<< HEAD
"""Command line interpreter"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """Class for the console, inheriting from cmd.Cmd"""
    prompt = '(hbnb) '

 def do_quit(self, arg):
        """Exit the program."""
        return True

def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl+D)."""
        return True

 def emptyline(self):
        """Do nothing on an empty line."""
        pass

def do_create(self, arg):
        """Create a new instance of BaseModel."""
        if not arg:
            print("** class name missing **")
            return
        try:
            instance = models.dict_classes[arg]()
            instance.save()
            print(instance.id)
        except KeyError:
            print("** class doesn't exist **")

  def do_show(self, arg):
        """Show the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models.dict_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance_key = f"{args[0]}.{args[1]}"
            obj = models.storage.all().get(instance_key)
            print(obj if obj else "** no instance found **")

def do_destroy(self, arg):
        """Delete an instance based on the class name and ID."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models.dict_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance_key = f"{args[0]}.{args[1]}"
            if instance_key in models.storage.all():
                del models.storage.all()[instance_key]
                models.storage.save()
            else:
                print("** no instance found **")

def do_all(self, arg):
        """Show all instances of a class (or all if no class is provided)."""
        args = arg.split()
        if not arg:
            for obj in models.storage.all().values():
                print(obj)
        elif args[0] not in models.dict_classes:
            print("** class doesn't exist **")
        else:
            for key, obj in models.storage.all().items():
                if key.startswith(args[0]):
                    print(obj)

 def do_update(self, arg):
        """Update an instance based on class name and ID."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models.dict_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            instance_key = f"{args[0]}.{args[1]}"
            obj = models.storage.all().get(instance_key)
            if obj:
                attr_name, attr_value = args[2], args[3].strip('"')
                try:
                    attr_value = eval(attr_value)  # Convert to correct type
                except (NameError, SyntaxError):
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()             
=======
"""
This module contains the entry point for the command interpreter.
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage
import inspect
import json
import sys


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter.

    commands:
    quit - exit the program
    EOF - exit the program
    """

    prompt = '(hbnb) '
    classes = {"Amenity": Amenity, "BaseModel": BaseModel,
               "City": City, "Place": Place, "Review": Review,
               "State": State, "User": User}

    def emptyline(self):
        """
        Overrides the default emptyline method to do nothing
        """
        pass

    def do_create(self, args):
        '''
        Creates and saves a new object
        ex: create BaseModel
        '''
        if not args:
            print("**class name missing**")
        elif args not in self.classes:
            print("**class doesn't exist**")
        else:
            new_instance = self.classes[args]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        '''
        Shows the dict representation of an object
        ex: show BaseModel 12345
        '''
        if not args:
            print("** class name missing **")
        else:
            args_list = args.split()
            if args_list[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args_list) < 2:
                print("** instance id missing **")
            else:
                key = args_list[0] + "." + args_list[1]
                all_objs = FileStorage().all()
                if key not in all_objs:
                    print("** no instance found **")
                else:
                    print(all_objs[key])

    def do_destroy(self, args):
        '''
        Deletes an object
        based on its class and id
        ex: destroy BaseModel 1234567
        '''
        if not args:
            print("** class name missing **")
        else:
            args_list = args.split()
            if args_list[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args_list) < 2:
                print("** instance id missing **")
            else:
                key = args_list[0] + "." + args_list[1]
                all_objs = FileStorage().all()
                if key not in all_objs:
                    print("** no instance found **")
                else:
                    del all_objs[key]
                    FileStorage().save()

    def do_all(self, args):
        '''
        Shows all objects in storage or all objects of a certain class
        ex: all
        or
        ex: all BaseModel
        '''
        all_objs = FileStorage().all()
        if not args:
            print([str(obj) for obj in all_objs.values()])
        elif args not in self.classes:
            print("** class doesn't exist **")
        else:
            class_objs = {k: v for k, v in all_objs.items() if args in k}
            print([str(obj) for obj in class_objs.values()])

    def do_update(self, args):
        """
        Update an object by add or updating an attribute
        ex: update BaseModel 1234-1234-1234 email "username@email.com"
        """
        if not args:
            print("** class name missing **")
        else:
            args_list = args.split()
            if args_list[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args_list) < 2:
                print("** instance id missing **")
            else:
                key = args_list[0] + "." + args_list[1]
                all_objs = FileStorage().all()
                if key not in all_objs:
                    print("** no instance found **")
                elif len(args_list) < 3:
                    print("** attribute name missing **")
                elif len(args_list) < 4:
                    print("** value missing **")
                else:
                    obj = all_objs[key]
                    setattr(obj, args_list[2], eval(args_list[3]))
                    obj.save()

    def do_count(self, args):
        """
        Return the number of instance of a class
        """
        if not args:
            print("** class name missing **")
        else:
            class_objs = {
                k: v for k,
                v in FileStorage().all().items() if args in k}
            print(len(class_objs))

    def do_quit(self, args):
        """
        Exit the program.
        """
        print("Goodbye!")
        return True

    def do_EOF(self, args):
        """
        (Ctrl+D or Ctrl+Z) EOF signal to exit the program
        """
        return True


=======
"""
This module contains the entry point for the command interpreter.
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage
import inspect
import json
import sys


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter.

    commands:
    quit - exit the program
    EOF - exit the program
    """

    prompt = '(hbnb) '
    classes = {"Amenity": Amenity, "BaseModel": BaseModel,
               "City": City, "Place": Place, "Review": Review,
               "State": State, "User": User}

    def emptyline(self):
        """
        Overrides the default emptyline method to do nothing
        """
        pass

    def do_create(self, args):
        '''
        Creates and saves a new object
        ex: create BaseModel
        '''
        if not args:
            print("**class name missing**")
        elif args not in self.classes:
            print("**class doesn't exist**")
        else:
            new_instance = self.classes[args]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        '''
        Shows the dict representation of an object
        ex: show BaseModel 12345
        '''
        if not args:
            print("** class name missing **")
        else:
            args_list = args.split()
            if args_list[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args_list) < 2:
                print("** instance id missing **")
            else:
                key = args_list[0] + "." + args_list[1]
                all_objs = FileStorage().all()
                if key not in all_objs:
                    print("** no instance found **")
                else:
                    print(all_objs[key])

    def do_destroy(self, args):
        '''
        Deletes an object
        based on its class and id
        ex: destroy BaseModel 1234567
        '''
        if not args:
            print("** class name missing **")
        else:
            args_list = args.split()
            if args_list[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args_list) < 2:
                print("** instance id missing **")
            else:
                key = args_list[0] + "." + args_list[1]
                all_objs = FileStorage().all()
                if key not in all_objs:
                    print("** no instance found **")
                else:
                    del all_objs[key]
                    FileStorage().save()

    def do_all(self, args):
        '''
        Shows all objects in storage or all objects of a certain class
        ex: all
        or
        ex: all BaseModel
        '''
        all_objs = FileStorage().all()
        if not args:
            print([str(obj) for obj in all_objs.values()])
        elif args not in self.classes:
            print("** class doesn't exist **")
        else:
            class_objs = {k: v for k, v in all_objs.items() if args in k}
            print([str(obj) for obj in class_objs.values()])

    def do_update(self, args):
        """
        Update an object by add or updating an attribute
        ex: update BaseModel 1234-1234-1234 email "username@email.com"
        """
        if not args:
            print("** class name missing **")
        else:
            args_list = args.split()
            if args_list[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args_list) < 2:
                print("** instance id missing **")
            else:
                key = args_list[0] + "." + args_list[1]
                all_objs = FileStorage().all()
                if key not in all_objs:
                    print("** no instance found **")
                elif len(args_list) < 3:
                    print("** attribute name missing **")
                elif len(args_list) < 4:
                    print("** value missing **")
                else:
                    obj = all_objs[key]
                    setattr(obj, args_list[2], eval(args_list[3]))
                    obj.save()

    def do_count(self, args):
        """
        Return the number of instance of a class
        """
        if not args:
            print("** class name missing **")
        else:
            class_objs = {
                k: v for k,
                v in FileStorage().all().items() if args in k}
            print(len(class_objs))

    def do_quit(self, args):
        """
        Exit the program.
        """
        print("Goodbye!")
        return True

    def do_EOF(self, args):
        """
        (Ctrl+D or Ctrl+Z) EOF signal to exit the program
        """
        return True


>>>>>>> parent of 20d09c6 (Update console.py)
if __name__ == '__main__':
    HBNBCommand().cmdloop()
>>>>>>> parent of 20d09c6 (Update console.py)
