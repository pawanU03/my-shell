import sys
import os

# type command
def type_command(command):
    if command in commands:
        print(f"{command} is a shell builtin")
        return
    
    PATH = os.environ['PATH']
    PATH_DIRS = PATH.split(":")
    
    for dir in PATH_DIRS:
        if not os.path.exists(dir):
            continue
        
        command_path = os.path.join(dir, command)
        
        if os.path.exists(command_path):
            if os.access(command_path, os.X_OK):
                print(f"{command} is {command_path}")
                return
        
        
    print(f"{command}: not found")

# dictionary of commands
commands = {
    # exit the shell
    'exit' : lambda exit_status=0, *_: print(os._exit(exit_status)),
    # *args: allow to take variable number of arguments
    'echo' : lambda *args: print(" ".join(args)),
    # lambda command: print(f"{command} is a shell builtin") if command in commands else print(f"{command}: not found")
    'type' : type_command,
}


def main():
    while True:        
        # standard output in terminal
        sys.stdout.write("$$ ")
        
        # command from user with arguments
        command_with_arguments = input().split()
        
        # split command to a command and an argument
        command = command_with_arguments[0]
        argument = command_with_arguments[1:]

        # command not found
        if command not in commands:
            print(f"{command}: command not found")
            continue
        commands[command](*argument)
    
if __name__ == "__main__":
    main()
