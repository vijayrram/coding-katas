"""FizzBuzz Coding Kata"""

from fizzbuzz_rules import fizzbuzz


if __name__ == "__main__":
    for num in range(1, 101):
        print(fizzbuzz(num))
