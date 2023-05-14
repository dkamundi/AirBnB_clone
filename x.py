#!/usr/bin/python3
"""
Entry point of the command interpreter
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and
        prints the id.
        """
        if not arg:
            print("** class name missing **")
        else:
            args = shlex.split(arg)
            try:
                new_instance = eval(args[0])()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name
        and id.
        """
        if not arg:
            print("** class name missing **")
        else:
            args = shlex.split(arg)
            try:
                cls = eval(args[0])
            except NameError:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
            else:
                objs = storage.all(cls)
                key = "{}.{}".format(args[0], args[1])
                if key in objs:
                    print(objs[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into
        the JSON file).
        """
        if not arg:
            print("** class name missing **")
        else:
            args = shlex.split(arg)
            try:
                cls = eval(args[0])
            except NameError:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
            else:
                objs = storage.all(cls)
                key = "{}.{}".format(args[0], args[1])
                if key in objs:
                    del objs[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the
        class name.
        """
        objs = storage.all()
        if not arg:
            print([str(objs[k]) for k in objs])
        else:
            try:
                cls = eval(arg)
                print([str(objs[k]) for k in objs if type(objs[k]) == cls])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating
        attribute (save the change into the JSON file).
        """
        if not arg:
            print("** class name missing **")
        else:
            args = shlex.split(arg)
            try:
                cls = eval(args[0])
            except NameError:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            objs = storage.all(cls)
if __name__ == '__main__':
    HBNBCommand().cmdloop()
