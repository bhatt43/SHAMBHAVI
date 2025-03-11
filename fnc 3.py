#3rd question
def create_array(x,y,z,value):
    return[[[value for _ in range(z)] for _ in range(y)] for _ in range(x)] 
array_3d=create_array(2,2,3,1)
for layer in array_3d:
        print(layer)
    
