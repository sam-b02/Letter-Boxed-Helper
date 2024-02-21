starting = input("Enter starting letter: ")
letters = []
viable = []

def initboard():
    top = []
    left = []
    right = []
    bottom = []
    for i in range(0,3):
        top.append(input("Enter top letter: "))
    for i in range(0,3):
        left.append(input("Enter left letter: "))
    for i in range(0,3):
        right.append(input("Enter right letter: "))
    for i in range(0,3):
        bottom.append(input("Enter bottom letter: "))
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

loop = True

while loop:
    letter = input("Enter a letter that can be anywhere inside the word. Enter 'done' if you are done: ")
    if letter.lower() != "done":
        letters.append(letter)
    else:
        loop = False

counter = 0

wordlist = open("Letter Boxed\wordlist.txt", "r")

for line in wordlist:
    counter += 1
    if counter % 1000 == 0:
        print(counter)
    line = line.strip()
    if contain(line, letters) and line[0] == starting:
        viable.append(line)

print("Done!")

if len(viable) == 0:
    print("No words found.")
else:
    print(f"{len(viable)} words found.")
    q = input("1. Refine further or 2. Print list: ")
    if q == "2":
        for line in viable:
            print(line)
    elif q == "1":
        counter = 0
        board = input("1. enter new or 2. use prefilled?")
        if board == "1":
            top, left, right, bottom = initboard()
        else:
            top = ["f","d","o"]
            left = ["i","h","u"]
            right = ["p","t","e"]
            bottom = ["g","l","r"]
            combine = top + left + right + bottom
        letterboxed_viable = []
        print(combine)
        for line in viable:
            viableBool = True
            for i in range(0,len(line)-2):
                if checkpos(line[i], top, left, right, bottom) == checkpos(line[i+1], top, left, right, bottom) or checkpos(line[i], top, left, right, bottom) == None or checkpos(line[i+1], top, left, right, bottom) == None:
                    viableBool = False
            for i in line:
                if i not in combine:
                    viableBool = False
            if viableBool == True:
                letterboxed_viable.append(line)
        if len(letterboxed_viable) == 0:
            print("lmao no lines")    
        else:
            for line in letterboxed_viable:
                print(line)
            print(f"{len(letterboxed_viable)} lines found")
