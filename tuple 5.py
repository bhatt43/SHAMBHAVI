tuples_list=[(1,2), (), (3,4), (5,6), ()]
new_list=[t for t in tuples_list if t]
print('The new list after removing the empty tuples is:', new_list)
