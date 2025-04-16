input_string = input("Enter a string: ")

char_freq = {}

for char in input_string:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

print("Character Frequencies:")
for char, freq in char_freq.items():
    print(f"'{char}': {freq}")
