with open('input.txt', 'r') as infile, open('cleaned.txt', 'w') as outfile:
    for line in infile:
        for word in [' a ', ' an ', ' the ']:
            line = line.replace(word, ' ')
        outfile.write(line)

print("Words removed and saved in 'cleaned.txt'")
