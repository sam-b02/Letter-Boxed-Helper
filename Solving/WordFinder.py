import time


def initboard():
    with open(r"Letter Boxed\Words\letter boxed diagram.txt", "r") as board:
        top = board.readline().strip().split(" ")
        left = board.readline().strip().split(" ")
        right = board.readline().strip().split(" ")
        bottom = board.readline().strip().split(" ")

    combine = "".join(top + left + right + bottom)
    return top, left, right, bottom, combine


def get_letters():
    starting = input("Enter starting letter: ")
    letters = []
    while True:
        letter = input(
            "Enter a letter that can be anywhere inside the word. Enter 'done' if you are done: "
        )
        if letter.lower() != "done":
            letters.append(letter.lower())
        else:
            return starting, letters


def word_check(word):
    if word[0] != starting:
        return False
    for i in letters:
        if i not in word:
            return False
    return True


starting, letters = get_letters()
viable_words = []

start_time = time.time()

with open(r"Letter Boxed\Words\valid word list.txt") as file:
    for line in file:
        line = line.strip()
        if word_check(line):
            viable_words.append(line)

end_time = time.time()
execution_time = end_time - start_time

if len(viable_words) == 0:
    print("no words found that match given criteria")
else:
    for i in viable_words:
        print(i)

print(f"task completed in {execution_time} seconds")
