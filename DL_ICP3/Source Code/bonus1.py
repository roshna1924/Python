import tensorflow as tf
from keras.models import Sequential
from keras import layers
from keras.preprocessing.text import Tokenizer
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.layers import Embedding
import matplotlib.pyplot as plt
import numpy as np
from keras.layers import Flatten
from keras.callbacks import TensorBoard
from time import time

df = pd.read_csv('imdb_master.csv', encoding='latin-1')
print(df.head())
df = df[df['label'] != 'unsup']  # Dropping Unnecessary labelfrom dataset
sentences = df['review'].values
y = df['label'].values

# tokenizing data
tokenizer = Tokenizer(num_words=2000)
tokenizer.fit_on_texts(sentences)
# getting the vocabulary of data
sentences = tokenizer.texts_to_matrix(sentences)
le = preprocessing.LabelEncoder()
y = le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(sentences, y, test_size=0.25, random_state=1000)

# Number of features
# print(input_dim)
model = Sequential()
model.add(Embedding(2000, 50, input_length=2000))
model.add(Flatten())
model.add(layers.Dense(300, input_dim=2000, activation='relu'))
model.add(layers.Dense(3, activation='softmax'))

tensorborad = TensorBoard(log_dir="logs/{}".format(time()))

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['acc'])

model.fit(X_train, y_train,
          batch_size=256,
          epochs=2,
          verbose=1,
          validation_data=(X_test, y_test),
          callbacks=[tensorborad])

history = model.fit(X_train, y_train, epochs=3, verbose=True, validation_data=(X_test, y_test), batch_size=256)

# For accuracy values
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# For loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()