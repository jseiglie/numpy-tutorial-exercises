import numpy as np
 
#3
#print(np.__version__)


#4
# zeros = np.zeros(10)
# print(zeros)

#5
# print(zeros.itemsize)
# print(zeros.size)
# memSize = zeros.itemsize * zeros.size
# print(memSize)


#6
# print(np.info(np.sum))

#7
# nullVector = np.zeros(10)
# nullVector[4] = 1
# print(nullVector)

#8
# arange = np.arange(10, 50)
# print(arange)

#9

# vector = np.arange(0, 10)
# reversedVector = vector[::-1]
# print(reversedVector)

#10

# matrix = np.arange(9).reshape((3,3))
# print(matrix)

# 11

# arr = [1,2,0,0,4,0]
# print(np.nonzero(arr))

# 12
# identityMatrix = np.eye(3)
# print(identityMatrix)

# 13
# arr = np.random.random(3)
# print(arr)

# 14

# arr = np.random.random(10)
# print(arr.max())

# 15
# arr = np.random.random(10)
# print(arr.mean())


# 16

# matrix = np.ones(25).reshape((5,5))
# matrix[1:-1,1:-1] = 0
# print(matrix)

# 17

# matrix = np.ones(25).reshape((5,5))
# matrix = np.pad(matrix, 1)
# print(matrix)
# 18
####################
# 19

# matrix = np.arange(9).reshape((3,3))
# print(np.diag(matrix))
 
# 20
# x = np.zeros((8, 8), dtype=int)
 # x = np.zeros((8, 8))
# x[1::2, ::2] = 1
# x[::2, 1::2] = 1
 
# print(x)
   
