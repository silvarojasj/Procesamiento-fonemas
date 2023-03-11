from pydub import AudioSegment
from pydub.playback import play
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
import csv
import sounddevice as sd


#----------------Vocal 1 a1---------------------
Archivo1 = 'AudioA1.wav'
fs, Ya1 = waves.read(Archivo1)

Y1a1 = np.abs(Ya1)
#Y2 = Y1[:,0]
Na1 = len(Ya1)
Nf = 1000
Y2a1=np.zeros(Na1)

for i in range(0,Na1-Nf):
    Y2a1 [i]=np.sum(Y1a1 [i:i+Nf])/500
ciclosa1=0    
auxa1=1000
aux2a1=0

while ciclosa1==0:

    Y3a1 = (Y2a1>auxa1+aux2a1)
    Xa1 = np.array(Y3a1)
    X1a1 = Xa1.astype(int)
    Y4a1 = np.abs(X1a1 [0:len(X1a1)-2]-X1a1 [1:len(X1a1)-1])
    
    clipa1 = np.where(Y4a1)
    clip1a1=np.array(clipa1)
    clip2a1=clip1a1 [0,:]
    Yja1 =Ya1 [clip2a1 [len(clip2a1)-2]:clip2a1 [len(clip2a1)-1]]
    fm1a1=np.abs(np.fft.fft(Yja1))
    fm2a1=(fm1a1 [0:int(np.floor(len(fm1a1)/2))])
    ciclosa1=np.floor(len(Yja1)/2048)
    ciclosa1=int(ciclosa1)
    
    if ciclosa1==0:
       if aux2a1<101:
          aux2a1=aux2a1+1
       else:
           auxa1+1000
           aux2a1=0
            
plt.plot(Ya1)
plt.title("Inicial a1")
plt.show()
plt.plot(Y2a1)
plt.title("Y2 a1")
plt.show()
plt.plot(Y1a1,'g')
plt.twinx()
plt.plot(Y4a1,'m')
plt.title("Y3 a1")
plt.show()
plt.plot(Yja1)
plt.title("Yj a1")
plt.show()
plt.plot(fm2a1)
plt.title('trasnformada de fourier a1')
plt.show()
tamm1=len(Yja1)

entrenamiento=np.zeros([25,50000])
target=np.zeros(25)
cont=0

entrenamiento[cont,0:tamm1]=Yja1[0:tamm1]
target[cont]=0
cont+=1

#----------------Vocal2 e1---------------------
Archivo2 = 'AudioE1.wav'
fs, Ye1 = waves.read(Archivo2)

Y1e1 = np.abs(Ye1)
#Y2 = Y1[:,0]
Ne1 = len(Ye1)
Nf = 1000
Y2e1=np.zeros(Ne1)
for i in range(0,Ne1-Nf):
    Y2e1 [i]=np.sum(Y1e1 [i:i+Nf])/500
ciclose1=0
auxe1=1000
aux2e1=0

while ciclose1==0:
    
    Y3e1 = (Y2e1>auxe1+aux2e1)
    Xe1 = np.array(Y3e1)
    X1e1 = Xe1.astype(int)
    Y4e1 = np.abs(X1e1 [0:len(X1e1)-2]-X1e1 [1:len(X1e1)-1])
    
    clipe1 = np.where(Y4e1)
    clip1e1=np.array(clipe1)
    clip2e1=clip1e1 [0,:]
    Yje1 =Ye1 [clip2e1 [len(clip2e1)-2]:clip2e1 [len(clip2e1)-1]]
    fm1e1=np.abs(np.fft.fft(Yje1))
    fm2e1=(fm1e1 [0:int(np.floor(len(fm1e1)/2))])
    ciclose1=np.floor(len(Yje1)/2048)
    ciclose1=int(ciclose1)
    
    if ciclose1==0:
        if aux2e1<101:
           aux2e1=aux2e1+1
    else:
         auxe1=auxe1+1000
         aux2e1=0


plt.plot(Ye1)
plt.title("Inicial e1")
plt.show()
plt.plot(Y2e1)
plt.title("Y2 e1")
plt.show()
plt.plot(Y1e1,'g')
plt.twinx()
plt.plot(Y4e1,'m')
plt.title("Y3 e1")
plt.show()
plt.plot(Yje1)
plt.title("Yj e1")
plt.show()
plt.plot(fm2e1)
plt.title('trasnformada de fourier e1')
plt.show()
tamm2=len(Yje1)
entrenamiento[cont,0:tamm2]=Yje1[0:tamm2]
target[cont]=1
cont+=1

#----------------Vocal 3 i1---------------------
Archivo3 = 'AudioI6.wav'
fs, Yi1 = waves.read(Archivo3)

Y1i1 = np.abs(Yi1)
#Y2 = Y1[:,0]
Ni1 = len(Yi1)
Nf = 1000
Y2i1=np.zeros(Ni1)
for i in range(0,Ni1-Nf):
    Y2i1 [i]=np.sum(Y1i1 [i:i+Nf])/500
ciclosi1=0
auxi1=1000
aux2i1=0

while ciclosi1==0:

    Y3i1 = (Y2i1>auxi1+aux2i1)
    Xi1 = np.array(Y3i1)
    X1i1 = Xi1.astype(int)
    Y4i1 = np.abs(X1i1 [0:len(X1i1)-2]-X1i1 [1:len(X1i1)-1])
    
    clipi1 = np.where(Y4i1)
    clip1i1=np.array(clipi1)
    clip2i1=clip1i1 [0,:]
    Yji1 =Yi1 [clip2i1 [len(clip2i1)-2]:clip2i1 [len(clip2i1)-1]]
    fm1i1=np.abs(np.fft.fft(Yji1))
    fm2i1=(fm1i1 [0:int(np.floor(len(fm1i1)/2))])
    ciclosi1=np.floor(len(Yji1)/2048)
    ciclosi1=int(ciclosi1)
    
    if ciclosi1==0:
       if aux2i1<101:
          aux2i1=aux2i1+1
       else:
           auxi1=auxi1+1000
           aux2i1=0
    

plt.plot(Yi1)
plt.title("Inicial i1")
plt.show()
plt.plot(Y2i1)
plt.title("Y2 i1")
plt.show()
plt.plot(Y1i1,'g')
plt.twinx()
plt.plot(Y4i1,'m')
plt.title("Y3 i1")
plt.show()
plt.plot(Yji1)
plt.title("Yj i1")
plt.show()
plt.plot(fm2i1)
plt.title('trasnformada de fourier i1')
plt.show()
tamm3=len(Yji1)
entrenamiento[cont,0:tamm3]=Yji1[0:tamm3]
target[cont]=2
cont+=1


#----------------Vocal 4 o1---------------------
Archivo4 = 'AudioO1.wav'
fs, Yo1 = waves.read(Archivo4)

Y1o1 = np.abs(Yo1)
#Y2 = Y1[:,0]
No1 = len(Yo1)
Nf = 1000
Y2o1=np.zeros(No1)
for i in range(0,No1-Nf):
    Y2o1 [i]=np.sum(Y1o1 [i:i+Nf])/500
cicloso1=0
auxo1=1000
aux2o1=0

while cicloso1==0:

    Y3o1 = (Y2o1>auxo1+aux2o1)
    Xo1 = np.array(Y3o1)
    X1o1 = Xo1.astype(int)
    Y4o1 = np.abs(X1o1 [0:len(X1o1)-2]-X1o1 [1:len(X1o1)-1])
    clipo1 = np.where(Y4o1)
    clip1o1=np.array(clipo1)
    clip2o1=clip1o1 [0,:]
    Yjo1 =Yo1 [clip2o1 [len(clip2o1)-2]:clip2o1 [len(clip2o1)-1]]
    fm1o1=np.abs(np.fft.fft(Yjo1))
    fm2o1=(fm1o1 [0:int(np.floor(len(fm1o1)/2))])
    cicloso1=np.floor(len(Yjo1)/2048)
    cicloso1=int(cicloso1)
    
    if cicloso1==0:
        if aux2o1<101:
           aux2o1=aux2o1+1
        else:
             auxo1=auxo1+1000
             aux2o1=0


plt.plot(Yo1)
plt.title("Inicial o1")
plt.show()
plt.plot(Y2o1)
plt.title("Y2 o1")
plt.show()
plt.plot(Y1o1,'g')
plt.twinx()
plt.plot(Y4o1,'m')
plt.title("Y3 o1")
plt.show()
plt.plot(Yjo1)
plt.title("Yj o1")
plt.show()
plt.plot(fm2o1)
plt.title('trasnformada de fourier o1')
plt.show()
tamm4=len(Yjo1)
entrenamiento[cont,0:tamm4]=Yjo1[0:tamm4]
target[cont]=3
cont+=1

#----------------Vocal 5 u1---------------------
Archivo5 = 'AudioU3.wav'
fs, Yu1 = waves.read(Archivo5)

Y1u1 = np.abs(Yu1)
#Y2 = Y1[:,0]
Nu1 = len(Yu1)
Nf = 1000
Y2u1=np.zeros(Nu1)
for i in range(0,Nu1-Nf):
    Y2u1 [i]=np.sum(Y1u1 [i:i+Nf])/500
ciclosu1=0
auxu1=1000
aux2u1=0

while ciclosu1==0:

    Y3u1 = (Y2u1>auxu1+aux2u1)
    Xu1 = np.array(Y3u1)
    X1u1 = Xu1.astype(int)
    Y4u1 = np.abs(X1u1 [0:len(X1u1)-2]-X1u1 [1:len(X1u1)-1])    
    clipu1 = np.where(Y4u1)
    clip1u1=np.array(clipu1)
    clip2u1=clip1u1 [0,:]
    Yju1 =Yu1 [clip2u1 [len(clip2u1)-2]:clip2u1 [len(clip2u1)-1]]
    fm1u1=np.abs(np.fft.fft(Yju1))
    fm2u1=(fm1u1 [0:int(np.floor(len(fm1u1)/2))])
    ciclosu1=np.floor(len(Yju1)/2048)
    ciclosu1=int(ciclosu1)
    
    if ciclosu1==0:
        if aux2u1<101:
           aux2u1=aux2u1+1
    else:
         auxu1=auxu1+1000
         aux2u1=0


plt.plot(Yu1)
plt.title("Inicial u1")
plt.show()
plt.plot(Y2u1)
plt.title("Y2 u1")
plt.show()
plt.plot(Y1u1,'g')
plt.twinx()
plt.plot(Y4u1,'m')
plt.title("Y3 u1")
plt.show()
plt.plot(Yju1)
plt.title("Yj u1")
plt.show()
plt.plot(fm2u1)
plt.title('trasnformada de fourier u1')
plt.show()
tamm5=len(Yju1)
entrenamiento[cont,0:tamm5]=Yju1[0:tamm5]
target[cont]=4
cont+=1

#----------------Vocal 6 a2---------------------
Archivo6 = 'AudioA3.wav'
fs, Ya2 = waves.read(Archivo6)

Y1a2 = np.abs(Ya2)
#Y2 = Y1[:,0]
Na2 = len(Ya2)
Nf = 1000
Y2a2=np.zeros(Na2)
for i in range(0,Na2-Nf):
    Y2a2 [i]=np.sum(Y1a2 [i:i+Nf])/500
ciclosa2=0
auxa2=1000
aux2a2=0

while ciclosa2==0:

    Y3a2 = (Y2a2>auxa2+aux2a2)
    Xa2 = np.array(Y3a2)
    X1a2 = Xa2.astype(int)
    Y4a2 = np.abs(X1a2 [0:len(X1a2)-2]-X1a2 [1:len(X1a2)-1])
    
    clipa2 = np.where(Y4a2)
    clip1a2=np.array(clipa2)
    clip2a2=clip1a2 [0,:]
    Yja2 =Ya2 [clip2a2 [len(clip2a2)-2]:clip2a2 [len(clip2a2)-1]]
    fm1a2=np.abs(np.fft.fft(Yja2))
    fm2a2=(fm1a2 [0:int(np.floor(len(fm1a2)/2))])
    ciclosa2=np.floor(len(Yja2)/2048)
    ciclosa2=int(ciclosa2)

    if ciclosa2==0:
        if aux2a2<101:
           aux2a2=aux2a2+1
        else:
             auxa2=auxa2+1000
             aux2a2=0


plt.plot(Ya2)
plt.title("Inicial a2")
plt.show()
plt.plot(Y2a2)
plt.title("Y2 a2")
plt.show()
plt.plot(Y1a2,'g')
plt.twinx()
plt.plot(Y4a2,'m')
plt.title("Y3 a2")
plt.show()
plt.plot(Yja2)
plt.title("Yj a2")
plt.show()
plt.plot(fm2a2)
plt.title('trasnformada de fourier a2')
plt.show()
tamm6=len(Yja2)
entrenamiento[cont,0:tamm6]=Yja2[0:tamm6]
target[cont]=0
cont+=1


#----------------Vocal 7 e2---------------------
Archivo7 = 'AudioE3.wav'
fs, Ye2 = waves.read(Archivo7)

Y1e2 = np.abs(Ye2)
#Y2 = Y1[:,0]
Ne2 = len(Ye2)
Nf = 1000
Y2e2=np.zeros(Ne2)
for i in range(0,Ne2-Nf):
    Y2e2 [i]=np.sum(Y1e2 [i:i+Nf])/500
ciclose2=0
auxe2=1000
aux2e2=0

while ciclose2==0:

    Y3e2 = (Y2e2>auxe2+aux2e2)
    Xe2 = np.array(Y3e2)
    X1e2 = Xe2.astype(int)
    Y4e2 = np.abs(X1e2 [0:len(X1e2)-2]-X1e2 [1:len(X1e2)-1])
    
    clipe2 = np.where(Y4e2)
    clip1e2=np.array(clipe2)
    clip2e2=clip1e2 [0,:]
    Yje2 =Ye2 [clip2e2 [len(clip2e2)-2]:clip2e2 [len(clip2e2)-1]]
    fm1e2=np.abs(np.fft.fft(Yje2))
    fm2e2=(fm1e2 [0:int(np.floor(len(fm1e2)/2))])
    ciclose2=np.floor(len(Yje2)/2048)
    ciclose2=int(ciclose2)
    
    if ciclose2==0:
        if aux2e2<101:
           aux2e2=aux2e2+1
        else:
             auxe2=auxe2+1000
             aux2e2=0


plt.plot(Ye2)
plt.title("Inicial e2")
plt.show()
plt.plot(Y2e2)
plt.title("Y2 e2")
plt.show()
plt.plot(Y1e2,'g')
plt.twinx()
plt.plot(Y4e2,'m')
plt.title("Y3 e2")
plt.show()
plt.plot(Yje2)
plt.title("Yj e2")
plt.show()
plt.plot(fm2e2)
plt.title('trasnformada de fourier e2')
plt.show()
tamm7=len(Yje2)
entrenamiento[cont,0:tamm7]=Yje2[0:tamm7]
target[cont]=1
cont+=1


#----------------Vocal 8 i2---------------------
Archivo8 = 'AudioI4.wav'
fs, Yi2 = waves.read(Archivo8)

Y1i2 = np.abs(Yi2)
#Y2 = Y1[:,0]
Ni2 = len(Yi2)
Nf = 1000
Y2i2=np.zeros(Ni2)
for i in range(0,Ni2-Nf):
    Y2i2 [i]=np.sum(Y1i2 [i:i+Nf])/500
ciclosi2=0
auxi2=1000
aux2i2=0

while ciclosi2==0:
    
    Y3i2 = (Y2i2>auxi2+aux2i2)
    Xi2 = np.array(Y3i2)
    X1i2 = Xi2.astype(int)
    Y4i2 = np.abs(X1i2 [0:len(X1i2)-2]-X1i2 [1:len(X1i2)-1])
    
    clipi2 = np.where(Y4i2)
    clip1i2=np.array(clipi2)
    clip2i2=clip1i2 [0,:]
    Yji2 =Yi2 [clip2i2 [len(clip2i2)-2]:clip2i2 [len(clip2i2)-1]]
    fm1i2=np.abs(np.fft.fft(Yji2))
    fm2i2=(fm1i2 [0:int(np.floor(len(fm1i2)/2))])
    ciclosi2=np.floor(len(Yji2)/2048)
    ciclosi2=int(ciclosi2)

    if ciclosi2==0:
        if aux2i2<101:
           aux2i2=aux2i2+1
        else:
             auxi2=auxi2+1000
             aux2i2=0


plt.plot(Yi2)
plt.title("Inicial i2")
plt.show()
plt.plot(Y2i2)
plt.title("Y2 i2")
plt.show()
plt.plot(Y1i2,'g')
plt.twinx()
plt.plot(Y4i2,'m')
plt.title("Y3 i2")
plt.show()
plt.plot(Yji2)
plt.title("Yj i2")
plt.show()
plt.plot(fm2i2)
plt.title('trasnformada de fourier i2')
plt.show()
tamm8=len(Yji2)
entrenamiento[cont,0:tamm8]=Yji2[0:tamm8]
target[cont]=2
cont+=1

#----------------Vocal 9 o2---------------------
Archivo9 = 'AudioO2.wav'
fs, Yo2 = waves.read(Archivo9)

Y1o2 = np.abs(Yo2)
#Y2 = Y1[:,0]
No2 = len(Yo2)
Nf = 1000
Y2o2=np.zeros(No2)
for i in range(0,No2-Nf):
    Y2o2 [i]=np.sum(Y1o2 [i:i+Nf])/500
cicloso2=0
auxo2=1000
aux2o2=0

while cicloso2==0:

    Y3o2 = (Y2o2>auxo2+aux2o2)
    Xo2 = np.array(Y3o2)
    X1o2 = Xo2.astype(int)
    Y4o2 = np.abs(X1o2 [0:len(X1o2)-2]-X1o2 [1:len(X1o2)-1])
    
    clipo2 = np.where(Y4o2)
    clip1o2=np.array(clipo2)
    clip2o2=clip1o2 [0,:]
    Yjo2 =Yo2 [clip2o2 [len(clip2o2)-2]:clip2o2 [len(clip2o2)-1]]
    fm1o2=np.abs(np.fft.fft(Yjo2))
    fm2o2=(fm1o2 [0:int(np.floor(len(fm1o2)/2))])
    cicloso2=np.floor(len(Yjo2)/2048)
    cicloso2=int(cicloso2)
    
    if cicloso2==0:
       if aux2o2<101:
          aux2o2=aux2o2+1
       else:
            auxo2=auxo2+1000
            aux2o2=0
    

plt.plot(Yo2)
plt.title("Inicial o2")
plt.show()
plt.plot(Y2o2)
plt.title("Y2 o2")
plt.show()
plt.plot(Y1o2,'g')
plt.twinx()
plt.plot(Y4o2,'m')
plt.title("Y3 o2")
plt.show()
plt.plot(Yjo2)
plt.title("Yj o2")
plt.show()
plt.plot(fm2o2)
plt.title('trasnformada de fourier o2')
plt.show()
tamm9=len(Yjo2)
entrenamiento[cont,0:tamm9]=Yjo2[0:tamm9]
target[cont]=3
cont+=1

#----------------Vocal 10  u2---------------------
Archivo10 = 'AudioU4.wav'
fs, Yu2 = waves.read(Archivo10)

Y1u2 = np.abs(Yu2)
#Y2 = Y1[:,0]
Nu2 = len(Yu2)
Nf = 1000
Y2u2=np.zeros(Nu2)
for i in range(0,Nu2-Nf):
    Y2u2 [i]=np.sum(Y1u2 [i:i+Nf])/500
ciclosu2=0
auxu2=1000
aux2u2=0

while ciclosu2==0:

    Y3u2 = (Y2u2>auxu2+aux2u2)
    Xu2 = np.array(Y3u2)
    X1u2 = Xu2.astype(int)
    Y4u2 = np.abs(X1u2 [0:len(X1u2)-2]-X1u2 [1:len(X1u2)-1])
    
    clipu2 = np.where(Y4u2)
    clip1u2=np.array(clipu2)
    clip2u2=clip1u2 [0,:]
    Yju2 =Yu2 [clip2u2 [len(clip2u2)-2]:clip2u2 [len(clip2u2)-1]]
    fm1u2=np.abs(np.fft.fft(Yju2))
    fm2u2=(fm1u2 [0:int(np.floor(len(fm1u2)/2))])
    ciclosu2=np.floor(len(Yju2)/2048)
    ciclosu2=int(ciclosu2)
    
    if ciclosu2==0:
        if aux2u2<101:
           aux2u2=aux2u2+1
        else:
             auxu2=auxu2+1000
             aux2u2=0


plt.plot(Yu2)
plt.title("Inicial u2")
plt.show()
plt.plot(Y2u2)
plt.title("Y2 u2")
plt.show()
plt.plot(Y1u2,'g')
plt.twinx()
plt.plot(Y4u2,'m')
plt.title("Y3 u2")
plt.show()
plt.plot(Yju2)
plt.title("Yj u2")
plt.show()
plt.plot(fm2u2)
plt.title('trasnformada de fourier u2')
plt.show()
tamm10=len(Yju2)
entrenamiento[cont,0:tamm10]=Yju2[0:tamm10]
target[cont]=4
cont+=1

#----------------Vocal 11 a3---------------------
Archivo11 = 'AudioA3.wav'
fs, Ya3 = waves.read(Archivo11)

Y1a3 = np.abs(Ya3)
#Y2 = Y1[:,0]
Na3 = len(Ya3)
Nf = 1000
Y2a3=np.zeros(Na3)
for i in range(0,Na3-Nf):
    Y2a3 [i]=np.sum(Y1a3 [i:i+Nf])/500
ciclosa3=0
auxa3=1000
aux2a3=0

while ciclosa3==0:

    Y3a3 = (Y2a3>auxa3+aux2a3)
    Xa3 = np.array(Y3a3)
    X1a3 = Xa3.astype(int)
    Y4a3 = np.abs(X1a3 [0:len(X1a3)-2]-X1a3 [1:len(X1a3)-1])
    
    clipa3 = np.where(Y4a3)
    clip1a3=np.array(clipa3)
    clip2a3=clip1a3 [0,:]
    Yja3 =Ya3 [clip2a3 [len(clip2a3)-2]:clip2a3 [len(clip2a3)-1]]
    fm1a3=np.abs(np.fft.fft(Yja3))
    fm2a3=(fm1a3 [0:int(np.floor(len(fm1a3)/2))])
    ciclosa3=np.floor(len(Yja3)/2048)
    ciclosa3=int(ciclosa3)
    
    if ciclosa3==0:
        if aux2a3<101:
           aux2a3=aux2a3+1
        else:
             auxa3=auxa3+1000
             aux2a3=0


plt.plot(Ya3)
plt.title("Inicial a3")
plt.show()
plt.plot(Y2a3)
plt.title("Y2 a3")
plt.show()
plt.plot(Y1a3,'g')
plt.twinx()
plt.plot(Y4a3,'m')
plt.title("Y3 a3")
plt.show()
plt.plot(Yja3)
plt.title("Yj a3")
plt.show()
plt.plot(fm2a3)
plt.title('trasnformada de fourier a3')
plt.show()
tamm11=len(Yja3)
entrenamiento[cont,0:tamm11]=Yja3[0:tamm11]
target[cont]=0
cont+=1

#----------------Vocal 12 e3---------------------
Archivo12 = 'AudioE8.wav'
fs, Ye3 = waves.read(Archivo12)

Y1e3 = np.abs(Ye3)
#Y2 = Y1[:,0]
Ne3 = len(Ye3)
Nf = 1000
Y2e3=np.zeros(Ne3)
for i in range(0,Ne3-Nf):
    Y2e3 [i]=np.sum(Y1e3 [i:i+Nf])/500
ciclose3=0
auxe3=1000
aux2e3=0

while ciclose3==0:
    
    Y3e3 = (Y2e3>auxe3+aux2e3)
    Xe3 = np.array(Y3e3)
    X1e3 = Xe3.astype(int)
    Y4e3 = np.abs(X1e3 [0:len(X1e3)-2]-X1e3 [1:len(X1e3)-1])
    
    clipe3 = np.where(Y4e3)
    clip1e3=np.array(clipe3)
    clip2e3=clip1e3 [0,:]
    Yje3 =Ye3 [clip2e3 [len(clip2e3)-2]:clip2e3 [len(clip2e3)-1]]
    fm1e3=np.abs(np.fft.fft(Yje3))
    fm2e3=(fm1e3 [0:int(np.floor(len(fm1e3)/2))])
    ciclose3=np.floor(len(Yje3)/2048)
    ciclose3=int(ciclose3)
    
    if ciclose3==0:
        if aux2e3<101:
           aux2e3=aux2e3+1
    else:
         auxe3=auxe3+1000
         aux2e3=0


plt.plot(Ye3)
plt.title("Inicial e3")
plt.show()
plt.plot(Y2e3)
plt.title("Y2 e3")
plt.show()
plt.plot(Y1e3,'g')
plt.twinx()
plt.plot(Y4e3,'m')
plt.title("Y3 e3")
plt.show()
plt.plot(Yje3)
plt.title("Yj e3")
plt.show()
plt.plot(fm2e3)
plt.title('trasnformada de fourier e3')
plt.show()
tamm12=len(Yje3)
entrenamiento[cont,0:tamm12]=Yje3[0:tamm12]
target[cont]=1
cont+=1

#----------------Vocal 13 i3---------------------
Archivo13 = 'AudioI3.wav'
fs, Yi3 = waves.read(Archivo13)

Y1i3 = np.abs(Yi3)
#Y2 = Y1[:,0]
Ni3 = len(Yi3)
Nf = 1000
Y2i3=np.zeros(Ni3)
for i in range(0,Ni3-Nf):
    Y2i3 [i]=np.sum(Y1i3 [i:i+Nf])/500
ciclosi3=0
auxi3=1000
aux2i3=0

while ciclosi3==0:

    Y3i3 = (Y2i3>auxi3+aux2i3)
    Xi3 = np.array(Y3i3)
    X1i3 = Xi3.astype(int)
    Y4i3 = np.abs(X1i3 [0:len(X1i3)-2]-X1i3 [1:len(X1i3)-1])
    
    clipi3 = np.where(Y4i3)
    clip1i3=np.array(clipi3)
    clip2i3=clip1i3 [0,:]
    Yji3 =Yi3 [clip2i3 [len(clip2i3)-2]:clip2i3 [len(clip2i3)-1]]
    fm1i3=np.abs(np.fft.fft(Yji3))
    fm2i3=(fm1i3 [0:int(np.floor(len(fm1i3)/2))])
    ciclosi3=np.floor(len(Yji3)/2048)
    ciclosi3=int(ciclosi3)
    
    if ciclosi3==0:
       if aux2i3<101:
          aux2i3=aux2i3+1
       else:
            auxi3=auxi3+1000
            aux2i3=0


plt.plot(Yi3)
plt.title("Inicial i3")
plt.show()
plt.plot(Y2i3)
plt.title("Y2 i3")
plt.show()
plt.plot(Y1i3,'g')
plt.twinx()
plt.plot(Y4i3,'m')
plt.title("Y3 i3")
plt.show()
plt.plot(Yji3)
plt.title("Yj i3")
plt.show()
plt.plot(fm2i3)
plt.title('trasnformada de fourier i3')
plt.show()
tamm13=len(Yji3)
entrenamiento[cont,0:tamm13]=Yji3[0:tamm13]
target[cont]=2
cont+=1

#----------------Vocal 14 o3---------------------
Archivo14 = 'AudioO3.wav'
fs, Yo3 = waves.read(Archivo14)

Y1o3 = np.abs(Yo3)
#Y2 = Y1[:,0]
No3 = len(Yo3)
Nf = 1000
Y2o3=np.zeros(No3)
for i in range(0,No3-Nf):
    Y2o3 [i]=np.sum(Y1o3 [i:i+Nf])/500
cicloso3=0
auxo3=1000
aux2o3=0

while cicloso3==0:
    
    Y3o3 = (Y2o3>auxo3+aux2o3)
    Xo3 = np.array(Y3o3)
    X1o3 = Xo3.astype(int)
    Y4o3 = np.abs(X1o3 [0:len(X1o3)-2]-X1o3 [1:len(X1o3)-1])
    
    clipo3 = np.where(Y4o3)
    clip1o3=np.array(clipo3)
    clip2o3=clip1o3 [0,:]
    Yjo3 =Yo3 [clip2o3 [len(clip2o3)-2]:clip2o3 [len(clip2o3)-1]]
    fm1o3=np.abs(np.fft.fft(Yjo3))
    fm2o3=(fm1o3 [0:int(np.floor(len(fm1o3)/2))])
    cicloso3=np.floor(len(Yjo3)/2048)
    cicloso3=int(cicloso3)
    
    if cicloso3==0:
        if aux2o3<101:
           aux2o3=aux2o3+1
        else:
             auxo3=auxo3+1000
             aux2o3=0


plt.plot(Yo3)
plt.title("Inicial o3")
plt.show()
plt.plot(Y2o3)
plt.title("Y2 o3")
plt.show()
plt.plot(Y1o3,'g')
plt.twinx()
plt.plot(Y4o3,'m')
plt.title("Y3 o3")
plt.show()
plt.plot(Yjo3)
plt.title("Yj o3")
plt.show()
plt.plot(fm2o3)
plt.title('trasnformada de fourier o3')
plt.show()
tamm14=len(Yjo3)
entrenamiento[cont,0:tamm14]=Yjo3[0:tamm14]
target[cont]=3
cont+=1

#----------------Vocal 15 u3---------------------
Archivo15 = 'AudioU9.wav'
fs, Yu3 = waves.read(Archivo15)

Y1u3 = np.abs(Yu3)
#Y2 = Y1[:,0]
Nu3 = len(Yu3)
Nf = 1000
Y2u3=np.zeros(Nu3)
for i in range(0,Nu3-Nf):
    Y2u3 [i]=np.sum(Y1u3 [i:i+Nf])/500
ciclosu3=0
auxu3=1000
aux2u3=0

while ciclosu3==0:

    Y3u3 = (Y2u3>auxu3+aux2u3)
    Xu3 = np.array(Y3u3)
    X1u3 = Xu3.astype(int)
    Y4u3 = np.abs(X1u3 [0:len(X1u3)-2]-X1u3 [1:len(X1u3)-1])
    
    clipu3 = np.where(Y4u3)
    clip1u3=np.array(clipu3)
    clip2u3=clip1u3 [0,:]
    Yju3 =Yu3 [clip2u3 [len(clip2u3)-2]:clip2u3 [len(clip2u3)-1]]
    fm1u3=np.abs(np.fft.fft(Yju3))
    fm2u3=(fm1u3 [0:int(np.floor(len(fm1u3)/2))])
    ciclosu3=np.floor(len(Yju3)/2048)
    ciclosu3=int(ciclosu3)
    
    if ciclosu3==0:
        if aux2u3<101:
           aux2u3=aux2u3+1
    else:
           auxu3=auxu3+1000
           aux2u3=0


plt.plot(Yu3)
plt.title("Inicial u3")
plt.show()
plt.plot(Y2u3)
plt.title("Y2 u3")
plt.show()
plt.plot(Y1u3,'g')
plt.twinx()
plt.plot(Y4u3,'m')
plt.title("Y3 u3")
plt.show()
plt.plot(Yju3)
plt.title("Yj u3")
plt.show()
plt.plot(fm2u3)
plt.title('trasnformada de fourier u3')
plt.show()
tamm15=len(Yju3)
entrenamiento[cont,0:tamm15]=Yju3[0:tamm15]
target[cont]=4
cont+=1

#----------------Vocal 16 a4---------------------
Archivo16 = 'AudioA4.wav'
fs, Ya4 = waves.read(Archivo16)

Y1a4 = np.abs(Ya4)
#Y2 = Y1[:,0]
Na4 = len(Ya4)
Nf = 1000
Y2a4=np.zeros(Na4)
for i in range(0,Na4-Nf):
    Y2a4 [i]=np.sum(Y1a4 [i:i+Nf])/500
ciclosa4=0
auxa4=1000
aux2a4=0

while ciclosa4==0:

    Y3a4 = (Y2a4>auxa4+aux2a4)
    Xa4 = np.array(Y3a4)
    X1a4 = Xa4.astype(int)
    Y4a4 = np.abs(X1a4 [0:len(X1a4)-2]-X1a4 [1:len(X1a4)-1])
    
    clipa4 = np.where(Y4a4)
    clip1a4=np.array(clipa4)
    clip2a4=clip1a4 [0,:]
    Yja4 =Ya4 [clip2a4 [len(clip2a4)-2]:clip2a4 [len(clip2a4)-1]]
    fm1a4=np.abs(np.fft.fft(Yja4))
    fm2a4=(fm1a4 [0:int(np.floor(len(fm1a4)/2))])
    ciclosa4=np.floor(len(Yja4)/2048)
    ciclosa4=int(ciclosa4)
    
    if ciclosa4==0:
        if aux2a4<101:
           aux2a4=aux2a4+1
        else:
             auxa4=auxa4+1000
             aux2a4=0


plt.plot(Ya4)
plt.title("Inicial a4")
plt.show()
plt.plot(Y2a4)
plt.title("Y2 a4")
plt.show()
plt.plot(Y1a4,'g')
plt.twinx()
plt.plot(Y4a4,'m')
plt.title("Y3 a4")
plt.show()
plt.plot(Yja4)
plt.title("Yj a4")
plt.show()
plt.plot(fm2a4)
plt.title('trasnformada de fourier a4')
plt.show()
tamm16=len(Yja4)
entrenamiento[cont,0:tamm16]=Yja4[0:tamm16]
target[cont]=0
cont+=1

#----------------Vocal 17 e4---------------------
Archivo17 = 'AudioE4.wav'
fs, Ye4 = waves.read(Archivo17)

Y1e4 = np.abs(Ye4)
#Y2 = Y1[:,0]
Ne4 = len(Ye4)
Nf = 1000
Y2e4=np.zeros(Ne4)
for i in range(0,Ne4-Nf):
    Y2e4 [i]=np.sum(Y1e4 [i:i+Nf])/500
ciclose4=0
auxe4=1000
aux2e4=0

while ciclose4==0:

    Y3e4 = (Y2e4>auxe4+aux2e4)
    Xe4 = np.array(Y3e4)
    X1e4 = Xe4.astype(int)
    Y4e4 = np.abs(X1e4 [0:len(X1e4)-2]-X1e4 [1:len(X1e4)-1])
    clipe4 = np.where(Y4e4)
    clip1e4=np.array(clipe4)
    clip2e4=clip1e4 [0,:]
    Yje4 =Ye4 [clip2e4 [len(clip2e4)-2]:clip2e4 [len(clip2e4)-1]]
    fm1e4=np.abs(np.fft.fft(Yje4))
    fm2e4=(fm1e4 [0:int(np.floor(len(fm1e4)/2))])
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
plt.title("Inicial e4")
plt.show()
plt.plot(Y2e4)
plt.title("Y2 e4")
plt.show()
plt.plot(Y1e4,'g')
plt.twinx()
plt.plot(Y4e4,'m')
plt.title("Y3 e4")
plt.show()
plt.plot(Yje4)
plt.title("Yj e4")
plt.show()
plt.plot(fm2e4)
plt.title('trasnformada de fourier e4')
plt.show()
tamm17=len(Yje4)
entrenamiento[cont,0:tamm17]=Yje4[0:tamm17]
target[cont]=1
cont+=1

#----------------Vocal 18 i4 prueba---------------------
Archivo18 = 'AudioI4.wav'
fs, Yi4 = waves.read(Archivo18)

Y1i4 = np.abs(Yi4)
#Y2 = Y1[:,0]
Ni4 = len(Yi4)
Nf = 1000
Y2i4=np.zeros(Ni4)
for i in range(0,Ni4-Nf):
    Y2i4 [i]=np.sum(Y1i4 [i:i+Nf])/500
ciclosi4=0
auxi4=1000
aux2i4=0

while ciclosi4==0:

    Y3i4 = (Y2i4>auxi4+aux2i4)
    Xi4 = np.array(Y3i4)
    X1i4 = Xi4.astype(int)
    Y4i4 = np.abs(X1i4 [0:len(X1i4)-2]-X1i4 [1:len(X1i4)-1])
    
    clipi4 = np.where(Y4i4)
    clip1i4=np.array(clipi4)
    clip2i4=clip1i4 [0,:]
    Yji4 =Yi4 [clip2i4 [len(clip2i4)-2]:clip2i4 [len(clip2i4)-1]]
    fm1i4=np.abs(np.fft.fft(Yji4))
    fm2i4=(fm1i4 [0:int(np.floor(len(fm1i4)/2))])
    ciclosi4=np.floor(len(Yji4)/2048)
    ciclosi4=int(ciclosi4)
    
    if ciclosi4==0:
        if aux2i4<101:
           aux2i4=aux2i4+1
        else:
             auxi4=auxi4+1000
             aux2i4=0


plt.plot(Yi4)
plt.title("Inicial i4")
plt.show()
plt.plot(Y2i4)
plt.title("Y2 i4")
plt.show()
plt.plot(Y1i4,'g')
plt.twinx()
plt.plot(Y4i4,'m')
plt.title("Y3 i4")
plt.show()
plt.plot(Yji4)
plt.title("Yj i4")
plt.show()
plt.plot(fm2i4)
plt.title('trasnformada de fourier i4')
plt.show()
tamm18=len(Yji4)
entrenamiento[cont,0:tamm18]=Yji4[0:tamm18]
target[cont]=2
cont+=1

#----------------Vocal 19 o4 prueba---------------------
Archivo19 = 'AudioO4.wav'
fs, Yo4 = waves.read(Archivo19)

Y1o4 = np.abs(Yo4)
#Y2 = Y1[:,0]
No4 = len(Yo4)
Nf = 1000
Y2o4=np.zeros(No4)
for i in range(0,No4-Nf):
    Y2o4 [i]=np.sum(Y1o4 [i:i+Nf])/500
cicloso4=0
auxo4=1000
aux2o4=0

while cicloso4==0:

    Y3o4 = (Y2o4>auxo4+aux2o4)
    Xo4 = np.array(Y3o4)
    X1o4 = Xo4.astype(int)
    Y4o4 = np.abs(X1o4 [0:len(X1o4)-2]-X1o4 [1:len(X1o4)-1])
    
    clipo4 = np.where(Y4o4)
    clip1o4=np.array(clipo4)
    clip2o4=clip1o4 [0,:]
    Yjo4 =Yo4 [clip2o4 [len(clip2o4)-2]:clip2o4 [len(clip2o4)-1]]
    fm1o4=np.abs(np.fft.fft(Yjo4))
    fm2o4=(fm1o4 [0:int(np.floor(len(fm1o4)/2))])
    cicloso4=np.floor(len(Yjo4)/2048)
    cicloso4=int(cicloso4)
    
    if cicloso4==0:
        if aux2o4<101:
           aux2o4=aux2o4+1
        else:
             auxo4=auxo4+1000
             aux2o4=0


plt.plot(Yo4)
plt.title("Inicial o4")
plt.show()
plt.plot(Y2o4)
plt.title("Y2 o4")
plt.show()
plt.plot(Y1o4,'g')
plt.twinx()
plt.plot(Y4o4,'m')
plt.title("Y3 o4")
plt.show()
plt.plot(Yjo4)
plt.title("Yj o4")
plt.show()
plt.plot(fm2o4)
plt.title('trasnformada de fourier o4')
plt.show()
tamm19=len(Yjo4)
entrenamiento[cont,0:tamm19]=Yjo4[0:tamm19]
target[cont]=3
cont+=1

#----------------Vocal 20 u4 prueba---------------------
Archivo20 = 'AudioU4.wav'
fs, Yu4 = waves.read(Archivo20)

Y1u4 = np.abs(Yu4)
#Y2 = Y1[:,0]
Nu4 = len(Yu4)
Nf = 1000
Y2u4=np.zeros(Nu4)
for i in range(0,Nu4-Nf):
    Y2u4 [i]=np.sum(Y1u4 [i:i+Nf])/500
ciclosu4=0
auxu4=1000
aux2u4=0

while ciclosu4==0:

    Y3u4 = (Y2u4>auxu4+aux2u4)
    Xu4 = np.array(Y3u4)
    X1u4 = Xu4.astype(int)
    Y4u4 = np.abs(X1u4 [0:len(X1u4)-2]-X1u4 [1:len(X1u4)-1])
    
    clipu4 = np.where(Y4u4)
    clip1u4=np.array(clipu4)
    clip2u4=clip1u4 [0,:]
    Yju4 =Yu4 [clip2u4 [len(clip2u4)-2]:clip2u4 [len(clip2u4)-1]]
    fm1u4=np.abs(np.fft.fft(Yju4))
    fm2u4=(fm1u4 [0:int(np.floor(len(fm1u4)/2))])
    ciclosu4=np.floor(len(Yju4)/2048)
    ciclosu4=int(ciclosu4)
    
    if ciclosu4==0:
        if aux2u4<101:
           aux2u4=aux2u4+1
        else:
             auxu4=auxu4+1000
             aux2u4=0


plt.plot(Yu4)
plt.title("Inicial u4")
plt.show()
plt.plot(Y2u4)
plt.title("Y2 u4")
plt.show()
plt.plot(Y1u4,'g')
plt.twinx()
plt.plot(Y4u4,'m')
plt.title("Y3 u4")
plt.show()
plt.plot(Yju4)
plt.title("Yj u4")
plt.show()
plt.plot(fm2u4)
plt.title('trasnformada de fourier u4')
plt.show()
tamm20=len(Yju4)
entrenamiento[cont,0:tamm20]=Yju4[0:tamm20]
target[cont]=4
cont+=1

#----------------Vocal 21 a5---------------------
Archivo21 = 'AudioA5.wav'
fs, Ya5 = waves.read(Archivo21)

Y1a5 = np.abs(Ya5)
#Y2 = Y1[:,0]
Na5 = len(Ya5)
Nf = 1000
Y2a5=np.zeros(Na5)
for i in range(0,Na5-Nf):
    Y2a5 [i]=np.sum(Y1a5 [i:i+Nf])/500
ciclosa5=0
auxa5=1000
aux2a5=0

while ciclosa5==0:

    Y3a5 = (Y2a5>auxa5+aux2a5)
    Xa5 = np.array(Y3a5)
    X1a5 = Xa5.astype(int)
    Y4a5 = np.abs(X1a5 [0:len(X1a5)-2]-X1a5 [1:len(X1a5)-1])
    
    clipa5 = np.where(Y4a5)
    clip1a5=np.array(clipa5)
    clip2a5=clip1a5 [0,:]
    Yja5 =Ya5 [clip2a5 [len(clip2a5)-2]:clip2a5 [len(clip2a5)-1]]
    fm1a5=np.abs(np.fft.fft(Yja5))
    fm2a5=(fm1a5 [0:int(np.floor(len(fm1a5)/2))])
    ciclosa5=np.floor(len(Yja5)/2048)
    ciclosa5=int(ciclosa5)
    
    if ciclosa5==0:
        if aux2a5<101:
           aux2a5=aux2a5+1
        else:
             auxa5=auxa5+1000
             aux2a5=0


plt.plot(Ya5)
plt.title("Inicial a5")
plt.show()
plt.plot(Y2a5)
plt.title("Y2 a5")
plt.show()
plt.plot(Y1a5,'g')
plt.twinx()
plt.plot(Y4a5,'m')
plt.title("Y3 a5")
plt.show()
plt.plot(Yja5)
plt.title("Yj a5")
plt.show()
plt.plot(fm2a5)
plt.title('trasnformada de fourier a5')
plt.show()
tamm21=len(Yja5)
entrenamiento[cont,0:tamm21]=Yja5[0:tamm21]
target[cont]=0
cont+=1

#----------------Vocal 22 e5---------------------
Archivo22 = 'AudioE5.wav'
fs, Ye5 = waves.read(Archivo22)

Y1e5 = np.abs(Ye5)
#Y2 = Y1[:,0]
Ne5 = len(Ye5)
Nf = 1000
Y2e5=np.zeros(Ne5)
for i in range(0,Ne5-Nf):
    Y2e5 [i]=np.sum(Y1e5 [i:i+Nf])/500
ciclose5=0
auxe5=1000
aux2e5=0

while ciclose5==0:

    Y3e5 = (Y2e5>auxe5+aux2e5)
    Xe5 = np.array(Y3e5)
    X1e5 = Xe5.astype(int)
    Y4e5 = np.abs(X1e5 [0:len(X1e5)-2]-X1e5 [1:len(X1e5)-1])
    
    clipe5 = np.where(Y4e5)
    clip1e5=np.array(clipe5)
    clip2e5=clip1e5 [0,:]
    Yje5 =Ye5 [clip2e5 [len(clip2e5)-2]:clip2e5 [len(clip2e5)-1]]
    fm1e5=np.abs(np.fft.fft(Yje5))
    fm2e5=(fm1e5 [0:int(np.floor(len(fm1e5)/2))])
    ciclose5=np.floor(len(Yje5)/2048)
    ciclose5=int(ciclose5)

    if ciclose5==0:
        if aux2e5<101:
           aux2e5=aux2e5+1
    else:
           auxe5=auxe5+1000
           aux2e5=0


plt.plot(Ye5)
plt.title("Inicial e5")
plt.show()
plt.plot(Y2e5)
plt.title("Y2 e5")
plt.show()
plt.plot(Y1e5,'g')
plt.twinx()
plt.plot(Y4e5,'m')
plt.title("Y3 e5")
plt.show()
plt.plot(Yje5)
plt.title("Yj e5")
plt.show()
plt.plot(fm2e5)
plt.title('trasnformada de fourier e5')
plt.show()
tamm22=len(Yje5)
entrenamiento[cont,0:tamm22]=Yje5[0:tamm22]
target[cont]=1
cont+=1

#----------------Vocal 23 i5 ---------------------
Archivo23 = 'AudioI5.wav'
fs, Yi5 = waves.read(Archivo23)

Y1i5 = np.abs(Yi5)
#Y2 = Y1[:,0]
Ni5 = len(Yi5)
Nf = 1000
Y2i5=np.zeros(Ni5)
for i in range(0,Ni5-Nf):
    Y2i5 [i]=np.sum(Y1i5 [i:i+Nf])/500
ciclosi5=0
auxi5=1000
aux2i5=0

while ciclosi5==0:

    Y3i5 = (Y2i5>auxi5+aux2i5)
    Xi5 = np.array(Y3i5)
    X1i5 = Xi5.astype(int)
    Y4i5 = np.abs(X1i5 [0:len(X1i5)-2]-X1i5 [1:len(X1i5)-1])
    
    clipi5 = np.where(Y4i5)
    clip1i5=np.array(clipi5)
    clip2i5=clip1i5 [0,:]
    Yji5 =Yi5 [clip2i5 [len(clip2i5)-2]:clip2i5 [len(clip2i5)-1]]
    fm1i5=np.abs(np.fft.fft(Yji5))
    fm2i5=(fm1i5 [0:int(np.floor(len(fm1i5)/2))])
    ciclosi5=np.floor(len(Yji5)/2048)
    ciclosi5=int(ciclosi5)
    
    if ciclosi5==0:
        if aux2i5<101:
           aux2i5=aux2i5+1
        else:
             auxi5=auxi5+1000
             aux2i5=0


plt.plot(Yi5)
plt.title("Inicial i5")
plt.show()
plt.plot(Y2i5)
plt.title("Y2 i5")
plt.show()
plt.plot(Y1i5,'g')
plt.twinx()
plt.plot(Y4i5,'m')
plt.title("Y3 i5")
plt.show()
plt.plot(Yji5)
plt.title("Yj i5")
plt.show()
plt.plot(fm2i5)
plt.title('trasnformada de fourier i5')
plt.show()
tamm23=len(Yji5)
entrenamiento[cont,0:tamm23]=Yji5[0:tamm23]
target[cont]=2
cont+=1

#----------------Vocal 24 o5---------------------
Archivo24 = 'AudioO5.wav'
fs, Yo5 = waves.read(Archivo24)

Y1o5 = np.abs(Yo5)
#Y2 = Y1[:,0]
No5 = len(Yo5)
Nf = 1000
Y2o5=np.zeros(No5)
for i in range(0,No5-Nf):
    Y2o5 [i]=np.sum(Y1o5 [i:i+Nf])/500
cicloso5=0
auxo5=1000
aux2o5=0

while cicloso5==0:

    Y3o5 = (Y2o5>auxo5+aux2o5)
    Xo5 = np.array(Y3o5)
    X1o5 = Xo5.astype(int)
    Y4o5 = np.abs(X1o5 [0:len(X1o5)-2]-X1o5 [1:len(X1o5)-1])
    clipo5 = np.where(Y4o5)
    clip1o5=np.array(clipo5)
    clip2o5=clip1o5 [0,:]
    Yjo5 =Yo5 [clip2o5 [len(clip2o5)-2]:clip2o5 [len(clip2o5)-1]]
    fm1o5=np.abs(np.fft.fft(Yjo5))
    fm2o5=(fm1o5 [0:int(np.floor(len(fm1o5)/2))])
    cicloso5=np.floor(len(Yjo5)/2048)
    cicloso5=int(cicloso5)
    
    if cicloso5==0:
        if aux2o5<101:
           aux2o5=aux2o5+1
        else:
             auxo5=auxo5+1000
             aux2o5=0


plt.plot(Yo5)
plt.title("Inicial o5")
plt.show()
plt.plot(Y2o5)
plt.title("Y2 o5")
plt.show()
plt.plot(Y1o5,'g')
plt.twinx()
plt.plot(Y4o5,'m')
plt.title("Y3 o5")
plt.show()
plt.plot(Yjo5)
plt.title("Yj o5")
plt.show()
plt.plot(fm2o5)
plt.title('trasnformada de fourier o5')
plt.show()
tamm24=len(Yjo5)
entrenamiento[cont,0:tamm24]=Yjo5[0:tamm24]
target[cont]=3
cont+=1

#----------------Vocal 25 u5---------------------
Archivo25 = 'AudioU5.wav'
fs, Yu5 = waves.read(Archivo25)

Y1u5 = np.abs(Yu5)
#Y2 = Y1[:,0]
Nu5 = len(Yu5)
Nf = 1000
Y2u5=np.zeros(Nu5)
for i in range(0,Nu5-Nf):
    Y2u5 [i]=np.sum(Y1u5 [i:i+Nf])/500
ciclosu5=0
auxu5=1000
aux2u5=0

while ciclosu5==0:
    
    Y3u5 = (Y2u5>auxu5+aux2u5)
    Xu5 = np.array(Y3u5)
    X1u5 = Xu5.astype(int)
    Y4u5 = np.abs(X1u5 [0:len(X1u5)-2]-X1u5 [1:len(X1u5)-1])
    
    clipu5 = np.where(Y4u5)
    clip1u5=np.array(clipu5)
    clip2u5=clip1u5 [0,:]
    Yju5 =Yu5 [clip2u5 [len(clip2u5)-2]:clip2u5 [len(clip2u5)-1]]
    fm1u5=np.abs(np.fft.fft(Yju5))
    fm2u5=(fm1u5 [0:int(np.floor(len(fm1u5)/2))])
    ciclosu5=np.floor(len(Yju5)/2048)
    ciclosu5=int(ciclosu5)
    
    if ciclosu5==0:
        if aux2u5<101:
           aux2u5=aux2u5+1
        else:
             auxu5=auxu5+1000
             aux2u5=0


plt.plot(Yu5)
plt.title("Inicial u5")
plt.show()
plt.plot(Y2u5)
plt.title("Y2 u5")
plt.show()
plt.plot(Y1u5,'g')
plt.twinx()
plt.plot(Y4u5,'m')
plt.title("Y3 u5")
plt.show()
plt.plot(Yju5)
plt.title("Yj u5")
plt.show()
plt.plot(fm2u5)
plt.title('trasnformada de fourier u5')
plt.show()
tamm25=len(Yju5)
entrenamiento[cont,0:tamm25]=Yju5[0:tamm25]
target[cont]=4
cont+=1

#----------------Vocal 26 a6---------------------
Archivo26 = 'AudioA6.wav'
fs, Ya6 = waves.read(Archivo26)

Y1a6 = np.abs(Ya6)
#Y2 = Y1[:,0]
Na6 = len(Ya6)
Nf = 1000
Y2a6=np.zeros(Na6)
for i in range(0,Na6-Nf):
    Y2a6 [i]=np.sum(Y1a6 [i:i+Nf])/500
ciclosa6=0
auxa6=1000
aux2a6=0

while ciclosa6==0:

    Y3a6 = (Y2a6>auxa6+aux2a6)
    Xa6 = np.array(Y3a6)
    X1a6 = Xa6.astype(int)
    Y4a6 = np.abs(X1a6 [0:len(X1a6)-2]-X1a6 [1:len(X1a6)-1])
    
    clipa6 = np.where(Y4a6)
    clip1a6=np.array(clipa6)
    clip2a6=clip1a6 [0,:]
    Yja6 =Ya6 [clip2a6 [len(clip2a6)-2]:clip2a6 [len(clip2a6)-1]]
    fm1a6=np.abs(np.fft.fft(Yja6))
    fm2a6=(fm1a6 [0:int(np.floor(len(fm1a6)/2))])
    ciclosa6=np.floor(len(Yja6)/2048)
    ciclosa6=int(ciclosa6)
    
    if ciclosa6==0:
        if aux2a6<101:
           aux2a6=aux2a6+1
        else:
             auxa6=auxa6+1000
             aux2a6=0


plt.plot(Ya6)
plt.title("Inicial a6")
plt.show()
plt.plot(Y2a6)
plt.title("Y2 a6")
plt.show()
plt.plot(Y1a6,'g')
plt.twinx()
plt.plot(Y4a6,'m')
plt.title("Y3 a6")
plt.show()
plt.plot(Yja6)
plt.title("Yj a6")
plt.show()
plt.plot(fm2a6)
plt.title('trasnformada de fourier a6')
plt.show()
tamm26=len(Yja6)
entrenamiento[cont,0:tamm26]=Yja6[0:tamm26]
target[cont]=0
cont+=1

#----------------Vocal 27 e6---------------------
Archivo27 = 'AudioE6.wav'
fs, Ye6 = waves.read(Archivo27)

Y1e6 = np.abs(Ye6)
#Y2 = Y1[:,0]
Ne6 = len(Ye6)
Nf = 1000
Y2e6=np.zeros(Ne6)
for i in range(0,Ne6-Nf):
    Y2e6 [i]=np.sum(Y1e6 [i:i+Nf])/500
ciclose6=0
auxe6=1000
aux2e6=0

while ciclose6==0:

    Y3e6 = (Y2e6>auxe6+aux2e6)
    Xe6 = np.array(Y3e6)
    X1e6 = Xe6.astype(int)
    Y4e6 = np.abs(X1e6 [0:len(X1e6)-2]-X1e6 [1:len(X1e6)-1])
    clipe6 = np.where(Y4e6)
    clip1e6=np.array(clipe6)
    clip2e6=clip1e6 [0,:]
    Yje6 =Ye6 [clip2e6 [len(clip2e6)-2]:clip2e6 [len(clip2e6)-1]]
    fm1e6=np.abs(np.fft.fft(Yje6))
    fm2e6=(fm1e6 [0:int(np.floor(len(fm1e6)/2))])
    ciclose6=np.floor(len(Yje6)/2048)
    ciclose6=int(ciclose6)
    
    if ciclose6==0:
        if aux2e6<101:
           aux2e6=aux2e6+1
        else:
             auxe6=auxe6+1000
             aux2e6=0


plt.plot(Ye6)
plt.title("Inicial e6")
plt.show()
plt.plot(Y2e6)
plt.title("Y2 e6")
plt.show()
plt.plot(Y1e6,'g')
plt.twinx()
plt.plot(Y4e6,'m')
plt.title("Y3 e6")
plt.show()
plt.plot(Yje6)
plt.title("Yj e6")
plt.show()
plt.plot(fm2e6)
plt.title('trasnformada de fourier e6')
plt.show()
tamm27=len(Yje6)
entrenamiento[cont,0:tamm27]=Yje6[0:tamm27]
target[cont]=1
cont+=1

#----------------Vocal 28 i6---------------------
Archivo28 = 'AudioI6.wav'
fs, Yi6 = waves.read(Archivo28)

Y1i6 = np.abs(Yi6)
#Y2 = Y1[:,0]
Ni6 = len(Yi6)
Nf = 1000
Y2i6=np.zeros(Ni6)
for i in range(0,Ni6-Nf):
    Y2i6 [i]=np.sum(Y1i6 [i:i+Nf])/500
ciclosi6=0
auxi6=1000
aux2i6=0

while ciclosi6==0:
    
    Y3i6 = (Y2i6>auxi6+aux2i6)
    Xi6 = np.array(Y3i6)
    X1i6 = Xi6.astype(int)
    Y4i6 = np.abs(X1i6 [0:len(X1i6)-2]-X1i6 [1:len(X1i6)-1])
    clipi6 = np.where(Y4i6)
    clip1i6=np.array(clipi6)
    clip2i6=clip1i6 [0,:]
    Yji6 =Yi6 [clip2i6 [len(clip2i6)-2]:clip2i6 [len(clip2i6)-1]]
    fm1i6=np.abs(np.fft.fft(Yji6))
    fm2i6=(fm1i6 [0:int(np.floor(len(fm1i6)/2))])
    ciclosi6=np.floor(len(Yji6)/2048)
    ciclosi6=int(ciclosi6)
    
    if ciclosi6==0:
       if aux2i6<101:
          aux2i6=aux2i6+1
       else:
            auxi6=auxi6+1000
            aux2i6=0


plt.plot(Yi6)
plt.title("Inicial i6")
plt.show()
plt.plot(Y2i6)
plt.title("Y2 i6")
plt.show()
plt.plot(Y1i6,'g')
plt.twinx()
plt.plot(Y4i6,'m')
plt.title("Y3 i6")
plt.show()
plt.plot(Yji6)
plt.title("Yj i6")
plt.show()
plt.plot(fm2i6)
plt.title('trasnformada de fourier i6')
plt.show()
tamm28=len(Yji6)
entrenamiento[cont,0:tamm28]=Yji6[0:tamm28]
target[cont]=2
cont+=1

#----------------Vocal 29 o6---------------------
Archivo29 = 'AudioO6.wav'
fs, Yo6 = waves.read(Archivo29)

Y1o6 = np.abs(Yo6)
#Y2 = Y1[:,0]
No6 = len(Yo6)
Nf = 1000
Y2o6=np.zeros(No6)
for i in range(0,No6-Nf):
    Y2o6 [i]=np.sum(Y1o6 [i:i+Nf])/500
cicloso6=0
auxo6=1000
aux2o6=0

while cicloso6==0:

    Y3o6 = (Y2o6>auxo6+aux2o6)
    Xo6 = np.array(Y3o6)
    X1o6 = Xo6.astype(int)
    Y4o6 = np.abs(X1o6 [0:len(X1o6)-2]-X1o6 [1:len(X1o6)-1])
    clipo6 = np.where(Y4o6)
    clip1o6=np.array(clipo6)
    clip2o6=clip1o6 [0,:]
    Yjo6 =Yo6 [clip2o6 [len(clip2o6)-2]:clip2o6 [len(clip2o6)-1]]
    fm1o6=np.abs(np.fft.fft(Yjo6))
    fm2o6=(fm1o6 [0:int(np.floor(len(fm1o6)/2))])
    cicloso6=np.floor(len(Yjo6)/2048)
    cicloso6=int(cicloso6)

    if cicloso6==0:
        if aux2o6<101:
           aux2o6=aux2o6+1
        else:
             auxo6=auxo6+1000
             aux2o6=0


plt.plot(Yo6)
plt.title("Inicial o6")
plt.show()
plt.plot(Y2o6)
plt.title("Y2 o6")
plt.show()
plt.plot(Y1o6,'g')
plt.twinx()
plt.plot(Y4o6,'m')
plt.title("Y3 o6")
plt.show()
plt.plot(Yjo6)
plt.title("Yj o6")
plt.show()
plt.plot(fm2o6)
plt.title('trasnformada de fourier o6')
plt.show()
tamm29=len(Yjo6)
entrenamiento[cont,0:tamm29]=Yjo6[0:tamm29]
target[cont]=3
cont+=1

#----------------Vocal 30 u6---------------------
Archivo30 = 'AudioU6.wav'
fs, Yu6 = waves.read(Archivo30)

Y1u6 = np.abs(Yu6)
#Y2 = Y1[:,0]
Nu6 = len(Yu6)
Nf = 1000
Y2u6=np.zeros(Nu6)
for i in range(0,Nu6-Nf):
    Y2u6 [i]=np.sum(Y1u6 [i:i+Nf])/500
ciclosu6=0
auxu6=1000
aux2u6=0

while ciclosu6==0:

    Y3u6 = (Y2u6>auxu6+aux2u6)
    Xu6 = np.array(Y3u6)
    X1u6 = Xu6.astype(int)
    Y4u6 = np.abs(X1u6 [0:len(X1u6)-2]-X1u6 [1:len(X1u6)-1])
    
    clipu6 = np.where(Y4u6)
    clip1u6=np.array(clipu6)
    clip2u6=clip1u6 [0,:]
    Yju6 =Yu6 [clip2u6 [len(clip2u6)-2]:clip2u6 [len(clip2u6)-1]]
    fm1u6=np.abs(np.fft.fft(Yju6))
    fm2u6=(fm1u6 [0:int(np.floor(len(fm1u6)/2))])
    ciclosu6=np.floor(len(Yju6)/2048)
    ciclosu6=int(ciclosu6)
    
    if ciclosu6==0:
        if aux2u6<101:
           aux2u6=aux2u6+1
        else:
            auxu6=auxu6+1000
            aux2u6=0


plt.plot(Yu6)
plt.title("Inicial u6")
plt.show()
plt.plot(Y2u6)
plt.title("Y2 u6")
plt.show()
plt.plot(Y1u6,'g')
plt.twinx()
plt.plot(Y4u6,'m')
plt.title("Y3 u6")
plt.show()
plt.plot(Yju6)
plt.title("Yj u6")
plt.show()
plt.plot(fm2u6)
plt.title('trasnformada de fourier u6')
plt.show()
tamm30=len(Yju6)
entrenamiento[cont,0:tamm30]=Yju6[0:tamm30]
target[cont]=4
cont+=1

#----------------Vocal 31 a7---------------------
Archivo31 = 'AudioA7.wav'
fs, Ya7 = waves.read(Archivo31)

Y1a7 = np.abs(Ya7)
#Y2 = Y1[:,0]
Na7 = len(Ya7)
Nf = 1000
Y2a7=np.zeros(Na7)
for i in range(0,Na7-Nf):
    Y2a7 [i]=np.sum(Y1a7 [i:i+Nf])/500
ciclosa7=0
auxa7=1000
aux2a7=0

while ciclosa7==0:
    
    Y3a7 = (Y2a7>auxa7+aux2a7)
    Xa7 = np.array(Y3a7)
    X1a7 = Xa7.astype(int)
    Y4a7 = np.abs(X1a7 [0:len(X1a7)-2]-X1a7 [1:len(X1a7)-1])
    clipa7 = np.where(Y4a7)
    clip1a7=np.array(clipa7)
    clip2a7=clip1a7 [0,:]
    Yja7 =Ya7 [clip2a7 [len(clip2a7)-2]:clip2a7 [len(clip2a7)-1]]
    fm1a7=np.abs(np.fft.fft(Yja7))
    fm2a7=(fm1a7 [0:int(np.floor(len(fm1a7)/2))])
    ciclosa7=np.floor(len(Yja7)/2048)
    ciclosa7=int(ciclosa7)
    
    if ciclosa7==0:
        if aux2a7<101:
           aux2a7=aux2a7+1
        else:
             auxa7=auxa7+1000
             aux2a7=0

plt.plot(Ya7)
plt.title("Inicial a7")
plt.show()
plt.plot(Y2a7)
plt.title("Y2 a7")
plt.show()
plt.plot(Y1a7,'g')
plt.twinx()
plt.plot(Y4a7,'m')
plt.title("Y3 a7")
plt.show()
plt.plot(Yja7)
plt.title("Yj a7")
plt.show()
plt.plot(fm2a7)
plt.title('trasnformada de fourier a7')
plt.show()
tamm31=len(Yja7)
entrenamiento[cont,0:tamm31]=Yja7[0:tamm31]
target[cont]=0
cont+=1

#----------------Vocal 32 e7---------------------
Archivo32 = 'AudioE7.wav'
fs, Ye7 = waves.read(Archivo32)

Y1e7 = np.abs(Ye7)
#Y2 = Y1[:,0]
Ne7 = len(Ye7)
Nf = 1000
Y2e7=np.zeros(Ne7)
for i in range(0,Ne7-Nf):
    Y2e7 [i]=np.sum(Y1e7 [i:i+Nf])/500
ciclose7=0
auxe7=1000
aux2e7=0

while ciclose7==0:

    Y3e7 = (Y2e7>auxe7+aux2e7)
    Xe7 = np.array(Y3e7)
    X1e7 = Xe7.astype(int)
    Y4e7 = np.abs(X1e7 [0:len(X1e7)-2]-X1e7 [1:len(X1e7)-1])
    clipe7 = np.where(Y4e7)
    clip1e7=np.array(clipe7)
    clip2e7=clip1e7 [0,:]
    Yje7 =Ye7 [clip2e7 [len(clip2e7)-2]:clip2e7 [len(clip2e7)-1]]
    fm1e7=np.abs(np.fft.fft(Yje7))
    fm2e7=(fm1e7 [0:int(np.floor(len(fm1e7)/2))])
    ciclose7=np.floor(len(Yje7)/2048)
    ciclose7=int(ciclose7)
    
    if ciclose7==0:
        if aux2e7<101:
           aux2e7=aux2e7+1
        else:
             auxe7=auxe7+1000
             aux2e7=0
                
                
plt.plot(Ye7)
plt.title("Inicial e7")
plt.show()
plt.plot(Y2e7)
plt.title("Y2 e7")
plt.show()
plt.plot(Y1e7,'g')
plt.twinx()
plt.plot(Y4e7,'m')
plt.title("Y3 e7")
plt.show()
plt.plot(Yje7)
plt.title("Yj e7")
plt.show()
plt.plot(fm2e7)
plt.title('trasnformada de fourier e7')
plt.show()
tamm32=len(Yje7)
entrenamiento[cont,0:tamm32]=Yje7[0:tamm32]
target[cont]=1
cont+=1

#----------------Vocal 33 i7 ---------------------
Archivo33 = 'AudioI7.wav'
fs, Yi7 = waves.read(Archivo33)

Y1i7 = np.abs(Yi7)
#Y2 = Y1[:,0]
Ni7 = len(Yi7)
Nf = 1000
Y2i7=np.zeros(Ni7)
for i in range(0,Ni7-Nf):
    Y2i7 [i]=np.sum(Y1i7 [i:i+Nf])/500
ciclosi7=0
auxi7=1000
aux2i7=0

while ciclosi7==0:

    Y3i7 = (Y2i7>auxi7+aux2i7)
    Xi7 = np.array(Y3i7)
    X1i7 = Xi7.astype(int)
    Y4i7 = np.abs(X1i7 [0:len(X1i7)-2]-X1i7 [1:len(X1i7)-1])

    clipi7 = np.where(Y4i7)
    clip1i7=np.array(clipi7)
    clip2i7=clip1i7 [0,:]
    Yji7 =Yi7 [clip2i7 [len(clip2i7)-2]:clip2i7 [len(clip2i7)-1]]
    fm1i7=np.abs(np.fft.fft(Yji7))
    fm2i7=(fm1i7 [0:int(np.floor(len(fm1i7)/2))])
    ciclosi7=np.floor(len(Yji7)/2048)
    ciclosi7=int(ciclosi7)

    if ciclosi7==0:
        if aux2i7<101:
            aux2i7=aux2i7+1
        else:
            auxi7=auxi7+1000
            aux2i7=0


plt.plot(Yi7)
plt.title("Inicial i7")
plt.show()
plt.plot(Y2i7)
plt.title("Y2 i7")
plt.show()
plt.plot(Y1i7,'g')
plt.twinx()
plt.plot(Y4i7,'m')
plt.title("Y3 i7")
plt.show()
plt.plot(Yji7)
plt.title("Yj i7")
plt.show()
plt.plot(fm2i7)
plt.title('trasnformada de fourier i7')
plt.show()
tamm33=len(Yji7)
entrenamiento[cont,0:tamm33]=Yji7[0:tamm33]
target[cont]=2
cont+=1

#----------------Vocal 34 o7---------------------
Archivo34 = 'AudioO7.wav'
fs, Yo7 = waves.read(Archivo34)

Y1o7 = np.abs(Yo7)
#Y2 = Y1[:,0]
No7 = len(Yo7)
Nf = 1000
Y2o7=np.zeros(No7)
for i in range(0,No7-Nf):
    Y2o7 [i]=np.sum(Y1o7 [i:i+Nf])/500
cicloso7=0
auxo7=1000
aux2o7=0

while cicloso7==0:

    Y3o7 = (Y2o7>auxo7+aux2o7)
    Xo7 = np.array(Y3o7)
    X1o7 = Xo7.astype(int)
    Y4o7 = np.abs(X1o7 [0:len(X1o7)-2]-X1o7 [1:len(X1o7)-1])

    clipo7 = np.where(Y4o7)
    clip1o7=np.array(clipo7)
    clip2o7=clip1o7 [0,:]
    Yjo7 =Yo7 [clip2o7 [len(clip2o7)-2]:clip2o7 [len(clip2o7)-1]]
    fm1o7=np.abs(np.fft.fft(Yjo7))
    fm2o7=(fm1o7 [0:int(np.floor(len(fm1o7)/2))])
    cicloso7=np.floor(len(Yjo7)/2048)
    cicloso7=int(cicloso7)

    if cicloso7==0:
        if aux2o7<101:
           aux2o7=aux2o7+1
        else:
             auxo7=auxo7+1000
             aux2o7=0


plt.plot(Yo7)
plt.title("Inicial o7")
plt.show()
plt.plot(Y2o7)
plt.title("Y2 o7")
plt.show()
plt.plot(Y1o7,'g')
plt.twinx()
plt.plot(Y4o7,'m')
plt.title("Y3 o7")
plt.show()
plt.plot(Yjo7)
plt.title("Yj o7")
plt.show()
plt.plot(fm2o7)
plt.title('trasnformada de fourier o7')
plt.show()
tamm34=len(Yjo7)
entrenamiento[cont,0:tamm34]=Yjo7[0:tamm34]
target[cont]=3
cont+=1

#----------------Vocal 35 u7 ---------------------
Archivo35 = 'AudioU7.wav'
fs, Yu7 = waves.read(Archivo35)

Y1u7 = np.abs(Yu7)
#Y2 = Y1[:,0]
Nu7 = len(Yu7)
Nf = 1000
Y2u7=np.zeros(Nu7)
for i in range(0,Nu7-Nf):
    Y2u7 [i]=np.sum(Y1u7 [i:i+Nf])/500
ciclosu7=0
auxu7=1000
aux2u7=0

while ciclosu7==0:
    
    Y3u7 = (Y2u7>auxu7+aux2u7)
    Xu7 = np.array(Y3u7)
    X1u7 = Xu7.astype(int)
    Y4u7 = np.abs(X1u7 [0:len(X1u7)-2]-X1u7 [1:len(X1u7)-1])
    
    clipu7 = np.where(Y4u7)
    clip1u7=np.array(clipu7)
    clip2u7=clip1u7 [0,:]
    Yju7 =Yu7 [clip2u7 [len(clip2u7)-2]:clip2u7 [len(clip2u7)-1]]
    Yju7 = Yju7 [:,0]
    #auxt=np.fft.fft(Yj)
    fm1u7=np.abs(np.fft.fft(Yju7))
    fm2u7=(fm1u7 [0:int(np.floor(len(fm1u7)/2))])
    #fm2=(fm1[0:tem])
    ciclosu7=np.floor(len(Yju7)/2048)
    ciclosu7=int(ciclosu7)
    
    if ciclosu7==0:
        if aux2u7<101:
           aux2u7=aux2u7+1
        else:
             auxu7=auxu7+1000
             aux2u7=0


plt.plot(Yu7)
plt.title("Inicial u7")
plt.show()
plt.plot(Y2u7)
plt.title("Y2 u7")
plt.show()
plt.plot(Y1u7,'g')
plt.twinx()
plt.plot(Y4u7,'m')
plt.title("Y3 u7")
plt.show()
plt.plot(Yju7)
plt.title("Yj u7")
plt.show()
plt.plot(fm2u7)
plt.title('trasnformada de fourier u7')
plt.show()
tamm35=len(Yju7)
entrenamiento[cont,0:tamm35]=Yju7[0:tamm35]
target[cont]=4
cont+=1


myFile = open('BDD.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(entrenamiento.transpose())
    
np.savetxt('BDD.dat', target)
