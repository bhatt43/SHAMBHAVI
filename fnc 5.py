#5th question
import string
def ispangram(s):
    alphabet_set=set(string.ascii_lowercase)
    input_set=set(s.lower())
    return alphabet_set<=input_set
test_strings=['The quick brown fox jumps over the lazy dog']

for text in test_strings:
    print(f"'{text}' is a pangram: {ispangram(text)}")
