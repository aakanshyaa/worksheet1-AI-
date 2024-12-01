# -*- coding: utf-8 -*-
"""worksheet1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oLxERV9HZQkwt8BibDr8P2KOo6go1lL-
"""

# qn:1
import numpy as np
empty_array = np.empty((2,2))
print (empty_array)

# qn:2
import numpy as np
ones_array = np.ones((4,2))
print (ones_array)

# qn3
import numpy as np
filled_array = np.full((3,3),9)
print(filled_array)

# qn4
import numpy as np
original_array = np.array([[5,8,1],[1,2,9]])
zeros_array = np.zeros_like(original_array)
print(zeros_array)

# qn5
import numpy as np
original_array = np.array([[1,2,3],[4,5,6]])
ones_array = np.ones_like(original_array)
print (ones_array)

# qn6
import numpy as np
new_list = [1,2,3,4]
array = np.array(new_list)
print(array)

# qn2.1
import numpy as np
array = np.arange(10, 50)
print("Array with values from 10 to 49:")
print(array)

# qn2.2
import numpy as np
array = np.arange(9)
matrix = array.reshape(3,3)
print(matrix)

# qn2.3
import numpy as np
identity_matrix = np.eye(3)
print(identity_matrix)

# qn2.4
import numpy as np
random_array = np.random.random(30)
mean_value = random_array.mean()
print(mean_value)

# qn2.5
import numpy as np
random_array = np.random.random((10,10))
min_value = random_array.min()
max_value = random_array.max()
print("10*10 Random Array:" )
print(random_array)
print("minimum value:")
print(min_value)
print("maximum value:")
print(max_value)

# qn2.6
import numpy as np
zero_array = np.zeros(10)
zero_array[4]=1
print(zero_array)

# qn2.7
import numpy as np
arr = np.array([1,2,0,0,4,0])
reversed_arr = arr[::-1]
print(reversed_arr)

#qn8
import numpy as np
n= 4
arr = np.ones((n,n),dtype= int)
arr[1:-1, 1:-1] =0
print(arr)

# qn9
# Create a 8X8 matrix and fill it with a checkerboard pattern.
import numpy as np
n = 8
matrix = np.zeros((n, n), dtype=int)
matrix[::2, ::2] = 1
matrix[1::2, 1::2] = 1
print(matrix)

#qn3.1
import numpy as np
x = np.array([[1, 2], [3, 5]])
y = np.array([[5, 6], [7, 8]])
result = x + y
print(result)

#qn3.2
import numpy as np
x = np.array([[1, 2], [3, 5]])
y = np.array([[5, 6], [7, 8]])
result = x - y
print(result)

#qn3.3
import numpy as np
x = np.array([[1, 2], [3, 5]])
y = np.array([[5, 6], [7, 8]])
x_result = x * 5
y_result = y * 8
print("x = \n", x_result)
print("y = \n",y_result)

#qn3.4:
import numpy as np
x = np.array([[1, 2], [3, 5]])
y = np.array([[5, 6], [7, 8]])
x_squared = np.square(x)
y_squared = np.square(y)
print(" x=\n", x_squared)
print("y=\n",y_squared)

#qn3.5
import numpy as np
v = np.array([9,10])
w = np.array([11,12])
x = np.array([[1,2],
              [3,5]])
y = np.array([[5,6]
            , [7,8]])

result1 = np.dot(v,w)
result2 = np.dot(x,v)
result3 =np.dot(x,y)

print(result1)
print(result2)
print(result3)

#qn3.6
import numpy as np
x = np.array([[1, 2], [3, 5]])
y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])
concat_x_y = np.vstack((x, y))
concat_v_w = np.column_stack((v, w))
print("Concatenated x and y along rows:\n", concat_x_y)
print("Concatenated v and w along columns:\n",concat_v_w)

#qn7
# Concatenate x(and)v; if you get an error, observe and explain why did you get the error?
import numpy as np
x = np.array([[1, 2], [3, 5]])
v = np.array([9, 10])
try:
    result = np.concatenate((x, v), axis=0)
except Exception as e:
    print(f"Error: {e}")

   # All the input arrays must have same number of dimensions. The error occurred because the dimensions of x and v were incompatible for concatenation.

#prb4
import numpy as np

A = np.array([[3, 4], [7, 8]])
B = np.array([[5, 3], [2, 1]])

A_inv = np.linalg.inv(A)
result_A_A_inv = np.dot(A, A_inv)
I = np.eye(2)
print("A * A^-1 =\n", result_A_A_inv)
print("Identity Matrix I =\n", I)

AB = np.dot(A, B)
BA = np.dot(B, A)
print("AB =\n", AB)
print("BA =\n", BA)
print("AB != BA")

AB_T = np.transpose(AB)
B_T_A_T = np.dot(np.transpose(B), np.transpose(A))
print("Transpose of AB = (AB)^T:\n", AB_T)
print("B^T * A^T:\n", B_T_A_T)
print("AB^T = B^TA^T")

import numpy as np

A = np.array([[2, -3, 1],
              [1, -1, 2],
              [3, 1, -1]])
B = np.array([-1, -3, 9])
A_inv = np.linalg.inv(A)
X = np.dot(A_inv, B)
print("Solution for [x, y, z]:",X)