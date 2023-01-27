import pandas as pd
import numpy as np

path = '../../../datasets/diabetes/diabetes.csv'

# Read the data
df = pd.read_csv(path)
print(df.head())

# Split the data into train and test
from sklearn.model_selection import train_test_split

X = df.drop('Outcome', axis=1)
y = df['Outcome']





X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Scale the data
from sklearn.preprocessing import StandardScaler

print()
print("X_train before scaling")
print(X_train)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print()
print("X_train after scaling")
print(X_train)
print()


pause = input("Press enter to continue")

# Build the model
import tensorflow as tf
from tensorflow import keras
from keras.layers import Dense
from keras.models import Sequential

model = Sequential()
model.add(Dense(128, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=["accuracy"])

# Train the model
model.fit(x=X_train, y=y_train, epochs=200, validation_data=(X_test, y_test))

# Evaluate the model
losses = pd.DataFrame(model.history.history)
losses.plot()

# Predictions
print("Predictions")
predictions = model.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix

#print("Classification Report")
#print(classification_report(y_test, predictions))
#print("Confusion Matrix")
#print(confusion_matrix(y_test, predictions))

# Save the model
model.save('diabetes_nn_model.h5')

# Load the model
#from keras.models import load_model
#
#new_model = load_model('diabetes_nn_model.h5')
