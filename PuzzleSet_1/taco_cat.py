import sys
import re

def check_input(sys_input):
    # checks that there is only 1 input & that the input is a string > len 0
    return len(sys.argv) == 2 and len(sys.argv[1]) > 0 and type(sys.argv[1]) == str
    
def check_if_palindrome(input_str):
    alpha_str = re.sub("[^a-zA-Z]","", input_str)
    forward = alpha_str.lower()
    backward = forward[::-1]
    return backward == forward #returns true if the word is the same forawrd & backward

#### RUNS PROGRAM ####
if check_input(sys.argv):
    input_str = sys.argv[1]
    if check_if_palindrome(input_str):
        print ('yes')
    else:
        print ('no')
else:
    raise ValueError ("Only one arg allowed; arg must be of type string")
