# Python_Puzzles

Puzzles in Python taken from Problem Solving with Python @ USF

Original repositories & commit histories can be found using the links given below! 

All solutions are written in Python 3. Enjoy :)

## Contents

**[ReHash - Creating a HashTable Class](https://github.com/USF-MSAN689/rehash-danielleasavage)**
* Creating_Htable_class.ipynb - This is the jupyter notebook used to create and test the original htable class
* htable_oo.py - This is the final py file

**[ReStructure - Data structures and Big O](https://github.com/USF-MSAN689/restructure-danielleasavage)**
* Creating_graphs.ipynb - This is the jupyter notebook used to create and test the original Node and Graph classes
* graph.py - Implements class Node and class Graph
* test_graph.py - Test for correct implementation of graph.py
* big_o_plot.py - Plots BigO completxity

**[AutoComplete - Tree/Trie Practice](https://github.com/USF-MSAN689/autocomplete-danielleasavage)**

Given a prefix or a suffix find all matching words in a given list of words Code should runs in O(n) for n symbols
* autocomplete.ipynb - This is the jupyter notebook used to create and test the autocomplete program
* fix_search.py - Final py file for autocomplete program
* word_list.txt - Used for testing the autocomplete

**[Puzzle Set 1 - Contains two puzzles and thier solutions](https://github.com/USF-MSAN689/taco-cat-is-calling-danielleasavage)** 
* puzzle_1.ipynb - This is the jupyter notebook used for creating and testing the puzzle solutions
* taco_cat.py - A program that takes a word or a sentence and determines whereather is it palindrome or not
* call_me_maybe.py - A program that given a "phone number" prints a sorted list of all possible words generated from a telephone keypad and verifies them with a given word list
* words_list.txt - Used for testing is possible words are infact real words

**[Puzzle Set 2 - Contains three puzzles and thier solutions](https://github.com/USF-MSAN689/noprobllamma-danielleasavage)**
Description of the problems take from [CourseWare for Problem Solving with Python](https://github.com/USF-MSAN689/courseware/blob/master/hm-5/hm5.md)
* noprobllama.ipynb - This is the jupyter notebook for creating and testing the puzzle solutions
* compass.py - Final Solution to the following problem

Find the shortest path on the compass

The first line of input is the current direction of the needle -- n_1 (0 ≤ n_1 ≤ 359) type:int
The second line of input the final direction of the needle -- (0 ≤ n_2 ≤ 359) type:int


* lazy.py - Final Solution to puzzle given below.

Belfort invests in stocks. He recently was able to get his hands on a a time machine. He realizes that with his knowledge of the stock market history he can make money by buying and selling at the right times. Given that he can only take $100 with him and can travel back at max one year how much money can he make?

The first line the number of days Belfort goes back in time -- d(1 ≤ d ≤ 365) type : int
Then follow d lines is the price per share on day i. 
Days are ordered from oldest to newest -- pi(1 ≤ pi ≤ 500) : type int

* ranking.py - Final Solution to the following problem

Spencer is playing a game that has a ranking system. There are 25 regular ranks, and an extra rank, Legend, above that. The ranks are numbered in decreasing order, 25 being the lowest rank, 1 the second highest rank, and Legend the highest rank.
If spencer wins he gains a star. If before the game the player was on rank 6-25, and this was the third or more consecutive win, she gains an additional bonus star for that win. When he has all the stars for his rank and gains another star, he will instead gain one rank and have one star on the new rank.
If Spencer is on rank 1-20 loses a game, he loses a star. If Spencer has zero stars on a rank and loses a star, he will lose a rank and have all stars minus one on the rank below. However, one can never drop below rank 20 (losing a game at rank 20 with no stars will have no effect).
If Spencer reaches the Legend rank he will stay a legend no matter the number of wins or losses following. 

Spencer starts at rank 25 with no stars. Given the match history of Spencer, what is his rank at the end of the sequence of matches?

The number of stars on each rank are as follows:
Rank 25-21: 2 stars
Rank 20-16: 3 stars
Rank 15-11: 4 stars
Rank 10-1: 5 stars

Results of the matches -- A single string with each charater crresponding with one game; **W** for win and **L** for loss.

