#!/usr/bin/python3

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def default(self, args):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
