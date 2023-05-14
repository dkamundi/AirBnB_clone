#!/usr/bin/env python3
"""Console"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    
    prompt = "(hbnb)"
    
    def do_create(self, arg):
        """Creates a new instance and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id"""
        args = arg.split()
        if not arg:
            print("** Class name missing **")
            return
        try:
            obj_dict = storage.all()[args[0] + '.' + args[1]].to_dict()
            print(obj_dict)
        except KeyError:
            print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except Exception:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            del storage.all()[args[0] + '.' + args[1]]
            storage.save()
        except KeyError:
            print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except Exception:
            print("** class doesn't exist **")
    
    def do_all(self, arg):
        """Print all string representation of all instances."""
        objects = []
        args = arg.split()
        if not arg:
            for obj in storage.all().values():
                objects.append(str(obj))
            print(objects)
            return
        try:
            for obj in storage.all().values():
                if obj.__class__.__name__ == args[0]:
                    objects.append(str(obj))
            print(objects)
        except Exception:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            obj = storage.all()[args[0] + '.' + args[1]]
            setattr(obj, args[2], type(getattr(obj, args[2]))(args[3]))
            obj.save()
        except KeyError:
            print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except Exception:
            print("** class doesn't exist **")
    
    def do_quit(self, arg):
        """To exot the program"""
        raise SystemExit

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        raise SystemExit

    def emptyline(self):
        """Called wheen empty line is entered"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
