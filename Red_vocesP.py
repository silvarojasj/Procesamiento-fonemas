# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 17:18:21 2018

@author: silva
"""

import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
from keras.models import model_from_json
import subprocess

json_file = open('red_vocalesE.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("red_vocalesE.h5")
print("Loaded model from disk")

entrada=np.zeros([1,50000])

archivo1 = 'AudioA39.wav'
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
    fm1=np.abs(np.fft.fft(Yj))
    fm2=(fm1[0:int(np.floor(len(fm1)/2))])
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
tamm1=len(Yj)

entrada[0,0:tamm1]=Yj[0:tamm1]
result = loaded_model.predict(entrada)
result=np.array(result)
print(result)

indice_max = result.argmax()
if indice_max==0:
    print("A")
    subprocess.call('espeak -ves "a" ',shell=True)

if indice_max==1:
    print("E")
    subprocess.call('espeak -ves "e" ',shell=True)
if indice_max==2:
    print("I")
    subprocess.call('espeak -ves "i" ',shell=True)

if indice_max==3:
    print("O")
    subprocess.call('espeak -ves "o" ',shell=True)
if indice_max==4:
    print("U")
    subprocess.call('espeak -ves "u" ',shell=True)
    