import sys
import os


def find_executable(command):
    # Get the PATH environment variable and split it into a list of directories.
    path_env = os.environ['PATH']
    path_dirs = path_env.split(":")
    
        # Iterate through each directory in the PATH.
    for dir in path_dirs:
        # Skip directories that don't exist.
        if not os.path.isdir(dir):
            continue

        # Construct the full path to the potential command.
        executable_path = os.path.join(dir, command)

        if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
            return executable_path
    return None

# type command
def type_command(command):
    # Check if the command is a built-in shell command first.
    if command in commands:
        print(f"{command} is a shell builtin")
        return

    executable_path = find_executable(command)
    if executable_path:
        print(f"{command} is {executable_path}")
    # If the command is not found in the PATH, print a "not found" message.
    else: print(f"{command}: not found")





# dictionary of commands
commands = {
    # exit the shell
    'exit' : lambda exit_status=0, *_: print(os._exit(exit_status)),
    # *args: allow to take variable number of arguments
    'echo' : lambda *args: print(" ".join(args)),
    # lambda command: print(f"{command} is a shell builtin") if command in commands else print(f"{command}: not found")
    'type' : type_command,
    'pwd': lambda *args: print(os.getcwd())
}
    

def main():
    while True:        
        # standard output in terminal
        sys.stdout.write("$$ ")
        sys.stdout.flush()
        
        # command from user with arguments
        try:
            command_with_arguments = input().split()
        except EOFError:
            print()
            break
        
        # split command to a command and an argument
        command = command_with_arguments[0]
        argument = command_with_arguments[1:]

        # command not found
        if command in commands:
            commands[command](*argument)
        else:
            executable_path = find_executable(command)
            
            if executable_path:
                # child process, near exact copy of our shell
                pid = os.fork()
                if pid == 0:
                # child process
                    os.execv(executable_path, [command] + argument)
                else:
                    # parent process
                    os.waitpid(pid, 0)
            else:
                print(f"{command}: command not found")
    
if __name__ == "__main__":
    main()