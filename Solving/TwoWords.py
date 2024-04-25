import time


def contains_all_characters(bit_vector1, bit_vector2, alphabet_vector):
    # Check if the combined bit vectors of two words cover all characters in the alphabet_vector.
    return (bit_vector1 | bit_vector2) == alphabet_vector


def get_combine():
    combine = ""
    with open(r"Letter Boxed\Words\letter boxed diagram.txt", "r") as file:
        content = file.read()
    combine = "".join(content.split())
    return combine


def get_words():
    with open(r"Letter Boxed\Words\valid word list.txt", "r") as file:
        # Read and return all words from the valid word list.txt file.
        return [line.strip() for line in file]


def precompute_bit_vectors(words):
    bit_vectors = {}
    # Create bit vectors for each word in the given list of words.
    for word in words:
        bit_vector = 0
        for char in word:
            bit_vector |= 1 << (ord(char) - ord("a"))
        bit_vectors[word] = bit_vector
    return bit_vectors


start_time = time.time()
combine = get_combine()
alpha_vector = 0

for char in combine:
    # Create a binary vector representing the letters in the letter boxed diagram.
    alpha_vector |= 1 << ord(char) - ord("a")

words = get_words()
bit_vectors = precompute_bit_vectors(words)

valid_pairs = []
for i in range(len(words)):
    word1 = words[i]
    last_char = word1[-1]
    bit_vector1 = bit_vectors[word1]
    for j in range(len(words)):
        word2 = words[j]
        if last_char == word2[0] and word1 != word2:
            bit_vector2 = bit_vectors[word2]
            if contains_all_characters(bit_vector1, bit_vector2, alpha_vector):
                valid_pairs.append(word1 + " " + word2)

end_time = time.time()
execution_time = end_time - start_time

if len(valid_pairs) > 0:
    print(f"Found the pairs in {execution_time} seconds")
    for i in valid_pairs:
        print(i)
else:
    print("No valid pairs found.")
