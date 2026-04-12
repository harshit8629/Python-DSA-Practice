# You can use the examples as you want
import numpy as np
matrix = [[0,1,1],[1,0,1],[1,1,0]]
# this method is used for adding the rows and for columns we use the axis =0
result = np.sum(matrix, axis=1)

# list compresion means converting integer into list
print([int(x) for x in result])