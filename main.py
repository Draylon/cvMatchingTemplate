import sys
if __name__ == "__main__":
    directory = ""
    if len(sys.argv) >= 2:
        directory=sys.argv[1]
    else:
        raise Exception("Insufficient Arguments: Missing directory!")

    from matchingTemplate import *
    matchingTemplate(directory)

else:
    exit(0)