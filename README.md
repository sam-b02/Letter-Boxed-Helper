# **NYT Letter Boxed Helper**

Welcome to the NYT Letter Boxed Helper repository! This tool is designed to assist players of the New York Times (NYT) Letter Boxed game by providing solutions and helpful features to solve puzzles more efficiently.

# **Features**
Word Finder: Quickly find words that can be formed using the given letters.

Longest Word: Find the longest word that can be formed using the given letters.

Data Cleaning: Allows you to use your own word lists - Clean and preprocess word lists to remove consecutive letters and special characters, ensuring only valid words are considered.

# **Usage**
To use the NYT Letter Boxed Helper:

To run this program, clone this repository to your local machine and run it.

If you want to replace the word list, replace the "english.txt" file with your own wordlist named as such. Run the "datacleaner.py" file and you should be good to go.

To change the titles, open the text file at "Letter Boxed\Words\wordlist.txt" and replace the letters with your own in the same format.

Note that the list is cleaned to remove any repeated letters, so if you want to use this as a way to search for words with your parameters, simply open "Letter Boxed\Data cleaning\DataCleaner.py" and change the variable "RepeatOn" at line 24 to True.

# **PLEASE NOTE**

The default wordlist was obtained from "https://github.com/xajkep/wordlists/tree/master". All credit goes to them.

The wordlist contains unrecognized and archaic words that the NYTs will not recognize. Make sure to check multiple words.


