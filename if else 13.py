def number_to_words(n):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
             "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
             "seventeen", "eighteen", "nineteen"]
    
    if 0 <= n <= 19:
        return words[n]
    else:
        return "Number out of range"

num = int(input("Enter a number (0-19): "))
print(f"{num} → {number_to_words(num)}")
