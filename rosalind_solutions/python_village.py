# Rosalind Python Village – Topic-wise grouped solutions
# https://rosalind.info/problems/list-view/?location=python-village
# string manipulation, slicing, file I/O, loops, and dictionaries.

# === INI1 ===
# INI1 – Installing Python
# Task: Print the Zen of Python
import this

# === INI2 ===
# INI2 – Variables and Arithmetic
# Task: Compute a^2 + b^2
def hypotenuse(a, b):
    return a**2 + b**2

print("INI2 – Hypotenuse Sum (879, 947):", hypotenuse(879, 947))


# === INI3 ===
# INI3 – Strings and Slicing
# Task: Given a string s and integers a, b, c, d, print s[a:b+1] and s[c:d+1]
s = input().strip()
a, b, c, d = map(int, input().split())
print("INI3 – Slices:", s[a:b+1], s[c:d+1])


# === INI4 ===
# INI4 – Loops and Conditions
# Task: Sum of odd integers between a and b (inclusive)
def sum_of_odds(start, end):
    return sum(i for i in range(start, end + 1) if i % 2 != 0)

print("INI4 – Sum of odds (4075, 8280):", sum_of_odds(4075, 8280))


# === INI5 ===
# INI5 – Working with Files
# Task: Print even-numbered lines (1-based) from a file
def extract_even_lines(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for i, line in enumerate(infile, 1):  # Start counting from 1
            if i % 2 == 0:
                outfile.write(line)

# Example usage (uncomment to use)
# extract_even_lines('rosalind_ini5.txt', 'output.txt')


# === INI6 ===
# INI6 – Working with Strings
# Task: Count word occurrences in a string
def count_word_occurrences(s):
    word_count = {}
    for word in s.split(' '):
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for word, count in word_count.items():
        print(f"{word} {count}")

# Example usage (uncomment to use)
# s = input("Enter a string: ").strip()
# count_word_occurrences(s)
