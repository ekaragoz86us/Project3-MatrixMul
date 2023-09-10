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
