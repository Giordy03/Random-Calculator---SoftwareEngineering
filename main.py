# import useful function from the random library
from random import randrange, choices


# create a class to use different color (error messages will be printed in red)
class TextColour:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"


# global variable --> we can recall it everywhere
FILE_PATH = 'Result.txt'


def main():
    student_ID = '2256322\n'      # My student ID
    # define a dictionary with all the possible operation you want to perform (in our case the four basic ones)
    operations = {
        'addition': '+',
        'subtraction': '-',
        'multiplication': '*',
        'division': '/'
    }
    format_file(FILE_PATH)
    write_on_file(FILE_PATH, student_ID)
    n = get_user_input()
    operands = number_of_operands(n)
    numb = determine_number(operands)
    operations_to_do = determine_operation(operations, operands)
    do_calculation(numb, operations_to_do, operations)


def get_user_input():
    ok = False
    # ask a number until the input is accepted as a right value (positive integer)
    while not ok:
        try:
            n = int(input('Please, enter a positive integer: '))
            if n > 0:
                return n
            else:
                print(f'{TextColour.RED}Number not positive, please try again {TextColour.RESET}')
        except Exception as error:
            print(TextColour.RED, error, TextColour.RESET)


def number_of_operands(n):
    # n is the total number of operations to perform
    operands = list()
    while n > 0:
        # randomly pick the number of operation for each line (between 3 and 5 included)
        operands.append(randrange(3, 6))
        n -= 1
    return operands


def determine_number(operands):
    numb = list()
    for i in range(0, len(operands)):
        a = list()
        for j in range(0, operands[i]):
            a.append(randrange(0, 101, 1))      # all operand should be in the range 0, 100 (extrema included)
        numb.append(a)
    return numb


def determine_operation(poss_ope, operands):
    operations = list()         # declare operation as a list
    for element in operands:
        # create a list for every set of operations to perform
        selected_operation = choices(list(poss_ope.keys()), k=(element - 1))
        operations.append(list(selected_operation))     # add the created list to the operation list
    return operations


def do_calculation(numb, operation, symbols):
    for i in range(len(operation)):
        line = str()        # declare variable as an empty string
        for j in range(len(operation[i])):
            line += f'{numb[i][j]} {symbols.get(operation[i][j])} '     # write the expression
        line += f'{numb[i][-1]}'        # add the last term
        try:
            result = eval(line)         # perform all the operation following the right mathematical order
        except Exception as error:      # if we divide by 0 there will be an error --> write the error as result
            result = f' = IMPOSSIBLE: {error}'      # print a message on the toolbar
            print(f'{TextColour.RED} {error} {TextColour.RESET}')
        if isinstance(result, int):     # if the result is an integer number no need to have decimal digits
            line += f' = {result}'
        elif isinstance(result, float):
            line += f' = {result:.2f}'
        else:                           # else stored it as a float number with two decimal digit
            line += result
        write_on_file(FILE_PATH, line)


def format_file(path):
    try:
        with open(path, 'w', encoding='utf-8') as file:
            # delete all the information stored in the file --> we start to write in a blank file
            file.truncate()
    except Exception as error:
        exit(error)
        

def write_on_file(path, string):
    try:
        # open the file in append mode (write without deleting the existing data in the file)
        with open(path, 'a', encoding='utf-8') as file:
            file.write(string + '\n')
    except Exception as error:
        exit(error)


if __name__ == '__main__':
    main()
