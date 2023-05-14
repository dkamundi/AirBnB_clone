#!/usr/bin/env python3
"""Console"""

import cmd



class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """To exot the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Called wheen empty line is entered"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
