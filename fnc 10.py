def frequency(text):
   
    words = text.split()
    
    freq_dict = {}
    
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    
    sorted_freq = dict(sorted(freq_dict.items()))
    
    return sorted_freq

input_string = input("Enter a string: ")
result = frequency(input_string)
print("Word Frequencies (sorted):")
for word, count in result.items():
    print(f"{word}: {count}")
