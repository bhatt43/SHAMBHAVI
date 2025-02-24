import math

def point_position_circle(x_c, y_c, r, x_p, y_p):
    
    distance = math.sqrt(math.pow(x_p - x_c, 2) + math.pow(y_p - y_c, 2))
    
    if distance < r:
        return "Inside the circle"
    elif distance == r:
        return "On the circle"
    else:
        return "Outside the circle"

x_c, y_c, r = 0, 0, 5  
x_p, y_p = 3, 4  

result = point_position_circle(x_c, y_c, r, x_p, y_p)
print(f"The point ({x_p}, {y_p}) is {result}.")
