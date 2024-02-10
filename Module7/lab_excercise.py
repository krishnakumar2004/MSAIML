# Define your functions here.

def print_menu():
    return """MENU
c - Number of non-whitespace characters
w - Number of words
f - Fix capitalization
r - Replace punctuation
s - Shorten spaces
q - Quit

Choose an option:"""

def get_num_of_non_WS_characters(input_1):
    count = 0
    input_1 = input_1.replace(" ", "")
    for i in input_1:
        count = count + 1
    return count

def get_num_of_words(input_1):
    count = 0
    list = input_1.split()
    count = len(list)
    return count

def fix_capitalization(input_1) :
    count = 0
    strcaps = []
    strout = ''
    list = input_1.split(".")
    for i in list :
       strcaps.append(i.strip().capitalize())
    count = len(list)
    strout = ". ".join(strcaps)
    return strout, count

def replace_punctuation(input_1, exclamation_count=0, semicolon_count=0) :
    exclamation_count = input_1.count("!")
    semicolon_count = input_1.count(";")
    strout = ''
    strout1 = input_1.replace("!",".")
    strout = strout1.replace(";", ",")
    return exclamation_count, semicolon_count, strout

def shorten_space(input_1) :
    strout = ''
    strout1 = input_1.replace("     "," ")
    strout2 = strout1.replace("   ", " ")
    strout3 = strout2.replace("    ", " ")
    strout = strout3.replace("  ", " ")
    return strout
def execute_menu(menuOption, input_1):
    if menuOption == 'c':
        count = get_num_of_non_WS_characters(input_1)
        print("Number of non-whitespace characters: {}".format(count))
        print()
    elif menuOption == 'w':
        count = get_num_of_words(input_1)
        print("Number of words: {}".format(count))
        print()
    elif menuOption == 'f':
        strout, count = fix_capitalization(input_1)
        print("Number of letters capitalized: {}".format(count))
        print("Edited text: {}".format(strout))
        print()
    elif menuOption == 'r':
        exclamation_count, semicolon_count, input1 = replace_punctuation(input_1)
        print("Punctuation replaced")
        print("exclamation_count: {}".format(exclamation_count))
        print("semicolon_count: {}".format(semicolon_count))
        print("Edited text: {}".format(input1))
        print()
    elif menuOption == 's':
        strout = shorten_space(input_1)
        print("Edited text: {}".format(strout))
        print()
    elif menuOption == 'q':
        print(menuOption)


if __name__ == '__main__':
    # Complete the main program here.
    input_1 = input("Enter a sample text:\n")
    print()
    print("You entered: {}".format(input_1))
    print()
    while (True):
        print(print_menu())
        menuOption = input()
        if menuOption == 'q':
            break
        execute_menu(menuOption, input_1)