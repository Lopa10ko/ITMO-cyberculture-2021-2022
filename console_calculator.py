#!C:\Users\Georgy\Desktop\cyberculture_21-22\ITMO-cyberculture-2021-2022 python3
##
# @mainpage Doxygen Documentation
#
# @section description_main Description
# An example Python program demonstrating how to use Doxygen style comments for
# generating source code documentation with Doxygen.
#
#
##
# @file console_calculator.py
#
# @brief Simple console calculator in python.
#
# @section libraries_main Libraries/Modules
# - unit testing standard library (unittest)
#
# @section notes_doxygen_example Notes
# - Comments are Doxygen compatible.
#
# @section todo_doxygen_example TODO
# - Get the unittest working.
# - Write overview.
#
# @section author_doxygen_example Author(s)
# - Created by George Lopa10ko on 11/25/2021.
# - Modified by George Lopa10ko on 11/25/2021.
#
# Copyright (c) 2021 Lopa10ko.  All rights reserved.

# Functions
def test_main():
    """! Testing by hand."""
    assert (main(('45 + 4 - 242442 + 32342'.replace(' ', '').replace('--', '+').replace('-', '+-').split('+'))) == -210051)
    assert (main(('56-757+5888-583+784+8858+1+1'.replace(' ', '').replace('--', '+').replace('-', '+-').split('+'))) == 14248)
    assert (main(('1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9'.replace(' ', '').replace('--', '+').replace('-', '+-').split('+'))) == 45)
    assert (main(('58838 -544 + 85858 - 29296 + 5930 - 5903 -4444'.replace(' ', '').replace('--', '+').replace('-', '+-').split('+'))) == 110439)
    assert (main(('5773+5885 -4 + 584828 -588 + 58 - 58588'.replace(' ', '').replace('--', '+').replace('-', '+-').split('+'))) == 537364)
    assert (main(('884882 - 4848848 + 2 - 3484'.replace(' ', '').replace('--', '+').replace('-', '+-').split('+'))) == -3967448)
    assert (main(('453--43+4433-43343 +44'.replace(' ', '').replace('--', '+').replace('-', '+-').split('+'))) == -38370)
    assert (main(('437774  + 848484848-         488'.replace(' ', '').replace('--', '+').replace('-', '+-').split('+'))) == 848922134)
    assert (main(('8 88 8 8 8 8 8 -  7 7 77 7 7 '.replace(' ', '').replace('--', '+').replace('-', '+-').split('+'))) == 88111111)
    print('all checked')
#Argument description
# @param parsed_str is preparsed input data
def main(parsed_str):
    """! Getting the answer calculated."""
    answer = 0
    for i in range(len(parsed_str)):
        answer += int(parsed_str[i])
    return answer

if __name__ == '__main__':
    """! Input/Output."""
    print("Give your expression: ")
    print(main(parsed_str = input().replace(' ', '').replace('--', '+').replace('-', '+-').split('+')))
    test_main()

