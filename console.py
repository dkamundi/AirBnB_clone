#!/usr/bin/python3
"""
Entry point of the command interpreter
"""
import cmd
import shlex
from models.engine.file_storage import FileStorage
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
        args = shlex.split(arg)
        if len(arg) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** no instance found **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        try:
            eval(args[0])()
        except NameError:
            print("** class doesn't exist **")
            return
        k = args[0] + "." + args[1]
        try:
            value = obj_dict[k]
            print(value)
        except KeyError:
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
        objects = storage.all()
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

    def default(self, arg):
        '''
            Catches all the function names that are not expicitly defined.
        '''
        args = shlex.split(arg)
        functions = {"all": self.do_all, "update": self.do_update,
                     "show": self.do_show, "count": self.do_count,
                     "destroy": self.do_destroy, "update": self.do_update}
        args = (args.replace("(", ".").replace(")", ".")
                .replace('"', "").replace(",", "").split("."))

        try:
            cmd_arg = args[0] + " " + args[2]
            func = functions[args[1]]
            func(cmd_arg)
        except NameError:
            print("*** Unknown syntax:", args[0])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
