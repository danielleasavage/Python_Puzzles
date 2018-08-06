import sys


def find_all_words(phone_number):
    letter_dict = {'2':['a','b','c'], '3':['d','e','f'],
                  '4':['g','h','i'], '5':['j','k','l'], '6': ['m','n','o'],
                  '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
    phone_number = ''.join([num for num in phone_number if num not in ['0','1']])
    word_list = []
    for word in sys.stdin:
        word = word.strip()
        if len(word) == len(phone_number):
            word_list.append(word)
    for i, num in enumerate(phone_number):
            word_list = [word for word in word_list if word[i] in letter_dict[num]]
    return word_list

#####################
#### RUNS SCRIPT ####
#####################

if len(sys.argv) == 2:
    phone_number = sys.argv[1].lstrip('0')
    try: 
        int(phone_number)
    except ValueError:
        print('Oops! Input arg must be an integer value')
    if int(phone_number) > 0:
        all_words = find_all_words(phone_number)
        print(all_words)
    else:
        print('Oops! Input arg must be a POSITIVE integer value')
else:
    print ('input required')
