
clc 
clear all
close all

[audio,Fs]=audioread('Paciente_E2.wav'); 
%audio = (audio(:, 1) + audio(:, 2)) / 2;
aux=length(audio)
x=audio;
%x=audio(1:aux/2)
N=length(x)
%load mtlb
%dt = 1/Fs; I0 = round(0.1/dt); Iend = round(0.25/dt); x = mtlb(I0:Iend);
segmentlen = 100;
noverlap = 90; 
NFFT = 128;
spectrogram(x,segmentlen,noverlap,NFFT,Fs,'yaxis'); title('Signal Spectrogram')
w=hamming(length(x))
xJ1 = x.*w;
xJa=xJ1
preemph = [1 0.63];
figure(2)
plot(x,'g')
figure(3)
hold on
plot(w,'r')
plot(xJ1,'b')
xJ1 = filter(1,preemph,xJ1);
plot(xJ1,'m')
xlabel('Tiempo(s)'); ylabel('Amplitud');
hold off
A = lpc(xJ1,16);
rts = roots(A);
rts = rts(imag(rts)>=0);
angz = atan2(imag(rts),real(rts));
[frqs,indices] = sort(angz.*(Fs/(2*pi)));
bw = -1/2*(Fs/(2*pi))*log(abs(rts(indices)));
nn = 1; 
for kk = 1:length(frqs)   
    if (frqs(kk) > 90 && bw(kk) <400)     
        formants(nn) = frqs(kk);         
        nn = nn+1;     
    end
end
formants
% figure (4)
% plot(formants(1),formants(2),'o')
%sound(audio,fs)