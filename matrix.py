# Matrix Multiplication
# Input A and B matrices
# Output C = A * B
def matrixmul(A, B):
  # Get the dimensions of A and B
  rA, cA = len(A), len(A[0])
  rB, cB = len(B), len(B[0])
  
  if (cA != rB):
    print("Dimension error")
    return 0

  # Dimensions of A * B = (rA, cB)
  # Initialize zero matrix
  C = [[0 for j in range(cB)] for i in range(rA)]

  # iterate through rows of A
  for i in range(rA):
    for j in range(cB):
      for k in range(rB):
        C[i][j] += A[i][k] * B[k][j]

  return C
