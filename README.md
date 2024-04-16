# **NYT Letter Boxed Helper**

Welcome to the NYT Letter Boxed Helper repository! This tool is designed to assist players of the New York Times (NYT) Letter Boxed game by providing solutions and helpful features to solve puzzles more efficiently.

# **Features**
- Two Words: Find a solution for the puzzle in two words, if possible.
- Word Finder: Quickly find words that can be formed using the given letters.
- Longest Word: Generates all possible valid words, and then finds the longest word possible. (results are saved at `Words\LongestWords.txt`)
- Data Cleaning: Allows you to use your own word lists - Clean and prepare word lists to remove consecutive letters and special characters, ensuring only valid words are considered.

# **Usage**
To use the NYT Letter Boxed Helper:

1. Clone this repository to your local machine.
2. {OPTIONAL} If you want to replace the word list, replace the `Words\english.txt` file with your own wordlist with the same name. 
Run the `Data cleaning\DataCleaner.py` file to clean the word list and make it ready for processing.
3. Change the letters used by opening the text file at `Words\letter boxed diagram.txt` and replace the letters with your own in the same format.
4. {IMPORTANT} Run the `Solving\longest word.py` program. Without doing this, the program will not have been updated with the newer letters.

You can now run any program you want.

# **PLEASE NOTE**

- Please run `longestword.py` if you have changed the letters. The program will not work otherwise.
- The default wordlist was obtained from [wordlists GitHub repository](https://github.com/xajkep/wordlists/tree/master). All credit goes to them.
- The wordlist contains unrecognized and archaic words that the NYTs will not recognize. Make sure to check multiple words.
- The programs do not have many checks, they assume the user has input the correct data. Please make sure that is the case. 

# **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
