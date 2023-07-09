Last modified: 09/07/2023

----------------------------------
README.txt
----------------------------------

This folder contains multiple files used to solve word square puzzles.
Below you will find a description of each file and their functionality.

word_square.py:
This file contains the main Python script for solving word square puzzles. The codebase in this file
employs a Trie data structure, with several nodes correlating to a given word in the Trie. To attempt different
word squares, adjust the value assigned to the 'test_inputs' variable.

init.py:
This empty file indicates that it's containing folder is a Python package, which means its modules can be
imported as a package.

test_wordsquare_function.py:
This script comprises of unit tests that utilize the functions present in the word_square.py file.
The unit tests are designed to ensure the wordsquare functions behave as intended.

valid_words.txt:
This text file contains all valid words that can be used to solve the word square. The main.py script reads these words.
This file was originally copied from the following link: http://norvig.com/ngrams/enable1.txt

To run the main script and solve the word squares, navigate to this directory in a terminal and run 'python main.py'.
Before running this script, please check your PC's Python version by running the following
Bash command 'python --version'. If you have a Python version older than Python 2.1, download
HomeBrew (package manager) using the following Bash command:
'/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"', followed
by 'brew upgrade python' to update your Python. The unittest module is not built into Python versions
older than Python 2.1.

If you would like to check the version of HomeBrew on your PC please use the following Bash command 'brew --version'

If you want to check if you have which HomeBrew on your PC and where it is stored use the following command 'which brew'

To run the tests, navigate to this directory in a terminal and run 'python test_wordsquare_function.py'.
