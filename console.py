#!/usr/bin/python3
"""Console interpreter"""
import cmd
from models.base_model import BaseModel
import models

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
        else:
            try:
                new = eval(args.split()[0])()
            except NameError:
                print("** class doesn't exist **")
            else:
                new.save()
                print(new.id)


    def do_show(self, args):
        """Prints the string representation of an
        instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234."""

        if (args == ""):
            print("** class name missing **")
        else:
            parsed = args.split()
            objs = models.storage.all()
            for obj in objs.keys():
                if parsed[0] in obj:
                    break
            else:
                print("** class doesn't exist **")
                return
            if (len(parsed) < 2):
                print("** instance id missing **")
                return
            got = objs.get(parsed[0] + "." + parsed[1])
            if (got == None):
                print("** no instance found **")
            else:
                print(got)
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()