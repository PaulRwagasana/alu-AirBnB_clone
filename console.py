#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""

import cmd
import models


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit the console.

        Usage:
            quit
            q
            exit
        """
        return True

    do_q = do_quit
    do_exit = do_quit

    def do_EOF(self, arg):
        """
        Quit the console.

        Usage:
            EOF
        """
        return True

    def emptyline(self):
        """
        An empty line + ENTER shouldn't execute anything
        """
        pass

    def do_create(self, arg):
        """
        Creates a new inst of BaseModel, saves it, and prints the id.
        """

        if not arg:
            print("** class name missing **")
            return
        if arg != "BaseModel":
            print("** class doesn't exist **")
            return
        obj = BaseModel()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """
        Displays the string representation of an instance using class name and id
        """

        args = arg.split(" ")
        if not args:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"BaseModel.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.

        Usage: destroy <class_name> <instance_id>

        Args:
            arg (str): Argument should contain <class_name> <instance_id>.
        """

    """Deletes an instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"BaseModel.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances.

        Usage:
            all
            all <class_name>

        Args:
            arg (str): The argument should contain <class_name>.
        """

         if arg and arg != "BaseModel":
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in storage.all().values()])

    def do_update(self, arg):
        """Updates an instance based on class name and id 
        by adding/updating attributes"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"BaseModel.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3]
        try:
            attr_value = eval(attr_value)
        except (NameError, SyntaxError):
            pass
        setattr(obj, attr_name, attr_value)
        obj.save()
    def remove_quotes(self, arg):
        """
        Removes the quotes from the argument.
        """
        rules = {"\"": "", "\'": ""}
        for key, value in rules.items():
            arg = arg.replace(key, value)
        return arg

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id.

        Usage: update <class_name> <instance_id> <attr_name> "<attr_value>"

        Args:
            arg (str): <class_name> <instance_id> <attr_name> <attr_value>.
        """

        split_args = arg.split(" ")
        class_name = split_args[0] if len(split_args) > 0 else None
        obj_id = split_args[1] if len(split_args) > 1 else None
        attr_name = split_args[2] if len(split_args) > 2 else None
        attr_value = split_args[3] if len(split_args) > 3 else None

        if not class_name:
            print("** class name missing **")
        elif class_name not in models.classes:
            print("** class doesn't exist **")
        elif not obj_id:
            print("** instance id missing **")
        elif not attr_name:
            print("** attribute name missing **")
        elif not attr_value:
            print("** value missing **")
        else:
            key = f"{class_name}.{obj_id}"
            forbidden_attrs = ['id', 'created_at', 'updated_at']
            if key in models.loaded_objects:
                if attr_name not in forbidden_attrs:
                    setattr(models.loaded_objects[key], attr_name,
                            self.remove_quotes(attr_value))
                    models.storage.save()
                else:
                    print(f"** Can't update the {attr_name} attribute **")
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
