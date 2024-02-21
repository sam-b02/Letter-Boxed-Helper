import re


def conseq(line, RepeatOn):
    if not RepeatOn:
        pattern = r"(.)\1"
        return bool(re.search(pattern, line))
    else:
        return False

def spec(line):
    pattern = r"[!@#$%^&*()_+{}\[\]:;<>,.?/\\|'\"~`-]"
    return bool(re.search(pattern, line))


file = open(r"Letter Boxed\Words\english.txt", "r")

cleanfile = open(r"Letter Boxed\Words\wordlist.txt", "w")

print("opened files")

counter = 0

RepeatOn = False #Change this to True if you want words with repeated characters to be allowed

for line in file:
    counter += 1
    if conseq(line, RepeatOn) == False and spec(line) == False and len(line) >= 3:
        cleanfile.write(f"{(line.lower().strip())}\n")
    if counter % 1000 == 0:
        print(counter)