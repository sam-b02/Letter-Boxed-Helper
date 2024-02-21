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


Words = []

board = input("1. enter new or 2. use prefilled?")
if board == "1":
    top, left, right, bottom = initboard()
else:
    top = ["f","d","o"]
    left = ["i","h","u"]
    right = ["p","t","e"]
    bottom = ["g","l","r"]
    combine = top + left + right + bottom



wordlist = open("Letter Boxed\wordlist.txt", "r")

counter = 0

for line in wordlist:
    line = line.strip()
    counter += 1
    if counter % 1000 == 0:
        print(counter)
    valid = True


    if checkpos(line[-1], top, left, right, bottom) == None or checkpos(line[-2], top, left, right, bottom) == None:
        valid = False
    
    for i in range(0,len(line)-2):
        if valid == True:
            if checkpos(line[i], top, left, right, bottom) == checkpos(line[i+1], top, left, right, bottom) or checkpos(line[i], top, left, right, bottom) == None:
                valid = False
    if valid == True:
        print
        Words.append(line.strip())
    
                

print(len(Words))

for i in range(1, len(Words)):
        key = Words[i]
        j = i - 1
        while j >= 0 and len(key) < len(Words[j]):
            Words[j + 1] = Words[j]
            j -= 1
        Words[j + 1] = key   

print(Words)