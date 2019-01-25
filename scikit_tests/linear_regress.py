#!.usr/bin/env python
from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([1,2,3])
y = np.array([2,4,6])

X = x[:,np.newaxis]
model = LinearRegression(normalize=True)

print model.normalize

print model

model.fit(X,y)
print(model.coef_)
