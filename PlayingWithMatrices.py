# Playing With Matrices
import numpy as np
import random as rd


# Array Initialization
rows = int(input("Enter number of rows : "))
cols = int(input("Enter number of columns : "))

arr1 = np.zeros((rows,cols))
arr2 = np.zeros((rows,cols))

for row in range(rows):
    for col in range(cols):
        arr1[row][col] = rd.randint(1,100)
        arr2[row][col] = rd.randint(1,100)

# print(arr1.dot(arr2))  #In-built func

print("\nMatrix 1 : ")
print(arr1)

print("\nMatrix 2 : ")
print(arr2)

result = np.zeros((rows,cols))
for i in range(len(arr1)):
    for j in range(len(arr1[0])):
        result[i][j] = arr1[i][j] + arr2[i][j]

print("\nSum of both Matrices : ")
print(result)


# Multiplication of 2 Matrices
mul = np.zeros((rows,cols))
for i in range(len(arr1)):
    for j in range(len(arr2[0])):   # col of y
        for k in range(len(arr2)):   # col row of y
            mul[i][j] += arr1[i][k] * arr2[k][j]

print("\nMultiplication of both Matrices : ")
print(mul)


# Transposing Resultant Matrix
transpose = np.zeros((rows,cols))
for i in range(len(result)):
    for j in range(len(result[0])):
        transpose[j][i] = result[i][j]

print("\nTransposing a Matrix...")
print("Transposed Matrix : ")
print(transpose)
print("\n")