"""FizzBuzz Coding Kata"""

from fizzbuzz import fizzbuzz, fizzbuzz2


if __name__ == "__main__":
    print("FizzBuzz", "-" * 8, sep="\n")
    for num in range(1, 101):
        print(fizzbuzz(num))

    print("\nFizzBuzz: Stage 2", "-" * 17, sep="\n")
    for num in range(1, 101):
        print(fizzbuzz2(num))
