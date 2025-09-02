import os
from .executor import find_executable

# exit the shell with argument checking
def exit_command(*args):
    if len(args) > 1:
        print("exit: too many arguments")
        return
    
    if not args:
        os._exit(0)
    
    try:
        exit_status = int(args[0])
        os._exit(exit_status)
    except ValueError:
        print(f"exit: {args[0]}: numeric argument required")
        return

# type command
def type_command(commands, *args):
    # no arguments
    if not args:
        return
    
    command = args[0]
    # Check if the command is a built-in shell command first.
    if command in commands:
        print(f"{command} is a shell builtin")
        return

    executable_path = find_executable(command)
    if executable_path:
        print(f"{command} is {executable_path}")
    # If the command is not found in the PATH, print a "not found" message.
    else: print(f"{command}: not found")

def change_directory(*args):
    # not arguments or cd ~
        if not args or args[0] == "~":
            target_path = os.path.expanduser("~")
        elif args[0] == '/':
            target_path = "/"
        else:
    # path provided
            target_path = args[0]
        
        try:
            if os.path.isdir(target_path):
                os.chdir(target_path)
            else:
                print(f"cd: {target_path}: No such file or directory")
        except OSError as e:
            print(f"cd: {e}")