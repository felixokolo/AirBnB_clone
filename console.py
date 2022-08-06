#!/usr/bin/python3
"""Console interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
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
            except Exception:
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
            try:
                eval(parsed[0] + ".__class__")
            except Exception:
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


    def do_destroy(self, args):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234."""

        if (args == ""):
                print("** class name missing **")
        else:
            parsed = args.split()
            objs = models.storage.all()
            try:
                eval(parsed[0] + ".__class__")
            except Exception:
                print("** class doesn't exist **")
                return
            if (len(parsed) < 2):
                print("** instance id missing **")
                return
            got = objs.get(parsed[0] + "." + parsed[1])
            if (got == None):
                print("** no instance found **")
            else:
                objs.pop(parsed[0] + "." + parsed[1])
                models.storage.save()

    def do_all(self, args):
        """ Prints all string representation of all
        instances based or not on the class name.
        Ex: $ all BaseModel or $ all."""

        if (args == ""):
            for obj in models.storage.all():
                print(models.storage.all()[obj])
        else:
            parsed = args.split()
            objs = models.storage.all()
            printed = 0
            try:
                eval(parsed[0] + ".__class__")
            except Exception:
                print("** class doesn't exist **")
                return
            for obj in objs.keys():
                if (parsed[0] == obj.split(".")[0]):
                    print(models.storage.all()[obj])


    def do_update(self, args):
        """Updates an instance based on the class name
        and id by adding or updating attribute (save the
        change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """

        if (args == ""):
                print("** class name missing **")
        else:
            pars = args.split('"')
            parsed = [parsed.extend(p.split()) for p in pars]
            objs = models.storage.all()
            try:
                eval(parsed[0] + ".__class__")
            except Exception:
                print("** class doesn't exist **")
                return
            if (len(parsed) < 2):
                print("** instance id missing **")
                return
            got = objs.get(parsed[0] + "." + parsed[1])
            if (got == None):
                print("** no instance found **")
                return
            if (len(parsed) < 3):
                print("** attribute name missing **")
                return
            if (len(parsed) < 4):
                print("** value missing **")
                return
            exec("attr = got." + parsed[2] + " = " + parsed[3])
                

if __name__ == '__main__':
    HBNBCommand().cmdloop()