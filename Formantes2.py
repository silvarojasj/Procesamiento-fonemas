# -*- coding: utf-8 -*-
"""
Created on Wed May 27 11:29:55 2020

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
from scipy.signal import lfilter
import scipy.io.wavfile as waves
import librosa
import Grabar_Tesis as Gt
from audiolazy import *


vocales=np.array([789.8,870.4,399.2,2276.8,242.6,2831.2,539.8,5956.4,325.8,5992.2])
Gt.Grabar();

Archivo1 = 'Audio.wav'
fs, Y = waves.read(Archivo1);
#x=(Y[:,0]+Y[:,1])/2;
x=Y
x=x/32767
N = len(x)
windows = np.hamming(N);
xJ = x*windows;
xJa=xJ
xJ = lfilter([1],[1.,0.63],xJ)
filt=lpc.autocor(xJ,16) 
A=filt.numerator
#Al= librosa.lpc(xJ,16)
rts = np.roots(A)
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
plt.scatter(vocales[0],vocales[1],color="b",label="A")
plt.scatter(vocales[2],vocales[3],color="purple",label="E")
plt.scatter(vocales[4],vocales[5],color="r",label="I")
plt.scatter(vocales[6],vocales[7],color="orange",label="O")
plt.scatter(vocales[8],vocales[9],color="maroon",label="U" )
plt.scatter(formants[0],formants[1],color="k",label="Vocal" )
plt.legend(loc='right')
plt.grid()
plt.show()

resA=np.abs(formants[0]-vocales[0])+np.abs(formants[1]-vocales[1])
resE=np.abs(formants[0]-vocales[2])+np.abs(formants[1]-vocales[3])
resI=np.abs(formants[0]-vocales[4])+np.abs(formants[1]-vocales[5])
resO=np.abs(formants[0]-vocales[6])+np.abs(formants[1]-vocales[7])
resU=np.abs(formants[0]-vocales[8])+np.abs(formants[1]-vocales[9])



if(resA<resE and resA<resI and resA<resO and resA<resU):
        print('La vocal es la A')
elif (resE<resI and resE<resO and resE<resU):
          print('la vocal es la E')
elif(resI<resO and resI<resU):
        print('la vocal es la I')
elif(resO<resU):
        print('la vocal es la O')
else :
    print('la vocal es la U')

    