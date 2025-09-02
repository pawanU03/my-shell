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

        try:
            if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
                return executable_path
        except OSError:
            # Ignore errors from os.access, as they are expected for files without execute permissions.
            pass
    return None