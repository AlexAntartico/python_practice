

def trimm_trailing_whitespace():
    """
    Function that will take a file as input and return
    same file without trailing whitespace
    """
    filename = input("File to trim:")
    with open(filename) as file_object:
        for line in file_object:
            print(line.rstrip())


if __name__ == '__main__':
    trimm_trailing_whitespace()
