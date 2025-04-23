import csv

data = {}
with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        rollno = int(row['Roll No'])
        total = int(row['Subject1']) + int(row['Subject2']) + int(row['Subject3'])
        data[rollno] = {
            'Name': row['Name'],
            'Marks': [int(row['Subject1']), int(row['Subject2']), int(row['Subject3'])],
            'Total': total
        }

for k, v in data.items():
    print(f"Roll No: {k}, Name: {v['Name']}, Marks: {v['Marks']}, Total: {v['Total']}")


