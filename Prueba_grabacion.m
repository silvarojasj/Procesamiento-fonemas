clc 
clear all
close all

%[audio,Fs]=audioread('Julian_I3.wav'); 
%x = (audio(:, 1) + audio(:, 2)) / 2;
vocales=[789.8,870.4,399.2,2276.8,242.6,2831.2,539.8,5956.4,325.8,5992.2]
Fs=44100;
fprintf("por favor diga una vocal\n")
Grab=audiorecorder(Fs,16,1);
fprintf("grabando...\n")
record (Grab);
pause(3);
stop(Grab);
fprintf("La vocal ha sido grabada\n")
x=getaudiodata(Grab,'double');
N=length(x);

segmentlen = 100;
noverlap = 90; 
NFFT = 128;
spectrogram(x,segmentlen,noverlap,NFFT,Fs,'yaxis'); title('Signal Spectrogram')
w=hamming(length(x))
xJ1 = x.*w;
preemph = [1 0.63];
figure(2)
plot(x,'g')
hold on
plot(w,'r')
plot(xJ1,'b')
xJ1 = filter(1,preemph,xJ1);
plot(xJ1,'m')
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
 figure (3)
hold on
scatter(vocales(1),vocales(2),'o','filled')
scatter(vocales(3),vocales(4),'o','filled')
scatter(vocales(5),vocales(6),'o','filled')
scatter(vocales(7),vocales(8),'o','filled')
scatter(vocales(9),vocales(10),'o','filled')
scatter(formants(1),formants(2),'o','filled')
legend('a','e','i','o','u','vocal')
xlabel('Formante 1'); ylabel('Formante 2');
grid on
hold off
%ResA(1)= formants(1)-vocales(1)
%ResA(2)= formants(2)-vocales(2)
ResA= abs(sqrt((formants(1)-vocales(1))^2+(formants(2)-vocales(2))^2));
ResE= abs(sqrt((formants(1)-vocales(3))^2+(formants(2)-vocales(4))^2));
ResI= abs(sqrt((formants(1)-vocales(5))^2+(formants(2)-vocales(6))^2));
ResO= abs(sqrt((formants(1)-vocales(7))^2+(formants(2)-vocales(8))^2));
ResU= abs(sqrt((formants(1)-vocales(9))^2+(formants(2)-vocales(10))^2));
if ((ResA<ResE)&&(ResA<ResI)&&(ResA<ResO)&&(ResA<ResU))
    fprintf('la vocal es A')
elseif ((ResE<ResI)&&(ResE<ResO)&&(ResE<ResU))
    fprintf('la vocal es E')
elseif ((ResI<ResO)&&(ResI<ResU))
    fprintf('la vocal es I')
elseif(ResO<ResU)
    fprintf('la vocal es O')
else
    fprintf('la vocal es U')
end

%sound(audio,fs)