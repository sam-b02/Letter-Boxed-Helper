import re


def conseq(line):
    pattern = r"(.)\1"
    return bool(re.search(pattern, line))


def spec(line):
    pattern = r"[!@#$%^&*()_+{}\[\]:;<>,.?/\\|'\"~`-]"
    return bool(re.search(pattern, line))


file = open(r"Words\english.txt", "r")

cleanfile = open(r"Words\word list.txt", "w")

print("opened files")

counter = 0

for line in file:
    counter += 1
    if not conseq(line) and spec(line) is False and len(line) >= 3:
        cleanfile.write(f"{(line.lower().strip())}\n")
    if counter % 1000 == 0:
        print(counter)
