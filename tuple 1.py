list=['shambhavi', ('raj',), 'yashshvi', ('vedagna',)]
boys_count=0
girls_count=0
for i in list:
    if isinstance (i, tuple):
        boys_count+=1
    else:
            girls_count+=1

print("number of girls:", girls_count)
print("number of boys:", boys_count)
