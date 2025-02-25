#set 3
names_set=set()
names_set.update({"sam", "ved", "bhishma", "gautam", "rachana"})
print("set after adding names:", names_set)

names_set.discard("sam")
names_set.add("gautam")
print("set after modifying a name:", names_set)

names_set.discard("ved")
names_set.discard("bhishma")
print("set after deleting two names:", names_set)
