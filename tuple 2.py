students=[(1,'aakash', 18), (2, 'shweta', 19), (3,'namrata', 20), (4,'aashvi', 22), (5,'aanchal', 25)]
roll_nos=[]
names=[]
ages=[]
for student in students:
    roll_nos.append(student[0])
    names.append(student[1])
    ages.append(student[2])

print("roll number:", roll_nos)
print("names:", names)
print("ages:", ages)
