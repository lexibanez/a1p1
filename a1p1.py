from pathlib import Path
# sample paths
# C:\Users\lexib\OneDrive\Desktop\ICS32
# C:\Users\lexib\OneDrive\Desktop\test

def display_directory(directory, options):
    

    contents = list(directory.iterdir())

    files = [x for x in contents if x.is_file()] # sort contents for files
    directories = [x for x in contents if x.is_dir()] # sort contents for directories

    if '-s' in options:
        if len(options) == 3:
            search_file = options[2] # gets the file to be searched
        if len(options) == 4:
            search_file = options[3] # gets the file to be searched

        if Path(directory / search_file).is_file(): # checks if the search file has a path
            print(Path(directory / search_file))
        for directory in directories:
            if '-r' in options:
                display_directory(directory, options)

    elif '-f' in options:
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
            if directory.is_dir():
                display_directory(directory, options)
            else:
                print('Could not find directory.')
        else:
            print("Invalid command.")
            continue

        
if __name__ == '__main__':
    main()