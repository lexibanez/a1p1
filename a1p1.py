from pathlib import Path

def display_directory(directory, options):
    contents = list(directory.iterdir())

    files = [x for x in contents if x.is_file()] # sort contents for files
    directories = [x for x in contents if x.is_dir()] # sort contents for directories

    if '-f' in options:
        for file in files:
            print(file)
        for directory in directories:
            if '-r' in options:
                display_directory(directory, options)
    else:
        for file in files:
            print(file)
        for directory in directories:
            print(directory)
            if '-r' in options:
                display_directory(directory, options)

def main():
    while True:
        user_input = input("Enter Command: ")
        command, *args = user_input.split()
        
        if command == 'Q':
            break
        elif command == 'L': 
            options = []
            if len(args) > 1:
                options = args
            directory = Path(args[0])
        else:
            print("Invalid command.")
            continue

        if directory.is_dir():
            display_directory(directory, options)
        else:
            print('Could not find directory.')
                
            
if __name__ == '__main__':
    main()