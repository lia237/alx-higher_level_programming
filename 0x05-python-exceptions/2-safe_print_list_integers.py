#!/usr/bin/python3
def safe_print_list_integers(my_list=[], max_print=0):
    integer_count = 0
    for i in range(max_print):
        try:
            print("{:d}".format(my_list[i]), end="")
            integer_count += 1
        except (TypeError, ValueError):
            pass
    print("")
    return integer_count

