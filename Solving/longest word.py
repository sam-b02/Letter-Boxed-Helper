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


Words = []


top, left, right, bottom, combine = initboard()


wordlist = open("Letter Boxed\Words\wordlist.txt", "r")

counter = 0

for line in wordlist:
    line = line.strip()
    counter += 1
    if counter % 50000 == 0:
        print(f"Scanned {counter} lines so far")
    valid = True

    if checkpos(line[-1], top, left, right, bottom) == None or checkpos(line[-2], top, left, right, bottom) == None:
        valid = False
    
    for i in range(0,len(line)-2):
        if valid == True:
            if checkpos(line[i], top, left, right, bottom) == checkpos(line[i+1], top, left, right, bottom) or checkpos(line[i], top, left, right, bottom) == None:
                valid = False
    if valid == True:
        Words.append(line.strip())

print(f"Found {len(Words)} letterboxed words\n\nSorting the list...")
time.sleep(1)

for i in range(1, len(Words)):
    key = Words[i]
    j = i - 1
    while j >= 0 and len(key) < len(Words[j]):
        Words[j + 1] = Words[j]
        j -= 1
    Words[j + 1] = key   

for line in Words:
    print(line)
