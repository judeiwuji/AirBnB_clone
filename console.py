#!/usr/bin/python3
"""This module contains the console interface for interacting
with the Application.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """The Application console class. Contains all the
    commands that this application can execute
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """

        return True

    def do_EOF(self, arg):
        """End of File command to exit the program
        """

        return True

    def emptyline(self):
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
