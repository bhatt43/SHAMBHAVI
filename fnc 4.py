#4th question
def sum_avg(marks):
    total=sum(marks)
    avg=total/len(marks)
    return total, avg
marks=[90,80,85,70,75]
total, avg=sum_avg(marks)
print(f"Total:{total}, Average:{avg}")
