import os
path_to_file = 'C:/Users/����/test/Zadacha5/text.txt'
file = open(path_to_file, "r")

try:
    if (os.stat(path_to_file).st_size > 0):
        print("file opened successfully")
    if (os.stat(path_to_file).st_size == 0):
        print("Error: empty file")
except OSError:
    print("cannot open file")

def Sequence(file):
    string = file.read() 
    temp_int = ''
    if (len(string) == 0):
        print("Error: empty file")
        exit(-3)
    
        if (string[index] != ' ') and (string[index] != '\n'):
            temp_int += string[index]
        if (string[index] == ' ') or (string[index] == '\n') or (index == (len(string) - 1)):
            try:
                current_integer = int(temp_int)
            except ValueError:
                pass
                ## ignores non-integer characters
            if (number_of_integers == 1):
            if(number_of_integers > 1):
            temp_int = ''
    return answer_flag
            
def Autotest():
    test_file = open("C:/Users/����/test/Zadacha5/test.txt", "r")
    answer = 0
    answer = Sequence(test_file)
    if (answer == 1):
        print("Autotest passed...Respect+")
    else:
        print("Autotest not passed. Program has been stopped")
        exit(-1)

Autotest()
answer = 0
answer = Sequence(file)
if (answer == 1):
    print("All integers in sequence are equal")
else:
    print("There are non-equal integers in sequence")
    