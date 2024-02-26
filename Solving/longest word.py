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

def char_check(line, combine):
    for char in line:
        if char not in combine:
            return False
    return True

def word_check(line, combine):
    if char_check(line, combine) == False:
        return False
    
    for i in range(1,len(line)):
        if line[i] in checkpos(line[i-1], top, left, right, bottom):
            return False
    
    return True

Words = []


top, left, right, bottom, combine = initboard()


wordlist = open("Letter Boxed\Words\wordlist.txt", "r")

counter = 0

for line in wordlist:
    line = line.strip()
    counter += 1

    if counter % 50000 == 0:
        print(f"Scanned {counter} lines so far")
    valid = word_check(line, combine)

    if valid == True:
        Words.append(line.strip())

print(f"Found {len(Words)} letterboxed words\n\nSorting the list...")

time.sleep(1)

Words.sort(key=len)

for line in Words:
    print(line)
