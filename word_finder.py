# Former Coding Interview Question: Find longest word in dictionary that is a subsequence of a given string

import collections

# Sample input
s = "abppplee"
d = {"able", "ale", "apple", "bale", "kangaroo"}

def find_longest_word_in_string(letters, words):
    letter_pos = collections.defaultdict(list)
    print("letters: ", letters)
    print("words: ", words)

    # for each letter in 'letters', collect all the indices at which it appears.
    # O(#letters) space and speed. [using O(n) algorithm]
    for index, letter in enumerate(letters):
        letter_pos[letter].append(index)
        print("letter_pos: ", letter_pos)

    for word in sorted(words, key=lambda word: len(word), reverse=True):
        pos = 0
        print("sorted dict: ", sorted(words, key=lambda word: len(word), reverse=True))
        print("word to be searched: ", word)
        for letter in word:
            print("letter: ", letter)
            if letter not in letter_pos:
                break
        # find any remaining valid positions in search string where this letter appears.
        # it would be better to do this with binary search
        possible_pos = [p for p in letter_pos[letter] if p >= pos]
        print("possible_pos: ", possible_pos)
        if not possible_pos:
            break
        pos = possible_pos[0] + 1
        print("pos: ", pos)

        # did not break out of loop, so all letters have valid positions
        print("word: ", word)
        return word

# Main
result = find_longest_word_in_string(s, d)
print("Result of the search:", result)