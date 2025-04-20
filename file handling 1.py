import csv
filename="excel_shambhavi.csv"
data=[
    ["roll no", "name", "cp 2", "maths", "chemistry"],
    ["1", "shambhavi", "20", "23", "24"],
    ["2", "priyanka", "21", "24", "23"],
    ["3", "priyanshi", "22", "19", "22.5"]
    ]

with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer=csv.writer(file)
    writer.writerows(data)

    print(f"CSV filr '{filename}' has been created successfully!")
