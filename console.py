#!/usr/bin/python3
'''contains the entry point of the command interpreter'''
from models import storage
import cmd
from models.base_model import BaseModel
import json


list = ["User", "BaseModel", "State", "Amenity", "Place", "Review"]

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
        
    def do_create(self, line):
        '''saves it (to the JSON file) and prints the id'''
        args = line.split()
        if not line:
            print("** class name missing **")
            return
        
        if args[0] not in list:
            print("** class doesn't exist **")
            return

        instance = BaseModel()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        '''Prints the string representation of an instance'''
        args = line.split()
        if not line:
            print("** class name missing **")
            return

        if args[0] not in list:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance = args[0] + "." + args[1]
        if instance not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[instance])

    def do_destroy(self, line):
        args = line.split()

        if not line:
            print("** class name missing **")
            return

        if args[0] not in list:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return
        
        key = args[0] + "." + args[1]
        if key in storage.all():
            del storage.all()[key]
            storage.save()
            return
        print("** no instance found **")
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
