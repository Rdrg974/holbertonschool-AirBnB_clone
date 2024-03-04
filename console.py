#!/usr/bin/python3
"""Module for console.py"""

import cmd
import sys
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def help_quit(self):
        """Help for the quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help for the EOF command"""
        print("EOF command to exit the program")

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    # Add more commands and methods as needed

if __name__ == "__main__":
    HBNBCommand().cmdloop()
