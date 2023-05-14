#!/usr/bin/env python3
""" The command prompt for the site """
import cmd


class HBNBCommand(cmd.Cmd):
    """ The command prompt """
    prompt = "(hbnb) "

    def emptyline(self):
        """ Do nothing upon receiving an empty line """
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
