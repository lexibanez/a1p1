from pathlib import Path

def main():
    
    while True:
        user_input = input("Enter Command: ")
        command, *args = user_input.split()
        option = None

        if command == 'Q':
            break
        elif command == 'L' and option is None:
            directory = Path(args[0])
            if directory.is_dir():
                contents = list(directory.iterdir())
                files = [x for x in contents if x.is_file()]
                directories = [x for x in contents if x.is_dir()]

                for file in files:
                    print(file)
                for directory in directories:
                    print(directory)


if __name__ == '__main__':
    main()