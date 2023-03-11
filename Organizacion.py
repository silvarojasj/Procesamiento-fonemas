# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:57:37 2020

@author: silva
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
import csv
import sounddevice as sd


def procesamiento(Ya,cont,voc):
    Y1a = np.abs(Ya)
    #Y2 = Y1[:,0]
    Na = len(Ya)
    Nf = 1000
    Y2a=np.zeros(Na)
    for i in range(0,Na-Nf):
        Y2a[i]=np.sum(Y1a[i:i+Nf])/500
    ciclosa=0
    auxa=4000
    aux2a=0
    
    while ciclosa==0:
    
        Y3a = (Y2a>auxa+aux2a)
        Xa = np.array(Y3a)
        X1a = Xa.astype(int)
        Y4a = np.abs(X1a[0:len(X1a)-2]-X1a[1:len(X1a)-1])
       
        clipa = np.where(Y4a)
        clip1a=np.array(clipa)
        clip2a=clip1a[0,:]
        Yja =Ya[clip2a[len(clip2a)-2]:clip2a[len(clip2a)-1]]
        Yja = Yja[:,0]
        #auxt=np.fft.fft(Yj)
        fm1a=np.abs(np.fft.fft(Yja))
        fm2a=(fm1a[0:int(np.floor(len(fm1a)/2))])
        #fm2=(fm1[0:tem])
        ciclosa=np.floor(len(Yja)/2048)
        ciclosa=int(ciclosa)
        
        if ciclosa==0:
            if aux2a<101:
                aux2a=aux2a+1
            else:
                auxa=auxa+1000
                aux2a=0
    
    
    plt.plot(Ya)
    plt.title("Inicial a")
    plt.show()
    plt.plot(Y2a)
    plt.title("Y2 a")
    plt.show()
    plt.plot(Y1a,'g')
    plt.twinx()
    plt.plot(Y4a,'m')
    plt.title("Y3 a")
    plt.show()
    plt.plot(Yja)
    plt.title("Yj a")
    plt.show()
    plt.plot(fm2a)
    plt.title('trasnformada de fourier a')
    plt.show()
    #sd.play(Yj,fs) 
    if voc==6:
        voc=1
    tamm1=len(Yja)          
    entrenamiento[cont,0:tamm1]=Yja[0:tamm1]
    if voc==1:
        target[cont]=0
        voc=voc+1
    elif voc ==2 :
        target[cont]=1
        voc=voc+1
    elif voc==3:
        target[cont]=2
        voc=voc+1
    elif voc ==4:
        target[cont]=3
        voc=voc+1
    elif voc==5:
        target[cont]=4
        voc=voc+1
    cont+=1
    
    return (entrenamiento,target,cont,voc)
#----------------Vocal 1---------------------
entrenamiento=np.zeros([45,50000])
target=np.zeros(45)
cont=0
voc=1
nvoc=1
nombre='Julian_'
#nombre='Audio'
vocalA='A'
vocalE='E'
vocalI='I'
vocalO='O'
vocalU='U'
ext='.wav'
for nvoc in range (1,9):
    archivo=nombre+vocalA+str(nvoc)+ext
    fs,Ya=waves.read(archivo)
    (entrenamiento,target,cont,voc)=procesamiento(Ya,cont,voc)
    archivo=nombre+vocalE+str(nvoc)+ext
    fs,Ya=waves.read(archivo)
    (entrenamiento,target,cont,voc)=procesamiento(Ya,cont,voc)
    archivo=nombre+vocalI+str(nvoc)+ext
    fs,Ya=waves.read(archivo)
    (entrenamiento,target,cont,voc)=procesamiento(Ya,cont,voc)
    archivo=nombre+vocalO+str(nvoc)+ext
    fs,Ya=waves.read(archivo)
    (entrenamiento,target,cont,voc)=procesamiento(Ya,cont,voc)
    archivo=nombre+vocalU+str(nvoc)+ext
    fs,Ya=waves.read(archivo)
    (entrenamiento,target,cont,voc)=procesamiento(Ya,cont,voc)
    

myFile = open('tablaP.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(entrenamiento.transpose())
    
np.savetxt('vectorP.dat', target)
