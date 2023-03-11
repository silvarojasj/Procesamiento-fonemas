# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 17:47:04 2019

@author: silva
"""

import pyaudio
import wave

def Grabar():
    FORMAT=pyaudio.paInt16
    CHANNELS=1
    RATE=44100
    CHUNK=1024
    duracion=5
    archivo="grabacion.wav"
    
    #iniciamos "pyaudio"
    
    audio=pyaudio.PyAudio()
    stream=audio.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
    
    
    #iniciamos Grabacion
    
    print("grabando...")
    frames=[]
    for i in range(0,int (RATE/CHUNK*duracion)):
        data=stream.read(CHUNK)
        frames.append(data)
    print("grabacion terminada")
    
    
    #detenemos grabacion 
    
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    #crear/guardar archivo de audio
    waveFile=wave.open(archivo,'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    print("procesando")
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    