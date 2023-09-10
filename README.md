# Project3-MatrixMul
August 27, 2023

**Goal.** Given two matrices in a text file, find their multiplication and provide the result both in the screen and append to the given file. 
Input: A matrix is given in the following format: the first line provides the number of rows and columns, and the second line provides the inputs in a serialized list, that is, the matrix entries are expressed from left to right row-wise. As an example,

`
2 3
1 2 3 4 5 6
`
means
`
[[1, 2, 3],
[4, 5, 6]]
`

Our text file will contain 4 lines for two matrices. As an example,
`
2 3
1 2 3 4 5 6
3 2
6 5 4 3 2 1
`

Then, their multiplication will be appended to this file as follows:
`
2 2
20 14 56 41
`

Need to know:
- How to read lines from a file and split wrt whitespace
- How to convert string to numbers
- How to convert a single list to nested list (like matrices), and vice versa
- How to write a program for matrix multiplication
- How to print the result on the screen
- How to append lines to a file
Btw, you can use [OnlineMatrixCalculator](https://matrix.reshish.com/multiplication.php as an online matrix multiplication calculator). You can also use [programiz](https://www.programiz.com/python-programming/examples/multiply-matrix) for matrix multiplication.
