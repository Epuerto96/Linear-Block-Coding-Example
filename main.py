#
#/BER = sum(xor(m*,m))/ (#m)
# BER <= E
#
import numpy as np
import matplotlib.pyplot as plt

# create message bits
n = 30000
m = np.random.randint(low=0,high=2, size=n).astype('bool')
print("Message Bits\n", m)

# Create code bits
r = 5

c = np.tile(m,(r,1)) # takes the matrix and tiles it

print("Codewords for R = 5\n",c)


# txt through bsc
epsilon = 10**-.3
errorBits = np.random.rand(c.shape[0],c.shape[1]) < epsilon
print("Error Bits\n",errorBits)
cHat = np.logical_xor(errorBits,c)
print("cHat\n",cHat)

# decode
sums = np.sum(cHat, axis=0)
mHat = sums>r/2
print("mHat\n",mHat)

#compute BER

BER = np.sum(np.logical_xor(m,mHat))/n
print("ber\n",BER)

# compare output of decoding with original message bits
