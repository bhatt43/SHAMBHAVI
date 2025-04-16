def generate_power_tuples(end):
    result = []
    for x in range(2, end):  
        result.append((x, x**2, x**3))
    return result

end_value = 10
tuples_list = generate_power_tuples(end_value)
print(tuples_list)
