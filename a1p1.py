from pathlib import Path

def list_directory(directory, option=None):
    contents = list(directory.iterdir())\
    
    files = [x for x in contents if x.is_file()] # sort contents for files
    for file in files:
        print(file)

    directories = [x for x in contents if x.is_dir()] # sort contents for directories
    for directory in directories:
        print(directory)
        if option == '-r':
            list_directory(directory, '-r')

        
def main():
    while True:
        user_input = input("Enter Command: ")
        command, *args = user_input.split()

        if command == 'Q':
            break
        elif command == 'L': 
            option = None
            if len(args) > 1:
                option = args[1]
            directory = Path(args[0])
        else:
            print("Invalid command.")
            continue

        if directory.is_dir():
            list_directory(directory, option)
        else:
            print('Could not find directory.')
                
            
if __name__ == '__main__':
    main()