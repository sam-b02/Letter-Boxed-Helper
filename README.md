# **NYT Letter Boxed Helper**

Welcome to the NYT Letter Boxed Helper repository! This tool is designed to assist players of the New York Times (NYT) Letter Boxed game by providing solutions and helpful features to solve puzzles more efficiently.

# **Features**
Word Finder: Quickly find words that can be formed using the given letters.
Longest Word: Find the longest word that can be formed using the given letters.
Data Cleaning: Allows you to use your own word lists - Clean and preprocess word lists to remove consecutive letters and special characters, ensuring only valid words are considered.

# **Usage**
To use the NYT Letter Boxed Helper:

Clone this repository to your local machine.

If you want to replace the word list, replace the "english.txt" file with your own wordlist named as such. Run the "datacleaner.py" file and you should be good to go.
If you don't want to input the same tiles every time, look for the section in the code that looks like this:

top = ["f","d","o"]

left = ["i","h","u"]

right = ["p","t","e"]

bottom = ["g","l","r"]

and replace the letters with your own.

# **PLEASE NOTE**

The default wordlist was obtained from "https://github.com/xajkep/wordlists/tree/master". All credit goes to them.

The wordlist contains unrecognized and archaic words that the NYTs will not recognize. Make sure to check multiple words.


