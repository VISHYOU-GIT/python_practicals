def matrix_multiply(A, B):

    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        raise ValueError("Matrix dimensions incompatible for multiplication")

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

if __name__ == "__main__":
    
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    B = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]

    result = matrix_multiply(A, B)

   
    print("Matrix A:")
    for row in A:
        print(row)

    print("\nMatrix B:")
    for row in B:
        print(row)

    print("\nResult of A × B:")
    for row in result:
        print(row)

"""
ALGORITHM:
1. Check if matrices can be multiplied (columns of A = rows of B)
2. Initialize result matrix with zeros
3. For each row i in matrix A:
   - For each column j in matrix B:
     - For each element k: result[i][j] += A[i][k] * B[k][j]
4. Return the result matrix

EXAMPLE OUTPUT:
Matrix A:
[1, 2, 3]
[4, 5, 6]

Matrix B:
[7, 8]
[9, 10]
[11, 12]

Result of A × B:
[58, 64]
[139, 154]

Mathematical Formula: C[i][j] = Σ(A[i][k] × B[k][j]) for k from 0 to n-1
Time Complexity: O(m × n × p) where A is m×n and B is n×p
Space Complexity: O(m × p) for result matrix
Condition: Number of columns in A must equal number of rows in B
"""
