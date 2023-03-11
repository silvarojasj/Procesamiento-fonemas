# -*- coding: utf-8 -*-
"""
from pydub import AudioSegment
from pydub.playback import play
Created on Sun Sep 29 11:59:46 2019

@author: silva
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
import csv
import sounddevice as sd

#----------------Vocal 1---------------------
archivo1 = 'Julian_A1.wav'
fs, Ya = waves.read(archivo1)
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
tamm1=len(Yja)          
entrenamiento=np.zeros([20,50000])
target=np.zeros(20)
cont=0
entrenamiento[cont,0:tamm1]=Yja[0:tamm1]
target[cont]=0
cont+=1 

#----------------Vocal 2---------------------
archivo2 = 'Julian_E1.wav'
fs, Ye = waves.read(archivo2)

Y1e = np.abs(Ye)
#Y2 = Y1[:,0]
Ne = len(Ye)
Nf = 1000
Y2e=np.zeros(Ne)
for i in range(0,Ne-Nf):
    Y2e[i]=np.sum(Y1e[i:i+Nf])/500
ciclose=0
auxe=4000
aux2e=0

while ciclose==0:

    Y3e = (Y2e>auxe+aux2e)
    Xe = np.array(Y3e)
    X1e = Xe.astype(int)
    Y4e = np.abs(X1e[0:len(X1e)-2]-X1e[1:len(X1e)-1])
   
    clipe = np.where(Y4e)
    clip1e=np.array(clipe)
    clip2e=clip1e[0,:]
    Yje =Ye[clip2e[len(clip2e)-2]:clip2e[len(clip2e)-1]]
    Yje = Yje[:,0]
    #auxt=np.fft.fft(Yj)
    fm1e=np.abs(np.fft.fft(Yje))
    fm2e=(fm1e[0:int(np.floor(len(fm1e)/2))])
    #fm2=(fm1[0:tem])
    ciclose=np.floor(len(Yje)/2048)
    ciclose=int(ciclose)
    
    if ciclose==0:
        if aux2e<101:
            aux2e=aux2e+1
        else:
            auxe=auxe+1000
            aux2e=0


plt.plot(Ye)
plt.title("Inicial e")
plt.show()
plt.plot(Y2e)
plt.title("Y2 e")
plt.show()
plt.plot(Y1e,'g')
plt.twinx()
plt.plot(Y4e,'m')
plt.title("Y3 e")
plt.show()
plt.plot(Yje)
plt.title("Yj")
plt.show()
plt.plot(fm2e)
plt.title('trasnformada de fourier e')
plt.show()
tamm2=len(Yje)
entrenamiento[cont,0:tamm2]=Yje[0:tamm2]
target[cont]=1
cont+=1
#----------------Vocal 3---------------------
archivo3 = 'Julian_I1.wav'
fs, Yi = waves.read(archivo3)

Y1i = np.abs(Yi)
#Y2 = Y1[:,0]
Ni = len(Yi)
Nf = 1000
Y2i=np.zeros(Ni)
for i in range(0,Ni-Nf):
    Y2i[i]=np.sum(Y1i[i:i+Nf])/500
ciclosi=0
auxi=4000
aux2i=0

while ciclosi==0:

    Y3i = (Y2i>auxi+aux2i)
    Xi = np.array(Y3i)
    X1i = Xi.astype(int)
    Y4i = np.abs(X1i[0:len(X1i)-2]-X1i[1:len(X1i)-1])
   
    clipi = np.where(Y4i)
    clip1i=np.array(clipi)
    clip2i=clip1i[0,:]
    Yji =Yi[clip2i[len(clip2i)-2]:clip2i[len(clip2i)-1]]
    Yji = Yji[:,0]
    #auxt=np.fft.fft(Yj)
    fm1i=np.abs(np.fft.fft(Yji))
    fm2i=(fm1i[0:int(np.floor(len(fm1i)/2))])
    #fm2=(fm1[0:tem])
    ciclosi=np.floor(len(Yji)/2048)
    ciclosi=int(ciclosi)
    
    if ciclosi==0:
        if aux2i<101:
            aux2i=aux2i+1
        else:
            auxi=auxi+1000
            aux2i=0


plt.plot(Yi)
plt.title("Inicial i")
plt.show()
plt.plot(Y2i)
plt.title("Y2 i")
plt.show()
plt.plot(Y1i,'g')
plt.twinx()
plt.plot(Y4i,'m')
plt.title("Y3 i")
plt.show()
plt.plot(Yji)
plt.title("Yj i")
plt.show()
plt.plot(fm2i)
plt.title('trasnformada de fourier i')
plt.show()
tamm3=len(Yji)
entrenamiento[cont,0:tamm3]=Yji[0:tamm3]
target[cont]=2
cont+=1
#----------------Vocal 4---------------------
archivo4 = 'Julian_O1.wav'
fs, Yo = waves.read(archivo4)

Y1o = np.abs(Yo)
#Y2 = Y1[:,0]
No = len(Yo)
Nf = 1000
Y2o=np.zeros(No)
for i in range(0,No-Nf):
    Y2o[i]=np.sum(Y1o[i:i+Nf])/500
cicloso=0
auxo=4000
aux2o=0

while cicloso==0:

    Y3o = (Y2o>auxo+aux2o)
    Xo = np.array(Y3o)
    X1o = Xo.astype(int)
    Y4o = np.abs(X1o[0:len(X1o)-2]-X1o[1:len(X1o)-1])
   
    clipo = np.where(Y4o)
    clip1o=np.array(clipo)
    clip2o=clip1o[0,:]
    Yjo =Yo[clip2o[len(clip2o)-2]:clip2o[len(clip2o)-1]]
    Yjo = Yjo[:,0]
    #auxt=np.fft.fft(Yj)
    fm1o=np.abs(np.fft.fft(Yjo))
    fm2o=(fm1o[0:int(np.floor(len(fm1o)/2))])
    #fm2=(fm1[0:tem])
    cicloso=np.floor(len(Yjo)/2048)
    cicloso=int(cicloso)
    
    if cicloso==0:
        if aux2o<101:
            aux2o=aux2o+1
        else:
            auxo=auxo+1000
            aux2o=0


plt.plot(Yo)
plt.title("Inicial o")
plt.show()
plt.plot(Y2o)
plt.title("Y2 o")
plt.show()
plt.plot(Y1o,'g')
plt.twinx()
plt.plot(Y4o,'m')
plt.title("Y3 o")
plt.show()
plt.plot(Yjo)
plt.title("Yj")
plt.show()
plt.plot(fm2o)
plt.title('trasnformada de fourier o')
plt.show()
tamm4=len(Yjo)
entrenamiento[cont,0:tamm4]=Yjo[0:tamm4]
target[cont]=3
cont+=1
#----------------Vocal 5---------------------
archivo5 = 'Julian_U1.wav'
fs, Yu = waves.read(archivo5)

Y1u = np.abs(Yu)
#Y2 = Y1[:,0]
Nu = len(Yu)
Nf = 1000
Y2u=np.zeros(Nu)
for i in range(0,Nu-Nf):
    Y2u[i]=np.sum(Y1u[i:i+Nf])/500
ciclosu=0
auxu=4000
aux2u=0

while ciclosu==0:

    Y3u = (Y2u>auxu+aux2u)
    Xu = np.array(Y3u)
    X1u = Xu.astype(int)
    Y4u = np.abs(X1u[0:len(X1u)-2]-X1u[1:len(X1u)-1])
   
    clipu = np.where(Y4u)
    clip1u=np.array(clipu)
    clip2u=clip1u[0,:]
    Yju =Yu[clip2u[len(clip2u)-2]:clip2u[len(clip2u)-1]]
    Yju = Yju[:,0]
    #auxt=np.fft.fft(Yj)
    fm1u=np.abs(np.fft.fft(Yju))
    fm2u=(fm1u[0:int(np.floor(len(fm1u)/2))])
    #fm2=(fm1[0:tem])
    ciclosu=np.floor(len(Yju)/2048)
    ciclosu=int(ciclosu)
    
    if ciclosu==0:
        if aux2u<101:
            aux2u=aux2u+1
        else:
            auxu=auxu+1000
            aux2u=0


plt.plot(Yu)
plt.title("Inicial u")
plt.show()
plt.plot(Y2u)
plt.title("Y2 u")
plt.show()
plt.plot(Y1u,'g')
plt.twinx()
plt.plot(Y4u,'m')
plt.title("Y3 u")
plt.show()
plt.plot(Yju)
plt.title("Yj u")
plt.show()
plt.plot(fm2u)
plt.title('trasnformada de fourier u')
plt.show()
tamm5=len(Yju)
entrenamiento[cont,0:tamm5]=Yju[0:tamm5]
target[cont]=4
cont+=1

#----------------Vocal 6---------------------
archivo6 = 'Julian_A2.wav'
fs, Ya2 = waves.read(archivo6)

Y1a2 = np.abs(Ya2)
#Y2 = Y1[:,0]
Na2 = len(Ya2)
Nf = 1000
Y2a2=np.zeros(Na2)
for i in range(0,Na2-Nf):
    Y2a2[i]=np.sum(Y1a2[i:i+Nf])/500
ciclosa2=0
auxa2=4000
aux2a2=0

while ciclosa2==0:

    Y3a2 = (Y2a2>auxa2+aux2a2)
    Xa2 = np.array(Y3a2)
    X1a2 = Xa2.astype(int)
    Y4a2 = np.abs(X1a2[0:len(X1a2)-2]-X1a2[1:len(X1a2)-1])
   
    clipa2 = np.where(Y4a2)
    clip1a2=np.array(clipa2)
    clip2a2=clip1a2[0,:]
    Yja2 =Ya2[clip2a2[len(clip2a2)-2]:clip2a2[len(clip2a2)-1]]
    Yja2 = Yja2[:,0]
    #auxt=np.fft.fft(Yj)
    fm1a2=np.abs(np.fft.fft(Yja2))
    fm2a2=(fm1a2[0:int(np.floor(len(fm1a2)/2))])
    #fm2=(fm1[0:tem])
    ciclosa2=np.floor(len(Yja2)/2048)
    ciclosa2=int(ciclosa2)
    
    if ciclosa2==0:
        if aux2a2<101:
            aux2a2=aux2a2+1
        else:
            auxa2=auxa2+1000
            aux2a2=0


plt.plot(Ya2)
plt.title("Inicial a")
plt.show()
plt.plot(Y2a2)
plt.title("Y2 a")
plt.show()
plt.plot(Y1a2,'g')
plt.twinx()
plt.plot(Y4a2,'m')
plt.title("Y3 a")
plt.show()
plt.plot(Yja2)
plt.title("Yj a")
plt.show()
plt.plot(fm2a2)
plt.title('trasnformada de fourier a')
plt.show()
#sd.play(Yj,fs)      
tamm6=len(Yja2)          
entrenamiento[cont,0:tamm6]=Yja2[0:tamm6]
target[cont]=0
cont+=1 
#----------------Vocal 7---------------------
archivo7 = 'Julian_E2.wav'
fs, Ye2 = waves.read(archivo7)

Y1e2 = np.abs(Ye2)
#Y2 = Y1[:,0]
Ne2 = len(Ye2)
Nf = 1000
Y2e2=np.zeros(Ne2)
for i in range(0,Ne2-Nf):
    Y2e2[i]=np.sum(Y1e2[i:i+Nf])/500
ciclose2=0
auxe2=4000
aux2e2=0

while ciclose2==0:

    Y3e2 = (Y2e2>auxe2+aux2e2)
    Xe2 = np.array(Y3e2)
    X1e2 = Xe2.astype(int)
    Y4e2 = np.abs(X1e2[0:len(X1e2)-2]-X1e2[1:len(X1e2)-1])
   
    clipe2 = np.where(Y4e2)
    clip1e2=np.array(clipe2)
    clip2e2=clip1e2[0,:]
    Yje2 =Ye2[clip2e2[len(clip2e2)-2]:clip2e2[len(clip2e2)-1]]
    Yje2 = Yje2[:,0]
    #auxt=np.fft.fft(Yj)
    fm1e2=np.abs(np.fft.fft(Yje2))
    fm2e2=(fm1e2[0:int(np.floor(len(fm1e2)/2))])
    #fm2=(fm1[0:tem])
    ciclose2=np.floor(len(Yje2)/2048)
    ciclose2=int(ciclose2)
    
    if ciclose2==0:
        if aux2e2<101:
            aux2e2=aux2e2+1
        else:
            auxe2=auxe2+1000
            aux2e2=0


plt.plot(Ye2)
plt.title("Inicial e")
plt.show()
plt.plot(Y2e2)
plt.title("Y2 e")
plt.show()
plt.plot(Y1e2,'g')
plt.twinx()
plt.plot(Y4e2,'m')
plt.title("Y3 e")
plt.show()
plt.plot(Yje2)
plt.title("Yj")
plt.show()
plt.plot(fm2e2)
plt.title('trasnformada de fourier e')
plt.show()
tamm7=len(Yje2)
entrenamiento[cont,0:tamm7]=Yje2[0:tamm7]
target[cont]=1
cont+=1
#----------------Vocal 8---------------------
archivo8 = 'Julian_I2.wav'
fs, Yi2 = waves.read(archivo8)

Y1i2 = np.abs(Yi2)
#Y2 = Y1[:,0]
Ni2 = len(Yi2)
Nf = 1000
Y2i2=np.zeros(Ni2)
for i in range(0,Ni2-Nf):
    Y2i2[i]=np.sum(Y1i2[i:i+Nf])/500
ciclosi2=0
auxi2=4000
aux2i2=0

while ciclosi2==0:

    Y3i2 = (Y2i2>auxi2+aux2i2)
    Xi2 = np.array(Y3i2)
    X1i2 = Xi2.astype(int)
    Y4i2 = np.abs(X1i2[0:len(X1i2)-2]-X1i2[1:len(X1i2)-1])
   
    clipi2 = np.where(Y4i2)
    clip1i2=np.array(clipi2)
    clip2i2=clip1i2[0,:]
    Yji2 =Yi2[clip2i2[len(clip2i2)-2]:clip2i2[len(clip2i2)-1]]
    Yji2 = Yji2[:,0]
    #auxt=np.fft.fft(Yj)
    fm1i2=np.abs(np.fft.fft(Yji2))
    fm2i2=(fm1i2[0:int(np.floor(len(fm1i2)/2))])
    #fm2=(fm1[0:tem])
    ciclosi2=np.floor(len(Yji2)/2048)
    ciclosi2=int(ciclosi2)
    
    if ciclosi2==0:
        if aux2i2<101:
            aux2i2=aux2i2+1
        else:
            auxi2=auxi2+1000
            aux2i2=0


plt.plot(Yi2)
plt.title("Inicial i")
plt.show()
plt.plot(Y2i2)
plt.title("Y2 i")
plt.show()
plt.plot(Y1i2,'g')
plt.twinx()
plt.plot(Y4i2,'m')
plt.title("Y3 i")
plt.show()
plt.plot(Yji2)
plt.title("Yj i")
plt.show()
plt.plot(fm2i2)
plt.title('trasnformada de fourier i')
plt.show()
tamm8=len(Yji2)
entrenamiento[cont,0:tamm8]=Yji2[0:tamm8]
target[cont]=2
cont+=1
#----------------Vocal 9---------------------
archivo9 = 'Julian_O2.wav'
fs, Yo2 = waves.read(archivo9)

Y1o2 = np.abs(Yo2)
#Y2 = Y1[:,0]
No2 = len(Yo2)
Nf = 1000
Y2o2=np.zeros(No2)
for i in range(0,No2-Nf):
    Y2o2[i]=np.sum(Y1o2[i:i+Nf])/500
cicloso2=0
auxo2=4000
aux2o2=0

while cicloso2==0:

    Y3o2 = (Y2o2>auxo2+aux2o2)
    Xo2 = np.array(Y3o2)
    X1o2 = Xo2.astype(int)
    Y4o2 = np.abs(X1o2[0:len(X1o2)-2]-X1o2[1:len(X1o2)-1])
   
    clipo2 = np.where(Y4o2)
    clip1o2=np.array(clipo2)
    clip2o2=clip1o2[0,:]
    Yjo2 =Yo2[clip2o2[len(clip2o2)-2]:clip2o2[len(clip2o2)-1]]
    Yjo2 = Yjo2[:,0]
    #auxt=np.fft.fft(Yj)
    fm1o2=np.abs(np.fft.fft(Yjo2))
    fm2o2=(fm1o2[0:int(np.floor(len(fm1o2)/2))])
    #fm2=(fm1[0:tem])
    cicloso2=np.floor(len(Yjo2)/2048)
    cicloso2=int(cicloso2)
    
    if cicloso2==0:
        if aux2o2<101:
            aux2o2=aux2o2+1
        else:
            auxo2=auxo2+1000
            aux2o2=0


plt.plot(Yo2)
plt.title("Inicial o")
plt.show()
plt.plot(Y2o2)
plt.title("Y2 o")
plt.show()
plt.plot(Y1o2,'g')
plt.twinx()
plt.plot(Y4o2,'m')
plt.title("Y3 o")
plt.show()
plt.plot(Yjo2)
plt.title("Yj")
plt.show()
plt.plot(fm2o2)
plt.title('trasnformada de fourier o')
plt.show()
tamm9=len(Yjo2)
entrenamiento[cont,0:tamm9]=Yjo2[0:tamm9]
target[cont]=3
cont+=1
#----------------Vocal 10---------------------
archivo10 = 'Julian_U2.wav'
fs, Yu2 = waves.read(archivo10)

Y1u2 = np.abs(Yu2)
#Y2 = Y1[:,0]
Nu2 = len(Yu2)
Nf = 1000
Y2u2=np.zeros(Nu2)
for i in range(0,Nu2-Nf):
    Y2u2[i]=np.sum(Y1u2[i:i+Nf])/500
ciclosu2=0
auxu2=4000
aux2u2=0

while ciclosu2==0:

    Y3u2 = (Y2u2>auxu2+aux2u2)
    Xu2 = np.array(Y3u2)
    X1u2 = Xu2.astype(int)
    Y4u2 = np.abs(X1u2[0:len(X1u2)-2]-X1u2[1:len(X1u2)-1])
   
    clipu2 = np.where(Y4u2)
    clip1u2=np.array(clipu2)
    clip2u2=clip1u2[0,:]
    Yju2 =Yu2[clip2u2[len(clip2u2)-2]:clip2u2[len(clip2u2)-1]]
    Yju2 = Yju2[:,0]
    #auxt=np.fft.fft(Yj)
    fm1u2=np.abs(np.fft.fft(Yju2))
    fm2u2=(fm1u2[0:int(np.floor(len(fm1u2)/2))])
    #fm2=(fm1[0:tem])
    ciclosu2=np.floor(len(Yju2)/2048)
    ciclosu2=int(ciclosu2)
    
    if ciclosu2==0:
        if aux2u2<101:
            aux2u2=aux2u2+1
        else:
            auxu2=auxu2+1000
            aux2u2=0


plt.plot(Yu2)
plt.title("Inicial u")
plt.show()
plt.plot(Y2u2)
plt.title("Y2 u")
plt.show()
plt.plot(Y1u2,'g')
plt.twinx()
plt.plot(Y4u2,'m')
plt.title("Y3 u")
plt.show()
plt.plot(Yju2)
plt.title("Yj u")
plt.show()
plt.plot(fm2u2)
plt.title('trasnformada de fourier u')
plt.show()
tamm10=len(Yju2)
entrenamiento[cont,0:tamm10]=Yju2[0:tamm10]
target[cont]=4
cont+=1
#----------------Vocal 11---------------------
archivo11 = 'Julian_A3.wav'
fs, Ya3 = waves.read(archivo11)

Y1a3 = np.abs(Ya3)
#Y2 = Y1[:,0]
Na3 = len(Ya3)
Nf = 1000
Y2a3=np.zeros(Na3)
for i in range(0,Na3-Nf):
    Y2a3[i]=np.sum(Y1a3[i:i+Nf])/500
ciclosa3=0
auxa3=4000
aux2a3=0

while ciclosa3==0:

    Y3a3 = (Y2a3>auxa3+aux2a3)
    Xa3 = np.array(Y3a3)
    X1a3 = Xa3.astype(int)
    Y4a3 = np.abs(X1a3[0:len(X1a3)-2]-X1a3[1:len(X1a3)-1])
   
    clipa3 = np.where(Y4a3)
    clip1a3=np.array(clipa3)
    clip2a3=clip1a3[0,:]
    Yja3 =Ya3[clip2a3[len(clip2a3)-2]:clip2a3[len(clip2a3)-1]]
    Yja3 = Yja3[:,0]
    #auxt=np.fft.fft(Yj)
    fm1a3=np.abs(np.fft.fft(Yja3))
    fm2a3=(fm1a3[0:int(np.floor(len(fm1a3)/2))])
    #fm2=(fm1[0:tem])
    ciclosa3=np.floor(len(Yja3)/2048)
    ciclosa3=int(ciclosa3)
    
    if ciclosa3==0:
        if aux2a3<101:
            aux2a3=aux2a3+1
        else:
            auxa3=auxa3+1000
            aux2a3=0


plt.plot(Ya3)
plt.title("Inicial a")
plt.show()
plt.plot(Y2a3)
plt.title("Y2 a")
plt.show()
plt.plot(Y1a3,'g')
plt.twinx()
plt.plot(Y4a3,'m')
plt.title("Y3 a")
plt.show()
plt.plot(Yja3)
plt.title("Yj a")
plt.show()
plt.plot(fm2a3)
plt.title('trasnformada de fourier a')
plt.show()
#sd.play(Yj,fs)      
tamm11=len(Yja3)
entrenamiento[cont,0:tamm11]=Yja3[0:tamm11]
target[cont]=0
cont+=1 
#----------------Vocal 12---------------------
archivo12 = 'Julian_E3.wav'
fs, Ye3 = waves.read(archivo12)

Y1e3 = np.abs(Ye3)
#Y2 = Y1[:,0]
Ne3 = len(Ye3)
Nf = 1000
Y2e3=np.zeros(Ne3)
for i in range(0,Ne3-Nf):
    Y2e3[i]=np.sum(Y1e3[i:i+Nf])/500
ciclose3=0
auxe3=4000
aux2e3=0

while ciclose3==0:

    Y3e3 = (Y2e3>auxe3+aux2e3)
    Xe3 = np.array(Y3e3)
    X1e3 = Xe3.astype(int)
    Y4e3 = np.abs(X1e3[0:len(X1e3)-2]-X1e3[1:len(X1e3)-1])
   
    clipe3 = np.where(Y4e3)
    clip1e3=np.array(clipe3)
    clip2e3=clip1e3[0,:]
    Yje3 =Ye3[clip2e3[len(clip2e3)-2]:clip2e3[len(clip2e3)-1]]
    Yje3 = Yje3[:,0]
    #auxt=np.fft.fft(Yj)
    fm1e3=np.abs(np.fft.fft(Yje3))
    fm2e3=(fm1e3[0:int(np.floor(len(fm1e3)/2))])
    #fm2=(fm1[0:tem])
    ciclose3=np.floor(len(Yje3)/2048)
    ciclose3=int(ciclose3)
    
    if ciclose3==0:
        if aux2e3<101:
            aux2e3=aux2e3+1
        else:
            auxe3=auxe3+1000
            aux2e3=0


plt.plot(Ye3)
plt.title("Inicial e")
plt.show()
plt.plot(Y2e3)
plt.title("Y2 e")
plt.show()
plt.plot(Y1e3,'g')
plt.twinx()
plt.plot(Y4e3,'m')
plt.title("Y3 e")
plt.show()
plt.plot(Yje3)
plt.title("Yj")
plt.show()
plt.plot(fm2e3)
plt.title('trasnformada de fourier e')
plt.show()
tamm12=len(Yje3)
entrenamiento[cont,0:tamm12]=Yje3[0:tamm12]
target[cont]=1
cont+=1
#----------------Vocal 3---------------------
archivo13 = 'Julian_I3.wav'
fs, Yi3 = waves.read(archivo13)

Y1i3 = np.abs(Yi3)
#Y2 = Y1[:,0]
Ni3 = len(Yi3)
Nf = 1000
Y2i3=np.zeros(Ni3)
for i in range(0,Ni3-Nf):
    Y2i3[i]=np.sum(Y1i3[i:i+Nf])/500
ciclosi3=0
auxi3=4000
aux2i3=0

while ciclosi3==0:

    Y3i3 = (Y2i3>auxi3+aux2i3)
    Xi3 = np.array(Y3i3)
    X1i3 = Xi3.astype(int)
    Y4i3 = np.abs(X1i3[0:len(X1i3)-2]-X1i3[1:len(X1i3)-1])
   
    clipi3 = np.where(Y4i3)
    clip1i3=np.array(clipi3)
    clip2i3=clip1i3[0,:]
    Yji3=Yi3[clip2i3[len(clip2i3)-2]:clip2i3[len(clip2i3)-1]]
    Yji3 = Yji3[:,0]
    #auxt=np.fft.fft(Yj)
    fm1i3=np.abs(np.fft.fft(Yji3))
    fm2i3=(fm1i3[0:int(np.floor(len(fm1i3)/2))])
    #fm2=(fm1[0:tem])
    ciclosi3=np.floor(len(Yji3)/2048)
    ciclosi3=int(ciclosi3)
    
    if ciclosi3==0:
        if aux2i3<101:
            aux2i3=aux2i3+1
        else:
            auxi3=auxi3+1000
            aux2i3=0


plt.plot(Yi3)
plt.title("Inicial i")
plt.show()
plt.plot(Y2i3)
plt.title("Y2 i")
plt.show()
plt.plot(Y1i3,'g')
plt.twinx()
plt.plot(Y4i3,'m')
plt.title("Y3 i")
plt.show()
plt.plot(Yji3)
plt.title("Yj i")
plt.show()
plt.plot(fm2i3)
plt.title('trasnformada de fourier i')
plt.show()
tamm13=len(Yji3)
entrenamiento[cont,0:tamm13]=Yji3[0:tamm13]
target[cont]=2
cont+=1
#----------------Vocal 14---------------------
archivo14 = 'Julian_O3.wav'
fs, Yo3 = waves.read(archivo14)

Y1o3 = np.abs(Yo3)
#Y2 = Y1[:,0]
No3 = len(Yo3)
Nf = 1000
Y2o3=np.zeros(No3)
for i in range(0,No3-Nf):
    Y2o3[i]=np.sum(Y1o3[i:i+Nf])/500
cicloso3=0
auxo3=4000
aux2o3=0

while cicloso3==0:

    Y3o3 = (Y2o3>auxo3+aux2o3)
    Xo3 = np.array(Y3o3)
    X1o3 = Xo3.astype(int)
    Y4o3 = np.abs(X1o3[0:len(X1o3)-2]-X1o3[1:len(X1o3)-1])
   
    clipo3 = np.where(Y4o3)
    clip1o3=np.array(clipo3)
    clip2o3=clip1o3[0,:]
    Yjo3=Yo3[clip2o3[len(clip2o3)-2]:clip2o3[len(clip2o3)-1]]
    Yjo3 = Yjo3[:,0]
    #auxt=np.fft.fft(Yj)
    fm1o3=np.abs(np.fft.fft(Yjo3))
    fm2o3=(fm1o3[0:int(np.floor(len(fm1o3)/2))])
    #fm2=(fm1[0:tem])
    cicloso3=np.floor(len(Yjo3)/2048)
    cicloso3=int(cicloso3)
    
    if cicloso3==0:
        if aux2o3<101:
            aux2o3=aux2o3+1
        else:
            auxo3=auxo3+1000
            aux2o3=0


plt.plot(Yo3)
plt.title("Inicial o")
plt.show()
plt.plot(Y2o3)
plt.title("Y2 o")
plt.show()
plt.plot(Y1o3,'g')
plt.twinx()
plt.plot(Y4o3,'m')
plt.title("Y3 o")
plt.show()
plt.plot(Yjo3)
plt.title("Yj")
plt.show()
plt.plot(fm2o3)
plt.title('trasnformada de fourier o')
plt.show()
tamm14=len(Yjo3)
entrenamiento[cont,0:tamm14]=Yjo3[0:tamm14]
target[cont]=3
cont+=1
#----------------Vocal 15---------------------
archivo15 = 'Julian_U3.wav'
fs, Yu3 = waves.read(archivo15)

Y1u3 = np.abs(Yu3)
#Y2 = Y1[:,0]
Nu3 = len(Yu3)
Nf = 1000
Y2u3=np.zeros(Nu3)
for i in range(0,Nu3-Nf):
    Y2u3[i]=np.sum(Y1u3[i:i+Nf])/500
ciclosu3=0
auxu3=4000
aux2u3=0

while ciclosu3==0:

    Y3u3 = (Y2u3>auxu3+aux2u3)
    Xu3 = np.array(Y3u3)
    X1u3 = Xu3.astype(int)
    Y4u3 = np.abs(X1u3[0:len(X1u3)-2]-X1u3[1:len(X1u3)-1])
   
    clipu3 = np.where(Y4u3)
    clip1u3=np.array(clipu3)
    clip2u3=clip1u3[0,:]
    Yju3 =Yu3[clip2u3[len(clip2u3)-2]:clip2u3[len(clip2u3)-1]]
    Yju3 = Yju3[:,0]
    #auxt=np.fft.fft(Yj)
    fm1u3=np.abs(np.fft.fft(Yju3))
    fm2u3=(fm1u3[0:int(np.floor(len(fm1u3)/2))])
    #fm2=(fm1[0:tem])
    ciclosu3=np.floor(len(Yju3)/2048)
    ciclosu3=int(ciclosu3)
    
    if ciclosu3==0:
        if aux2u3<101:
            aux2u3=aux2u3+1
        else:
            auxu3=auxu3+1000
            aux2u3=0


plt.plot(Yu3)
plt.title("Inicial u")
plt.show()
plt.plot(Y2u3)
plt.title("Y2 u")
plt.show()
plt.plot(Y1u3,'g')
plt.twinx()
plt.plot(Y4u3,'m')
plt.title("Y3 u")
plt.show()
plt.plot(Yju3)
plt.title("Yj u")
plt.show()
plt.plot(fm2u3)
plt.title('trasnformada de fourier u')
plt.show()
tamm15=len(Yju3)
entrenamiento[cont,0:tamm15]=Yju3[0:tamm15]
target[cont]=4
cont+=1

#----------------Vocal 16---------------------
archivo16 = 'Julian_A4.wav'
fs, Ya4 = waves.read(archivo16)

Y1a4 = np.abs(Ya4)
#Y2 = Y1[:,0]
Na4= len(Ya4)
Nf = 1000
Y2a4=np.zeros(Na4)
for i in range(0,Na4-Nf):
    Y2a4[i]=np.sum(Y1a4[i:i+Nf])/500
ciclosa4=0
auxa4=4000
aux2a4=0

while ciclosa4==0:

    Y3a4 = (Y2a4>auxa4+aux2a4)
    Xa4 = np.array(Y3a4)
    X1a4 = Xa4.astype(int)
    Y4a4 = np.abs(X1a4[0:len(X1a4)-2]-X1a4[1:len(X1a4)-1])
   
    clipa4 = np.where(Y4a4)
    clip1a4=np.array(clipa4)
    clip2a4=clip1a4[0,:]
    Yja4 =Ya4[clip2a4[len(clip2a4)-2]:clip2a4[len(clip2a4)-1]]
    Yja4 = Yja4[:,0]
    #auxt=np.fft.fft(Yj)
    fm1a4=np.abs(np.fft.fft(Yja4))
    fm2a4=(fm1a4[0:int(np.floor(len(fm1a4)/2))])
    #fm2=(fm1[0:tem])
    ciclosa4=np.floor(len(Yja4)/2048)
    ciclosa4=int(ciclosa4)
    
    if ciclosa4==0:
        if aux2a4<101:
            aux2a4=aux2a4+1
        else:
            auxa4=auxa4+1000
            aux2a4=0


plt.plot(Ya4)
plt.title("Inicial a")
plt.show()
plt.plot(Y2a4)
plt.title("Y2 a")
plt.show()
plt.plot(Y1a4,'g')
plt.twinx()
plt.plot(Y4a4,'m')
plt.title("Y3 a")
plt.show()
plt.plot(Yja4)
plt.title("Yj a")
plt.show()
plt.plot(fm2a4)
plt.title('trasnformada de fourier a')
plt.show()
#sd.play(Yj,fs)      
tamm16=len(Yja4)
entrenamiento[cont,0:tamm16]=Yja4[0:tamm16]
target[cont]=0
cont+=1 
#----------------Vocal 17---------------------
archivo17 = 'Julian_E4.wav'
fs, Ye4 = waves.read(archivo17)

Y1e4 = np.abs(Ye4)
#Y2 = Y1[:,0]
Ne4 = len(Ye4)
Nf = 1000
Y2e4=np.zeros(Ne4)
for i in range(0,Ne4-Nf):
    Y2e4[i]=np.sum(Y1e4[i:i+Nf])/500
ciclose4=0
auxe4=4000
aux2e4=0

while ciclose4==0:

    Y3e4 = (Y2e4>auxe4+aux2e4)
    Xe4 = np.array(Y3e4)
    X1e4 = Xe4.astype(int)
    Y4e4 = np.abs(X1e4[0:len(X1e4)-2]-X1e4[1:len(X1e4)-1])
   
    clipe4 = np.where(Y4e4)
    clip1e4=np.array(clipe4)
    clip2e4=clip1e4[0,:]
    Yje4 =Ye4[clip2e4[len(clip2e4)-2]:clip2e4[len(clip2e4)-1]]
    Yje4 = Yje4[:,0]
    #auxt=np.fft.fft(Yj)
    fm1e4=np.abs(np.fft.fft(Yje4))
    fm2e4=(fm1e4[0:int(np.floor(len(fm1e4)/2))])
    #fm2=(fm1[0:tem])
    ciclose4=np.floor(len(Yje4)/2048)
    ciclose4=int(ciclose4)
    
    if ciclose4==0:
        if aux2e4<101:
            aux2e4=aux2e4+1
        else:
            auxe4=auxe4+1000
            aux2e4=0


plt.plot(Ye4)
plt.title("Inicial e")
plt.show()
plt.plot(Y2e4)
plt.title("Y2 e")
plt.show()
plt.plot(Y1e4,'g')
plt.twinx()
plt.plot(Y4e4,'m')
plt.title("Y3 e")
plt.show()
plt.plot(Yje4)
plt.title("Yj")
plt.show()
plt.plot(fm2e4)
plt.title('trasnformada de fourier e')
plt.show()
tamm17=len(Yje4)
entrenamiento[cont,0:tamm17]=Yje4[0:tamm17]
target[cont]=1
cont+=1
#----------------Vocal 18---------------------
archivo18 = 'Julian_I4.wav'
fs, Yi4 = waves.read(archivo18)

Y1i4 = np.abs(Yi4)
#Y2 = Y1[:,0]
Ni4 = len(Yi4)
Nf = 1000
Y2i4=np.zeros(Ni4)
for i in range(0,Ni4-Nf):
    Y2i4[i]=np.sum(Y1i4[i:i+Nf])/500
ciclosi4=0
auxi4=1000
aux2i4=0

while ciclosi4==0:

    Y3i4 = (Y2i4>auxi4+aux2i4)
    Xi4 = np.array(Y3i4)
    X1i4 = Xi4.astype(int)
    Y4i4 = np.abs(X1i4[0:len(X1i4)-2]-X1i4[1:len(X1i4)-1])
   
    clipi4 = np.where(Y4i4)
    clip1i4=np.array(clipi4)
    clip2i4=clip1i4[0,:]
    Yji4 =Yi4[clip2i4[len(clip2i4)-2]:clip2i4[len(clip2i4)-1]]
    Yji4 = Yji4[:,0]
    #auxt=np.fft.fft(Yj)
    fm1i4=np.abs(np.fft.fft(Yji4))
    fm2i4=(fm1i4[0:int(np.floor(len(fm1i4)/2))])
    #fm2=(fm1[0:tem])
    ciclosi4=np.floor(len(Yji4)/2048)
    ciclosi4=int(ciclosi4)
    
    if ciclosi4==0:
        if aux2i4<101:
            aux2i4=aux2i4+1
        else:
            auxi4=auxi4+1000
            aux2i4=0


plt.plot(Yi4)
plt.title("Inicial i")
plt.show()
plt.plot(Y2i4)
plt.title("Y2 i")
plt.show()
plt.plot(Y1i4,'g')
plt.twinx()
plt.plot(Y4i4,'m')
plt.title("Y3 i")
plt.show()
plt.plot(Yji4)
plt.title("Yj i")
plt.show()
plt.plot(fm2i4)
plt.title('trasnformada de fourier i')
plt.show()
tamm18=len(Yji4)
entrenamiento[cont,0:tamm18]=Yji4[0:tamm18]
target[cont]=2
cont+=1
#----------------Vocal 19---------------------
archivo19 = 'Julian_O4.wav'
fs, Yo4 = waves.read(archivo19)

Y1o4 = np.abs(Yo4)
#Y2 = Y1[:,0]
No4 = len(Yo4)
Nf = 1000
Y2o4=np.zeros(No4)
for i in range(0,No4-Nf):
    Y2o4[i]=np.sum(Y1o4[i:i+Nf])/500
cicloso4=0
auxo4=4000
aux2o4=0

while cicloso4==0:

    Y3o4 = (Y2o4>auxo4+aux2o4)
    Xo4 = np.array(Y3o4)
    X1o4 = Xo4.astype(int)
    Y4o4 = np.abs(X1o4[0:len(X1o4)-2]-X1o4[1:len(X1o4)-1])
   
    clipo4 = np.where(Y4o4)
    clip1o4=np.array(clipo4)
    clip2o4=clip1o4[0,:]
    Yjo4 =Yo4[clip2o4[len(clip2o4)-2]:clip2o4[len(clip2o4)-1]]
    Yjo4 = Yjo4[:,0]
    #auxt=np.fft.fft(Yj)
    fm1o4=np.abs(np.fft.fft(Yjo4))
    fm2o4=(fm1o4[0:int(np.floor(len(fm1o4)/2))])
    #fm2=(fm1[0:tem])
    cicloso4=np.floor(len(Yjo4)/2048)
    cicloso4=int(cicloso4)
    
    if cicloso4==0:
        if aux2o4<101:
            aux2o4=aux2o4+1
        else:
            auxo4=auxo4+1000
            aux2o4=0


plt.plot(Yo4)
plt.title("Inicial o")
plt.show()
plt.plot(Y2o4)
plt.title("Y2 o")
plt.show()
plt.plot(Y1o4,'g')
plt.twinx()
plt.plot(Y4o4,'m')
plt.title("Y3 o")
plt.show()
plt.plot(Yjo4)
plt.title("Yj")
plt.show()
plt.plot(fm2o4)
plt.title('trasnformada de fourier o')
plt.show()
tamm19=len(Yjo4)
entrenamiento[cont,0:tamm19]=Yjo4[0:tamm19]
target[cont]=3
cont+=1
#----------------Vocal 20---------------------
archivo20 = 'Julian_U4.wav'
fs, Yu4 = waves.read(archivo20)

Y1u4 = np.abs(Yu4)
#Y2 = Y1[:,0]
Nu4 = len(Yu4)
Nf = 1000
Y2u4=np.zeros(Nu4)
for i in range(0,Nu4-Nf):
    Y2u4[i]=np.sum(Y1u4[i:i+Nf])/500
ciclosu4=0
auxu4=4000
aux2u4=0

while ciclosu4==0:

    Y3u4 = (Y2u4>auxu4+aux2u4)
    Xu4 = np.array(Y3u4)
    X1u4 = Xu4.astype(int)
    Y4u4 = np.abs(X1u4[0:len(X1u4)-2]-X1u4[1:len(X1u4)-1])
   
    clipu4 = np.where(Y4u4)
    clip1u4=np.array(clipu4)
    clip2u4=clip1u4[0,:]
    Yju4 =Yu4[clip2u4[len(clip2u4)-2]:clip2u4[len(clip2u4)-1]]
    Yju4 = Yju4[:,0]
    #auxt=np.fft.fft(Yj)
    fm1u4=np.abs(np.fft.fft(Yju4))
    fm2u4=(fm1u4[0:int(np.floor(len(fm1u4)/2))])
    #fm2=(fm1[0:tem])
    ciclosu4=np.floor(len(Yju4)/2048)
    ciclosu4=int(ciclosu4)
    
    if ciclosu4==0:
        if aux2u4<101:
            aux2u4=aux2u4+1
        else:
            auxu4=auxu4+1000
            aux2u4=0


plt.plot(Yu4)
plt.title("Inicial u")
plt.show()
plt.plot(Y2u4)
plt.title("Y2 u")
plt.show()
plt.plot(Y1u4,'g')
plt.twinx()
plt.plot(Y4u4,'m')
plt.title("Y3 u")
plt.show()
plt.plot(Yju4)
plt.title("Yj u")
plt.show()
plt.plot(fm2u4)
plt.title('trasnformada de fourier u')
plt.show()
tamm20=len(Yju4)
entrenamiento[cont,0:tamm20]=Yju4[0:tamm20,]
target[cont]=4
cont+=1



myFile = open('tablaP.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(entrenamiento.transpose())
    
np.savetxt('vectorP.dat', target)