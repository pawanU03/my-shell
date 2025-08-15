import sys
import os



# dictionary of commands
commands = {
    # *args: allow to take variable number of arguments
    'echo' : lambda *args: print(" ".join(args))
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
        
        
        # to exit the shell
        if command == "exit":
           quit()
        
        # command not found
        if command not in commands:
            print(f"{command}: command not found")
            continue
        
        commands[command](*argument)
    
if __name__ == "__main__":
    main()
