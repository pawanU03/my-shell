import sys
import os


def find_executable(command):
    # Get the PATH environment variable and split it into a list of directories.
    PATH = os.environ['PATH']
    PATH_DIRS = PATH.split(":")
    
        # Iterate through each directory in the PATH.
    for dir in PATH_DIRS:
        # Skip directories that don't exist.
        if not os.path.exists(dir):
            continue

        # Construct the full path to the potential command.
        command_path = os.path.join(dir, command)

        # Check if the command exists and is executable.
        if os.path.exists(command_path):
            if os.access(command_path, os.X_OK):
                return command_path
    return None

# type command
def type_command(command):
    command_path = find_executable(command)
    # Check if the command is a built-in shell command first.
    if command in commands:
        print(f"{command} is a shell builtin")
        return

    elif command_path:
        print(f"{command} is {command_path}")

    # If the command is not found in the PATH, print a "not found" message.
    else: print(f"{command}: not found")

def helper():
    pass

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
