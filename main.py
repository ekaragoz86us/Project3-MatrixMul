# File operations in Python
# * https://www.w3schools.com/python/python_file_open.asp
# * https://www.geeksforgeeks.org/reading-writing-text-files-python/

#f = open("dosya.ismi", "flag-r-w-a")
#f.read()
#f.read(10)  -- not necessary
#f.readline() -- satiri okur ve string olarak dondurur, sonraki satira gecer
#f.write("string...") -- dosyanin sonuna yaz eger dosya 'a' ile acilmissa
#f.write("string...") -- bos dosyaya yazar eger dosya 'w' ile acilmissa
#f.close()

myFileName = "matrix.txt"
f = open(myFileName, "r")

# Tek tek satir okuma
#Adim = f.readline()
#Adata = f.readline()
#Bdim = f.readline()
#Bdata = f.readline()

# Butun satirlar liste olarak
Adim, Adata, Bdim, Bdata = f.readlines()

print("Dimension of A ", Adim)
print("Data in A ", Adata)
print("Dimension of B", Bdim)
print("Data in B ", Bdata)

Adim = Adim.rstrip('\n')
#Adim = Adim.replace('\n', '')
#Adim = Adim.strip('\n')
Adim = Adim.split(" ")
rA, cA = int(Adim[0]), int(Adim[1])
#print(rA, cA)

Bdim = Bdim.rstrip('\n')
Bdim = Bdim.split(" ")
rB, cB = int(Bdim[0]), int(Bdim[1])

Adata = (Adata.rstrip('\n')).split(" ")
Bdata = (Bdata.rstrip('\n')).split(" ")
#print(Adata)
#print(Bdata)

f.close()

#     c0 c1 c2
# r0  1  2  3
# r1  4  5  6
#   0       1      2      3     4      5
# (0,0), (0,1), (0,2), (1,0), (1,1), (1,2)
# rA = 2 --> i = 0, 1
# cA = 3 --> j = 0, 1, 2
# (i,j) <--> cA * i + j

A = [[int(Adata[cA * i + j]) for j in range(cA)] for i in range(rA)]
print("A =", A)

B = [[int(Bdata[cB * i + j]) for j in range(cB)] for i in range(rB)]
print("B =", B)

# Call matrix multiplication function
from matrix import matrixmul
C = matrixmul(A, B)
print("C =", C)

rC, cC = len(C), len(C[0])
Cdata = []
for i in range(rC):
  Cdata += C[i]
Cdata = [str(_) for _ in Cdata]
Cdata = ' '.join(Cdata)

# Open the same file and append the resulting matrix in the end
f = open(myFileName, "a")
f.write('\n' + str(rC) + ' ' + str(cC) + '\n')
f.write(Cdata)
f.close()
