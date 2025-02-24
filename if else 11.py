def are_collinear(x1, y1, x2, y2, x3, y3):
   
    area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    
    return area == 0

x1, y1 = 1, 2
x2, y2 = 3, 4
x3, y3 = 5, 6

if are_collinear(x1, y1, x2, y2, x3, y3):
    print("The points are collinear.")
else:
    print("The points are not collinear.")
