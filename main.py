import sys
if __name__ == "__main__":
    parameter_list = sys.argv
    if len(parameter_list) == 3:
        addr = parameter_list[1]
        protocol = [parameter_list[2]]
    elif len(parameter_list) == 2:
        protocol = [parameter_list[1]]

    from matchingTemplate import *
    matchingTemplate()

else:
    exit(0)