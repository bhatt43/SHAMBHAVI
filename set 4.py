#set 4
names_set={"Bhupendra", "Bhavya", "Bob", "Ashiya", "Aliya"}

a_names={name for name in names_set if name.startswith("A")}
b_names={name for name in names_set if name.startswith("B")}

print("names starting with A:", a_names)
print("names starting with B:", b_names)
