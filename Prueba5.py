# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:22:31 2019

@author: silva
"""


from pydub import AudioSegment
from pydub.playback import play
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
import csv
import sounddevice as sd

#----------------Vocal 1---------------------
archivo1 = 'AudioI10.wav'
fs, Y = waves.read(archivo1)
#Audio1 = AudioSegment.from_wav("Voc_A.wav")
#play(Audio1)

tam=len(Y)
Y1 = np.abs(Y)
#Y2 = Y1[:,0]

N = len(Y)
Nf = 1000
Y2=np.zeros(N)
for i in range(0,N-Nf):
    Y2[i]=np.sum(Y1[i:i+Nf])/500
ciclos=0
aux=1000
aux2=0

while ciclos==0:

    Y3 = (Y2>aux+aux2)
    X = np.array(Y3)
    X1 = X.astype(int)
    Y4 = np.abs(X1[0:len(X1)-2]-X1[1:len(X1)-1])
   
    clip = np.where(Y4)
    clip1=np.array(clip)
    clip2=clip1[0,:]
    Yj =Y[clip2[len(clip2)-2]:clip2[len(clip2)-1]]
    #Yj = Yj[:,0]
    
    #auxt=np.fft.fft(Yj)
    fm1=np.abs(np.fft.fft(Yj))
    fm2=(fm1[0:int(np.floor(len(fm1)/2))])
    #fm2=(fm1[0:tem])
    ciclos=np.floor(len(Yj)/2048)
    ciclos=int(ciclos)
    
    if ciclos==0:
        if aux2<101:
            aux2=aux2+1
        else:
            aux=aux+1000
            aux2=0


plt.plot(Y)
plt.title("Inicial")
plt.show()
plt.plot(Y2)
plt.title("Y2")
plt.show()
plt.plot(Y1,'g')
plt.twinx()
plt.plot(Y4,'m')
plt.title("Y3")
plt.show()
plt.plot(Yj)
plt.title("Yj")
plt.show()
plt.plot(fm2)
plt.title('trasnformada de fourier')
plt.show()
sd.play(Yj,fs)                
    