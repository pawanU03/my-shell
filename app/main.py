import sys
import os
from .commands import commands
from .executor import find_executable

def handle_input():
    # command from user with arguments
    try:
        command_with_arguments = input().split()
        # handle empty input
        if not command_with_arguments:
            return True
            
    except EOFError:
        return False
    
    # split command to a command and an argument
    command = command_with_arguments[0]
    argument = command_with_arguments[1:]

    # command not found
    if command in commands:
        if command == 'type':
            commands[command](commands, *argument)
        else:
            commands[command](*argument)
    else:
        executable_path = find_executable(command)
        
        if executable_path:
            try:
                # child process, near exact copy of our shell
                pid = os.fork()
                if pid == 0:
                # child process
                    os.execv(executable_path, [command] + argument)
                else:
                    # parent process
                    os.waitpid(pid, 0)
            except OSError as e:
                print(f"Error executing command: {e}")
        else:
            print(f"{command}: command not found")
    return True
    

def main():
    while True:        
        # standard output in terminal
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        if not handle_input():
            break
    
if __name__ == "__main__":
    main()