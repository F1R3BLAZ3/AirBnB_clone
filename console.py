#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_EOF(self, line):
        """ Defines EOF option"""
        return True
    
    def do_quit(self, args):
        """ Defines quit option"""
        return True

    def default(self, args):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
