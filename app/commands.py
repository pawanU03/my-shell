from builtins import exit_command, type_command, change_directory
import os

# dictionary of commands
commands = {
    # exit the shell
    'exit' : exit_command,
    # *args: allow to take variable number of arguments
    'echo' : lambda *args: print(" ".join(args)),
    'type' : type_command,
    'pwd'  : lambda **args: print(os.getcwd()),
    'cd'   : change_directory
}