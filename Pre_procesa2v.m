clc 
clear all
close all
fs=44100;
fprintf("por favor diga una vocal\n")
Grab=audiorecorder(fs,16,1);
fprintf("grabando...\n")
record (Grab);
pause(3);
stop(Grab);
fprintf("La vocal ha sido grabada\n")
x=getaudiodata(Grab,'double');
y=x
%[y,fs]=audioread('AudioA1.wav'); 
y1=abs(y);
y2=y1;
N=length(y)
Nf=1000;
for i=1:N-Nf
    y2(i)=sum(y1(i:i+Nf-1))/500;
end
ciclos=0
aux=0.02
    while(ciclos==0)

        y3=(y2>aux);

        y4=abs(y3(1:length(y3)-1)-y3(2:length(y3)));
        figure(1)
        plot(y2) 
        title('Valor absoluto de señal de audio de entrada')
        xlabel('Tiempo s'); ylabel('Ganancia dB');
        
        
        figure(6)   
        plot(y,'b')
        title('Señal de audio de entrada')
        xlabel('Tiempo s'); ylabel('Ganancia dB');
        
        figure( 2)   
        plot(y,'g')
        title('Señal de audio de entrada')
        xlabel('Tiempo s'); ylabel('Ganancia dB');
        hold on
        clip=find(y4)

        yJ=y(clip(length(clip)-1):clip(length(clip)))
 
        plot(y4*0.5,'m')
        hold off

        figure(3)  
        plot(yJ)
        title('Recorte de señal del paciente')
        xlabel('Tiempo s'); ylabel('Ganancia dB');
        fm1=abs(fft(yJ));
        fm2=(fm1(1:floor(length(fm1)/2)))

        figure(4)  
        plot((1:length(fm2))*((0.5*fs)/length(fm2))./1000,fm2);
        xlim([0 10])
        title('Transformada de fourier de señal del paciente')
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
res=zeros(5000,1);
for i=1:length (yJ)
    res(i)=yJ(i);
end

%%sound(yJ,fs)
 figure(5)
%  filename='Grafica de voz 3d.gif';
%  set(gcf,'Renderer','zbuffer')
%  Rr=Ft
 surf(Ft)
 [caz,cel] = view
 v = [-5 -2 5];
 [caz,cel] = view(v)
%  t = -15*pi/180;
% %  tform= affine3d
% %  Ft=imwarp(Ft,tform);
% %  im=frame2im(frame)
%  [imind,cm]=rgb2ind(im,256);
%  imwrite(imind,cm,filename,'gif','LoopCount',inf)
%  imwrite(imind,cm,filename,'gif','WriteMode','append')
%  
% % save Prueba_Sp.mat