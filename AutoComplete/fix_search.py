import sys


class Node:
    """ A node in a tree built from all words in the word list.
    Parameters:
    letter - each node represents an individual letter in a sequence
    of all words leading to it.
    """

    def __init__(self, letter):
        self.letter = letter
        self.children = []
        self.full_word = False
        self.words_containing = []
        self.child_dict = {}

    def add_child(self, new_node, letter):
        self.children.append(new_node)
        self.child_dict[letter] = new_node


class AmazingAutoComplete:
    """Given a list of words this class creates a
    data structure that will assist in the O(n) or less
    search for words containing fix.
    """

    def __init__(self, word_list, command):
        self.word_list = [word.lower() for word in word_list]
        self.direction = command
        self.root = Node('.')

    def add_word(self, root, word, word_ordered):
        node = root
        for letter in word:
            more_letters = [child.letter for child in node.children]
            if letter in more_letters:
                node = node.children[more_letters.index(letter)]
            else:
                child = Node(letter)
                node.add_child(child, letter)
                node = child
            node.words_containing.append(word_ordered)
        node.word_finished = True
        # node.words_containing.append(word_ordered)

    def build_tree(self):
        root = self.root

        if self.direction == 'p':
            for word in self.word_list:
                self.add_word(root, word, word)
        else:
            for word in self.word_list:
                self.add_word(root, word[::-1], word)


    def find_all_words(self, fix, command):
        """
        Parameters:
        fix - string that should be contained in the words returned
        structure - the data structure created by 'create_structure'.
        command - string indicating prefix of suffix
        Output:
        Returns the words containing fix
        """
        node = self.root
        if len(node.children) < 1:
            return 'No words given'
        if command == 'prefix':
            for letter in fix:
                try:
                    node = node.child_dict[letter]
                except:
                    return 'No words with that' + command
        else:
            for letter in fix[::-1]:
                try:
                    node = node.child_dict[letter]
                except:
                    return 'No words with that' + command
        return node.words_containing


def acceptable_ffix(s):
    """
    Parameters: s - is a string
    Output : returns True is it is an acceptable
    prefix/suffix (of at least length one and part of the English ASCII set);
    otherwise returns False.
    """
    return len(s) > 0 and all(65 <= ord(c) <= 122 for c in s)


def create_structure(command):
    """
    Parameters:
    command - string that indicates if fix is a prefix or a suffix
    Output:
    Returns a data_structure to search through for words containing fix
    """
    word_list = []
    for word in sys.stdin:
        word = word.strip()
        word_list.append(word)
    structure = AmazingAutoComplete(word_list, command)
    structure.build_tree()
    return structure


usage = """usage: python fix_search.py [-p str |file ] ...
Only one arg can be passed at any given time.
Options and arguments:
-h     : print this help message and exit
-p     : return a list of words with the prefix given and exit (also --prefix)
-s     : return a list of words with the suffix given and exit (also --suffix)
< file   : txt file read from stdin
arg ...: arguments passed to program in sys.argv[1:]

O(n) explanation:
The creation of the data structure itself is not O(n).
However the search for words containing the string given as part
of the parameters of the search is. Given the way that the structure is
created, it is simply n O(1) lookups for each letter in the string. Making the
total complexity of the problem O(n) for n letters in the string.
"""

#######################################################
############## This Runs the Program ##################
#######################################################

if len(sys.argv) == 3 and acceptable_ffix(sys.argv[2]):

    command_type = sys.argv[1]
    fix = sys.argv[2]

    if command_type == '-h':  # returns usage instructions
        print(usage)

    elif command_type == '-p' or command_type == '--prefix':
        # returns words that contain the prefix given
        my_tree = create_structure('p')
        print(my_tree.find_all_words(fix, 'prefix'))

    elif command_type == '-s' or command_type == '--suffix':
        # returns words that contain the suffix given
        my_tree = create_structure('s')
        print(my_tree.find_all_words(fix, 'suffix'))

    else:  # if the args are none of the above return usage instructions
        print(usage)

else:  # if the args restrictions are not met return usage instructions
    print(usage)
