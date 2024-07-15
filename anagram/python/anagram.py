"""Script with the solution for the Anagram coding kata."""

if __name__ == "__main__":
    filepath = "wordlist.txt"
    word_to_anagram = "documenting"

    wordlist = []
    with open(filepath) as file:
        for line in file:
            wordlist.extend(line.split())

    valid_anagrams = []
    sorted_word_to_anagram = sorted(word_to_anagram)
    for index, first in enumerate(wordlist):
        for second in wordlist[index+1:]:
            if sorted_word_to_anagram == sorted(first + second):
                valid_anagrams.append((first, second))

    for first, second in valid_anagrams:
        print(f"{word_to_anagram} = {first} + {second}")
