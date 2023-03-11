# -*- coding: utf-8 -*-
"""
Created on Sun May 24 15:29:45 2020

@author: silva
"""
import numpy as np
import scipy.linalg
from numpy import ceil, log2
from collections import deque
from audiolazy import *



# =============================================================================
# 
# 
# def CLPC(x,N):
#     n=x.size;
#     if(n==0):
#         print("el arreglo esta vacio")
#     aux=ceil(log2(np.abs(2*n-1)));   
#     X=np.fft.fft(x,2**aux);
#     R=np.fft.ifft(abs(X)**2);
#     R=R/n
# #    ldfilt = levinson_durbin(R, N)
#     a=scipy.linalg.solve_toeplitz(R,N)
#         
# 
# =============================================================================

x=np.array([1,2,3,4,5,6,7,8,9])
n=x.size
N=16
aux=int(ceil(log2(np.abs(2*n-1))));   
X=np.fft.fft(x,2**aux);
R=np.fft.ifft(abs(X)**2);
R=R/n
ldfilt = levinson_durbin(R, N)
#a=scipy.linalg.solve_toeplitz(R,N)        
