with open('file1.txt') as f1, open('file2.txt') as f2, open('merged.txt', 'w') as out:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

    for i in range(max(len(lines1), len(lines2))):
        if i < len(lines1):
            out.write(lines1[i])
        if i < len(lines2):
            out.write(lines2[i])

print("Merged file created as 'merged.txt'")
