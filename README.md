# **NYT Letter Boxed Helper**

Welcome to the NYT Letter Boxed Helper repository! This tool is designed to assist players of the New York Times (NYT) Letter Boxed game by providing solutions and helpful features to solve puzzles more efficiently.

# **Features**
- Two Words: Find a solution for the puzzle in two words, if possible.
- Word Finder: Quickly find words that can be formed using the given letters.
- Longest Word: Find the longest word that can be formed using the given letters.
- Data Cleaning: Allows you to use your own word lists - Clean and preprocess word lists to remove consecutive letters and special characters, ensuring only valid words are considered.

# **Usage**
To use the NYT Letter Boxed Helper:

1. Clone this repository to your local machine.
2. {OPTIONAL} If you want to replace the word list, replace the `Words\english.txt` file with your own wordlist named as such. Run the `Data cleaning\DataCleaner.py` file to preprocess the word list.
3. Change the letters used by opening the text file at `Words\wordlist.txt` and replace the letters with your own in the same format.
4. Run the `Solving\longest word.py` program.

You can now run any program you want.

# **PLEASE NOTE**

- Please run `longestword.py` before running `twowords.py`. The program will not work otherwise.
- The default wordlist was obtained from [wordlists GitHub repository](https://github.com/xajkep/wordlists/tree/master). All credit goes to them.
- The wordlist contains unrecognized and archaic words that the NYTs will not recognize. Make sure to check multiple words.
