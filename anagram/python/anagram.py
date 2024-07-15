"""Script with the solution for the Anagram coding kata."""

if __name__ == "__main__":
    filepath = "wordlist.txt"
    word_to_anagram = "documenting"

    wordlist = []
    with open(filepath) as file:
        for line in file:
            wordlist.extend(line.split())

    for index, first in enumerate(wordlist):
        for second in wordlist[index+1:]:
            if sorted(word_to_anagram) == sorted(first + second):
                print(f"{word_to_anagram} = {first} + {second}")
