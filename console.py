#!/usr/bin/python3
'''contains the entry point of the command interpreter'''
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    ''' command interprete implement'''
    prompt = "(hbnb) "

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, line):
        '''to exit the program'''
        print()
        return True

    def emptyline(self):
        '''an empty line'''
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
