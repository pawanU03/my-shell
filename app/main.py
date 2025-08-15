import sys


def main():
    while True:
        # standard output in terminal
        sys.stdout.write("> ")
        
        # command from user
        command = input()
        
        # exit command
        if command == "exit":
            break
        print(f"{command}: command not found")

        
if __name__ == "__main__":
    main()
