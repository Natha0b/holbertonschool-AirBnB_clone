#!/usr/bin/python3
'''contains the entry point of the command interpreter'''
from models import storage
import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


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

        instance = eval(args[0])()
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
        ''' Deletes an instance based on the class name and id'''
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
        storage.all().pop(instance)
        storage.save()

    def do_all(self, line):
        '''Prints all string representation of all instances'''
        args = line.split()
        list_obj = []

        if len(args) == 0:
            for aux in storage.all().values():
                list_obj.append(str(aux))
            print(list_obj)
            return

        if args[0] not in list:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            for aux in storage.all().values():
                list_obj.append(str(aux))
            print(list_obj)
            return

    def do_update(self, line):
        '''Updates an instance based on the class name and id'''

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

        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            print("** value missing **")
            return

        if type(args[3]) == str:
            args[3] = args[3].strip('"').replace('"', '')
        setattr(storage.all()[instance], args[2], args[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
