#!/usr/bin/python3
"""Console interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Interpreter class"""
    
    prompt = "(hbnb)"


    def do_foo(self, args):
        """Just trying something: FOO"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()