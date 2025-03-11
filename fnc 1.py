sample_string="SHAMBHAVI bhatt"
def count_lower_upper(s):
   count={"uppercase":0, "lowercase":0}

   for i in s:
       if i.isupper():
           count["uppercase"]+=1
       else:
           count["lowercase"]+=1

   return count
result=count_lower_upper(sample_string)
print(result)
