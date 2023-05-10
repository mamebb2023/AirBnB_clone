#!/usr/bin/env python3
""" This is the main entry of the console """
import cmd


class AirBnB(cmd.Cmd):
    """ The commads to be used

    Attributes:
        prompt (str): The command prompt
    """

    prompt = "(hbnb) "

    def do_EOF(sefl, arg):
        """ EOF signal to exit the prompt """
        print("")
        return True

    def do_quit(self, arg):
        """ Quit the command prompt """
        return True


if __name__ == '__main__':
    AirBnB().cmdloop()
