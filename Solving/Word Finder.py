import time

def initboard():
    board = open("Letter Boxed\Words\letter boxed diagram.txt","r")
    side = None
    top = []
    left = []
    right = []
    bottom = []
    for line in board:
        line = line.strip()
        if line:
            if line in ["top","left","right","bottom"]:
                side = line
            elif side:
                if side == "top":
                    top.append(line)
                elif side == "left":
                    left.append(line)
                elif side == "right":
                    right.append(line)
                elif side == "bottom":
                    bottom.append(line)
    combine = top + left + right + bottom
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

def contain(line, letters):
    return all(char in set(line) for char in letters)

def char_check(line, combine):
    for char in line:
        if char not in combine:
            return False
    return True

starting = input("Enter starting letter: ")
letters = []
viable = []

loop = True
while loop:
    letter = input("Enter a letter that can be anywhere inside the word. Enter 'done' if you are done: ")
    if letter.lower() != "done":
        letters.append(letter)
    else:
        loop = False

wordlist = open("Letter Boxed\Words\wordlist.txt", "r")
counter = 0

for line in wordlist:
    counter += 1
    if counter % 50000 == 0:
        print(f"Scanned {counter} lines so far")
    line = line.strip()
    if contain(line, letters) and line[0] == starting:
        viable.append(line)

print("Done!")

if len(viable) == 0:
    print("No words found.")
else:
    print(f"{len(viable)} words found with the selected letters.\n\nChecking if they match letter boxed rules now...")
    time.sleep(1)
    top, left, right, bottom, combine = initboard()
    letterboxed_viable = []

    for line in viable:
        viableBool = char_check(line,combine)
        if viableBool:
            for i in range(0,len(line)-2):
                if line[i+1] in checkpos(line[i], top, left, right, bottom):
                    viableBool = False
        if viableBool == True:
            letterboxed_viable.append(line)
    if len(letterboxed_viable) == 0:
        print("No lines were found that matched the given criteria.")    
    else:
        for line in letterboxed_viable:
            print(line)
        print(f"{len(letterboxed_viable)} lines found")