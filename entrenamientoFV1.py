# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 11:37:56 2018

@author: silva
"""

import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#entrenamiento=np.zeros([25,13733])
target=np.zeros(25)
cont=0

df = pd.read_csv('BDD.csv',header=None)
entrenamiento=np.array(df)
entrenamiento=entrenamiento.transpose()
target=np.loadtxt('BDD.dat')

from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
x_train, x_test, target_train, target_test= train_test_split(entrenamiento,target,test_size=1,random_state=0)

target_train=to_categorical(target_train,5)
target_test=to_categorical(target_test,5)
# centrar los Datos
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_Train=sc.fit_transform(x_train)
X_Test=sc.transform(x_test)

import keras
from keras.models import Sequential
from keras.layers import Dense,Flatten

# Crear La Rede Neuronal como un Objeto
classifier=Sequential()

classifier.add(Dense(output_dim=11, init='uniform',activation='relu',input_dim=50000 ))
classifier.add(Dense(output_dim=9, init='uniform',activation='relu' ))
classifier.add(Dense(output_dim=7, init='uniform',activation='relu' ))
classifier.add(Dense(output_dim=5, init='uniform',activation='softmax'))


classifier.compile('adam',  loss='categorical_crossentropy', metrics=['accuracy'] )
classifier.summary()
classifier.fit(X_Train,target_train, batch_size=40, nb_epoch=200)

y=classifier.predict(X_Test)
print(target_test)
print(y)


from keras.models import model_from_json
# serialize model to JSON
redvocales_json = classifier.to_json()
with open("red_vocalesE.json", "w") as json_file:
    json_file.write(redvocales_json)
# serialize weights to HDF5
classifier.save_weights("red_vocalesE.h5")
print("Saved red to disk")
