def convert(input_str):
    words = input_str.split()
    
    unique_words = list(set(words))
    
    sorted_words = sorted(unique_words)
    
    result = ' '.join(sorted_words)
    
    return result

input_string = input("Enter a sequence of words separated by spaces: ")
output_string = convert(input_string)
print("Processed string:", output_string)
