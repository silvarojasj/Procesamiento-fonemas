clc 
clear all
close all
[y,fs]=audioread('AudioA1.wav'); 
ya=y(1:76680)
y1=abs(ya);
y2=y1;
N=length(y1)
Nf=1000;
for i=1:N-Nf
    y2(i)=sum(y1(i:i+Nf-1))/500;
end
ciclos=0
aux=0.01
while(ciclos==0)
    
    y3=(y2>aux);

    y4=abs(y3(1:length(y3)-1)-y3(2:length(y3)));
    %sound(y,fs);
    figure(1)
    plot(y2)    
    figure(2)
    plot(y1,'g')
    
    clip=find(y4)
    yJ=y1(clip(length(clip)-1):clip(length(clip)))
    %plot(y2,'r')
    hold on
    plot(y3*0.5,'b')     
    plot(y4*0.5,'m')
    hold off
%     dt = 1/fs;
%     t = 0:dt:(length(yJ)*dt)-dt;
%     plot(t,yJ)
  
    figure(3)  
    plot(yJ)
    title('Recorte  de señal de persona sana ')
    xlabel('Tiempo s'); ylabel('Ganancia dB');
    fm1=abs(fft(yJ));
    fm2=(fm1(1:floor(length(fm1)/2)))

    figure(4)  
    plot((1:length(fm2))*((0.5*fs)/length(fm2))./1000,fm2);
    xlim([0 10])
    title('Transforamada de fourier a señal de persona sana')
    xlabel('Frecuencia kHz'); ylabel('|Y(F)|');

    ciclos=floor(length(yJ)/2048)
    if(ciclos==0)
        aux=aux+0.01
    end
end
    for i=1:ciclos
    ff=abs(fft(yJ((i-1)*2048+1:i*2048)));

    Ft(i,:)=ff(1:100)
    end

%sound(yJ,fs)
figure(5)
surf(Ft)