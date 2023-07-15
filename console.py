#!/usr/bin/python3
'''console module'''


import cmd


class HBNBCommand(cmd.Cmd):
    '''A class that defines the entry point
    to the command interpreter
    '''

    prompt = '(hbnb) '

    def emptyline(self):
        '''Do nothing when prompt recieves an empty line'''
        pass

    def do_quit(self, arg):
        '''Quit command to exit the program
        '''
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
