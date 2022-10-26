#!/usr/bin/python3
"""This module contains the console interface for interacting
with the Application.
"""

import cmd

from models import get_model, storage
from helpers.command_validator import CommandValidator


class HBNBCommand(cmd.Cmd):
    """The Application console class. Contains all the
    commands that this application can execute
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """Ensures that an empty line + ENTER shouldn’t
        execute anything"""

        return False

    def do_quit(self, arg):
        """Quit command to exit the program
        """

        return True

    def do_EOF(self, arg):
        """End of File command to exit the program
        """

        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to json
        file and print the id
        """

        if not CommandValidator.canDoCreate(arg):
            return False
        model = get_model(arg)
        obj = model()
        obj.save()
        print("{}".format(obj.id))

    def do_show(self, arg):
        """ Prints the string representation of an instance based
        on the class name and id
        """

        if not CommandValidator.canDoCommand(arg):
            return False

        args = arg.strip().split(" ")
        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key, None)
        print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        """

        if not CommandValidator.canDoCommand(arg):
            return False

        args = arg.strip().split(" ")
        key = "{}.{}".format(args[0], args[1])
        del storage.all()[key]
        storage.save()

    def do_update(self, arg):
        """Updates an instance based on the class name and id by
        adding or updating attribute
        """

        if not CommandValidator.canDoUpdate(arg):
            return False

        args = arg.strip().split(" ")
        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key, None)
        attribute = args[2]
        value = args[3]
        quoted_value = arg.split('"')
        if len(quoted_value) > 1:
            value = quoted_value[1]
        try:
            attribute_type = type(getattr(obj, attribute))
            setattr(obj, attribute, attribute_type(value))
        except AttributeError:
            setattr(obj, attribute, value)
        obj.save()

    def do_all(self, arg=""):
        """Prints all string representation of all
        instances based or not on the class name
        """
        if arg == "":
            objs = storage.all()
            list_o = []
            for key in objs:
                list_o.append(str(objs[key]))
            print(list_o)
        else:
            if not CommandValidator.canDoCreate(arg):
                return False
            objs = storage.all()
            list_o = []
            for key in objs:
                if arg in key:
                    list_o.append(str(objs[key]))
            print(list_o)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
