#!/usr/bin/python3
"""Console interpreter"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Interpreter class"""
    
    prompt = "(hbnb)"


    def do_EOF(self, args):
        """EOF quit command to exit the program"""
        return True


    def do_quit(self, args):
        """Quit command to exit the program"""
        return True


    def emptyline(self):
        """Do nothing on empty line"""
        pass


    def do_create(self, args):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints
        the id. Ex: $ create BaseModel"""
        if (args == ""):
            print("** class name missing **")
        try:
            exec("newss = " + args.split()[0] + "()")
            new = BaseModel()
        except NameError:
            print("** class doesn't exist **")
        new.save()
        print(new.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()