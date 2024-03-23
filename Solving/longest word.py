def initboard():
    board = open("Letter Boxed\\Words\\letter boxed diagram.txt", "r")
    side = None
    top = set()
    left = set()
    right = set()
    bottom = set()
    for line in board:
        line = line.strip()
        if line:
            if line in ["top", "left", "right", "bottom"]:
                side = line
            elif side:
                for char in line:
                    if side == "top":
                        top.add(char)
                    elif side == "left":
                        left.add(char)
                    elif side == "right":
                        right.add(char)
                    elif side == "bottom":
                        bottom.add(char)
    combine = top.union(left, right, bottom)
    return top, left, right, bottom, combine


def checkpos(x, top, left, right, bottom):
    if x in top:
        temp = top
    elif x in left:
        temp = left
    elif x in right:
        temp = right
    elif x in bottom:
        temp = bottom
    else:
        temp = None
    return temp


def char_check(line, combine):
    return all(char in combine for char in line)


def word_check(line, combine):
    if not char_check(line, combine):
        return False
    for i in range(1, len(line)):
        if line[i] in checkpos(line[i - 1], top, left, right, bottom):
            return False
    return True


Words = []
top, left, right, bottom, combine = initboard()
wordlist = open("Letter Boxed\\Words\\wordlist.txt", "r")
counter = 0
for line in wordlist:
    line = line.strip()
    counter += 1
    if counter % 50000 == 0:
        print(f"Scanned {counter} lines so far")
    valid = word_check(line, combine)
    if valid:
        Words.append(line)

print(f"Found {len(Words)} letterboxed words\n\nSorting the list...")
Words.sort(key=len, reverse=True)

with open(r"Letter Boxed\Words\LongestWords.txt", "w") as file:
    for line in Words:
        file.write(line + "\n")

print("Done! You can find the words at Letter Boxed\Words\LongestWords.txt")
