import numpy as np

with open ('input_10.txt', 'r') as f:
    file = f.read().split("\n")
    
data = []
for i in file:
    data.append(list(i))
    
# Create a matrix
data = np.asarray(data)
#print(data)

# Create a result matrix
result = np.zeros(data.shape)

#######

def get_num_astreoids(x, y):
    '''Calculate the number of astreoids for the given astreoid in (x,y) location'''
    
    slope_list = []
    num_astreoids = 0
    
    for i in range(data.shape[1]): # x axis
        for j in range(data.shape[0]): # y axis
            
            # Calculate the slopes only for other astreoids (for #, not .)
            if data[i,j] == "#": # if astreoid
                if (x == i) & (y == j): # Same astreoid
                    pass
                else:
                    if x != i: # Not same column
                        if y == j: # Same row
                            if x-i > 0: # Right
                                m = 9999
                            else: # Left
                                m = -8888
                        else: # Not same row
                            m  = (y-j)/(x-i)
                            if y-j < 0: # Down
                                m = m * -1111111 
                                # I tried multiplying with -1, but it didnt work,
                                # because there was some other other astreoid with the same value
                            else: # Up
                                m = m * 1  
                    else: # Same column
                        if y-j < 0: # Down
                            m = 99
                        else: # Up
                            m = -99
                    
                    slope_list.append(m)
    
#     print(x, y)
#     print(slope_list)
    
    slope_list = list(set(slope_list)) # Get the unique slopes
    num_astreoids = len(slope_list) # Calculate the number of unique slopes
    
    return num_astreoids

##### Main
for i in range(data.shape[1]): # For each row (x axis)
    for j in range(data.shape[0]): # For each column (y axis)
        
        if data[i,j] == "#": # If astreoid
            result[i, j] = get_num_astreoids(i, j) # Calculate the number of astreoids it can detect
            

print(result.max())
print(np.where(result==result.max()))
print(result)