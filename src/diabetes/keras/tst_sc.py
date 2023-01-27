import pandas as pd
import numpy as np

path = '../../../datasets/diabetes/tst.csv'

# Read the data
df = pd.read_csv(path)
print(df.head())

# Scale the data
from sklearn.preprocessing import StandardScaler

print()
print("X_train before scaling")
print(df)
scaler = StandardScaler()
df = scaler.fit_transform(df)
print()
print("X_train after scaling")
print(df)
print()

