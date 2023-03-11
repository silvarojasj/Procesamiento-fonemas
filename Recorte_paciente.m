clc
clear all
close all

Filename='AudioU46.wav';
[y,fs]=audioread(Filename);
y2=y(length(y)/2:length(y))
figure(1)
plot(y)
figure(2)
plot(y2)

wavFilename='Paciente_U46.wav';
audiowrite(wavFilename,y2,fs);