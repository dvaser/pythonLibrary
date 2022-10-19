import numpy as np

result = np.arange(0,65,15)
result = np.arange(5,15)
result = np.arange(50, 101, 5)
result = np.zeros(10)
result = np.linspace(0,100,5)
result = np.random.randint(10,30, 5)
result = np.random.randn()
matrix = np.random.randn(-50,50,15).reshape(3,5)
print(matrix)
result = matrix.sum()

np_array = np.arange(10,20)
result = np_array[:3]
result = result[::-1]

result = matrix[0,:]
result = matrix[1,2]
result = matrix[:,0]
result = matrix**2
result = matrix % 2 == 0 and matrix > 50
result = matrix[result]


print(result)