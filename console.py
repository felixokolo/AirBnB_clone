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

import re
import sys


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
            if (got is None):
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
            if (got is None):
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

    def do_count(self, args):
        """ counts all string representation of all
        instances based or not on the class name.
        Ex: $ count BaseModel or $ all."""

        cnt = 0
        if (args == ""):
            print(len(models.storage.all()))
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
                    cnt += 1
            else:
                print(cnt)

    def do_update(self, args):
        """Updates an instance based on the class name
        and id by adding or updating attribute (save the
        change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """

        if (args == ""):
            print("** class name missing **")
        else:
            parsed = parse_args(args, '"')
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
            if (got is None):
                print("** no instance found **")
                return
            if (len(parsed) < 3):
                print("** attribute name missing **")
                return
            if (len(parsed) < 4):
                print("** value missing **")
                return
            exec("attr = got." + parsed[2] + " = " + parsed[3])
            got.save()

    def precmd(self, line):
        """executes before command"""
        if (len(sys.argv) > 1):
            HBNBCommand.prompt = "(hbnb)\n"
        return line

    def do_User(self, args):
        """performs commands on user"""
        parsed = parse_args(args.strip('.'), '\\(', '\\)')
        ext = ""
        if len(parsed) > 1:
            ext = extract_args(parsed[1])
        eval("self.do_" + parsed[0] + '("User "' + ext + ')')

    def do_State(self, args):
        """performs commands on State"""
        parsed = parse_args(args.strip('.'), '\\(', '\\)')
        ext = ""
        if len(parsed) > 1:
            ext = extract_args(parsed[1])
        eval("self.do_" + parsed[0] + '("State "' + ext + ')')

    def do_City(self, args):
        """performs commands on City"""
        parsed = parse_args(args.strip('.'), '\\(', '\\)')
        ext = ""
        if len(parsed) > 1:
            ext = extract_args(parsed[1])
        eval("self.do_" + parsed[0] + '("City "' + ext + ')')

    def do_Amenity(self, args):
        """performs commands on Amenity"""
        parsed = parse_args(args.strip('.'), '\\(', '\\)')
        ext = ""
        if len(parsed) > 1:
            ext = extract_args(parsed[1])
        eval("self.do_" + parsed[0] + '("Amenity "' + ext + ')')
    def do_Review(self, args):
        """performs commands on Review"""
        parsed = parse_args(args.strip('.'), '\\(', '\\)')
        ext = ""
        if len(parsed) > 1:
            ext = extract_args(parsed[1])
        eval("self.do_" + parsed[0] + '("Review "' + ext + ')')

    def do_Place(self, args):
        """performs commands on Place"""
        parsed = parse_args(args.strip('.'), '\\(', '\\)')
        ext = ""
        if len(parsed) > 1:
            ext = extract_args(parsed[1])
        eval("self.do_" + parsed[0] + '("Place "' + ext + ')')

    def do_BaseModel(self, args):
        """performs commands on BaseModel"""
        parsed = parse_args(args.strip('.'), '\\(', '\\)')
        ext = ""
        if len(parsed) > 1:
            ext = extract_args(parsed[1])
        eval("self.do_" + parsed[0] + '("BaseModel "' + ext + ')')


def parse_args(args, delmtr1='"', delmtr2='"'):
    """parse args to list of arguments"""
    ret = []
    if delmtr1.strip('\\') in args:
        search = delmtr1 + '(.*)' + delmtr2 + '$'
        at = re.search(search, args)
        if at is not None:
            found = args[at.start():]
            remain = args[:at.start()]
            ret = remain.split()
            ret.append(found)
        else:
            ret = args.split()
    else:
        ret = args.split()
    return ret

def extract_args(args):
    """parse args to list of arguments"""
    args = args.lstrip('(')
    args = args.rstrip(')')
    return args

if __name__ == '__main__':
    HBNBCommand().cmdloop()
