# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:56:18 2020

@author: silva
"""
import sys
import csv
import math
import numpy as np
import scipy as sp
import sounddevice as sd
from pydub import AudioSegment
from pydub.playback import play
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
from scipy.signal import lfilter
import librosa
from audiolazy import *


# =============================================================================
# def CLPC(x,M):
#      n=x.size;
#      if(n==0):
#          print("el arreglo esta vacio")
#      aux=ceil(log2(np.abs(2*n-1)));   
#      X=np.fft.fft(x,2**aux);
#      R=np.fft.ifft(abs(X)**2);
#      R=R/n
#      ldfilt = levinson_durbin(R, M)     
#      return ldfilt
# def levinson_1d(r, order):
#     """Levinson-Durbin recursion, to efficiently solve symmetric linear systems
#     with toeplitz structure.
#  
#     Parameters
#     ---------
#     r : array-like
#         input array to invert (since the matrix is symmetric Toeplitz, the
#         corresponding pxp matrix is defined by p items only). Generally the
#         autocorrelation of the signal for linear prediction coefficients
#         estimation. The first item must be a non zero real.
#  
#     Notes
#     ----
#     This implementation is in python, hence unsuitable for any serious
#     computation. Use it as educational and reference purpose only.
#  
#     Levinson is a well-known algorithm to solve the Hermitian toeplitz
#     equation:
#  
#                        _          _
#         -R[1] = R[0]   R[1]   ... R[p-1]    a[1]
#          :      :      :          :      *  :
#          :      :      :          _      *  :
#         -R[p] = R[p-1] R[p-2] ... R[0]      a[p]
#                        _
#     with respect to a (  is the complex conjugate). Using the special symmetry
#     in the matrix, the inversion can be done in O(p^2) instead of O(p^3).
#     """
#     r = np.atleast_1d(r)
#     if r.ndim > 1:
#         raise ValueError("Only rank 1 are supported for now.")
#  
#     n = r.size
#     if n < 1:
#         raise ValueError("Cannot operate on empty array !")
#     elif order > n - 1:
#         raise ValueError("Order should be <= size-1")
#  
#     if not np.isreal(r[0]):
#         raise ValueError("First item of input must be real.")
#     elif not np.isfinite(1/r[0]):
#         raise ValueError("First item should be != 0")
#  
#     # Estimated coefficients
#     a = np.empty(order+1, r.dtype)
#     # temporary array
#     t = np.empty(order+1, r.dtype)
#     # Reflection coefficients
#     k = np.empty(order, r.dtype)
#  
#     a[0] = 1.
#     e = r[0]
#  
#     for i in xrange(1, order+1):
#         acc = r[i]
#         for j in range(1, i):
#             acc += a[j] * r[i-j]
#         k[i-1] = -acc / e
#         a[i] = k[i-1]
#  
#         for j in range(order):
#             t[j] = a[j]
#  
#         for j in range(1, i):
#             a[j] += k[i-1] * np.conj(t[i-j])
#  
#         e *= 1 - k[i-1] * np.conj(k[i-1])
#  
#     return a, e, k
# 
# def lpc_ref(signal, order):
#     """Compute the Linear Prediction Coefficients.
#  
#     Return the order + 1 LPC coefficients for the signal. c = lpc(x, k) will
#     find the k+1 coefficients of a k order linear filter:
#  
#       xp[n] = -c[1] * x[n-2] - ... - c[k-1] * x[n-k-1]
#  
#     Such as the sum of the squared-error e[i] = xp[i] - x[i] is minimized.
#  
#     Parameters
#     ----------
#     signal: array_like
#         input signal
#     order : int
#         LPC order (the output will have order + 1 items)
#  
#     Notes
#     ----
#     This is just for reference, as it is using the direct inversion of the
#     toeplitz matrix, which is really slow"""
#     if signal.ndim > 1:
#         raise ValueError("Array of rank > 1 not supported yet")
#     if order > signal.size:
#         raise ValueError("Input signal must have a lenght >= lpc order")
#  
#     if order > 0:
#         p = order + 1
#         r = np.zeros(p, signal.dtype)
#         # Number of non zero values in autocorrelation one needs for p LPC
#         # coefficients
#         nx = np.min([p, signal.size])
#         x = np.correlate(signal, signal, 'full')
#         r[:nx] = x[signal.size-1:signal.size+order]
#         phi = np.dot(sp.linalg.inv(sp.linalg.toeplitz(r[:-1])), -r[1:])
#         return np.concatenate(([1.], phi))
#     else:
#         return np.ones(1, dtype = signal.dtype)
# 
Archivo1 = 'Julian_E1.wav'
fs, Y = waves.read(Archivo1);
x=(Y[:,0]+Y[:,1])/2;
x=x/32767
N = len(x)
windows = np.hamming(N);
xJ = x*windows;
xJa=xJ
xJ = lfilter([1],[1.,0.63],xJ)
Al= librosa.lpc(xJ,16)
filt=lpc.autocor(xJ,16)    
Aa=filt.numerator
n=x.size
aux=ceil(log2(np.abs(2*n-1)));   
X=np.fft.fft(xJ,2**aux);
R=np.fft.ifft(abs(X)**2);
R=R/n
ldfilt = levinson_durbin(R,16) 
#[aa,ee,kk]=levinson_1d(R,16)
#AAA=lpc_ref(R,16)   
#A=CLPC(xJ,16)
print(ldfilt)
print('/n')
print(Aa)
print('/n')
print(Al)
print('/n')
#print(aa)
#print('/n')
#print(AAA)
#print('/n')

#fs=44100
#A=np.array([1,-3.5730,6.3443,-8.8183,10.7441,-10.5098,8.0785,-4.5481,0.5130,2.8291,-4.7091,5.1628,-4.3229,2.9719,-1.7732,0.7865,-0.1704])
rts = np.roots(Al)
rts = rts[np.imag(rts)>=0]
angz = np.arctan2(np.imag(rts),np.real(rts))
fqrs = angz * (fs/(2*math.pi))
s=sorted(range(len(fqrs)),key=lambda k: fqrs[k])
fqrs=sorted(fqrs)
print (fqrs)
bw=np.array(-1/2*(fs/(2*np.pi))*np.log( np.absolute (rts[s])))
n=0
formants=np.zeros(8) 
for i in range (0,len(fqrs)):
 	if(fqrs[i]>90 and bw[i]<400):
 		formants[n]=fqrs[i]
 		n+=1
  
print (formants)
# plt.plot(x)
# plt.title("Señal de entrada")
# plt.show()
# plt.title("ventana de hamming")
# plt.plot(x,'g')
# plt.plot (windows,'r')
# plt.plot(xJ,'b')
# plt.show()
# =============================================================================
#sd.play(xJ,fs) 

