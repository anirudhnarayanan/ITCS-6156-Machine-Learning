#!/usr/bin/env python

import numpy as np
from gradient_descent import GradientDescent
#import matplotlib.pyplot as plt



x = np.array([[1,10,100],[2,20,200],[3,30,300],[4,40,400],[5,50,500]])
y = np.array([[160],[320],[480],[640],[800]])

#x = np.array([[1],[2],[3],[4],[5]])
#y = np.array([[2],[4],[6],[8],[10]])

a = GradientDescent(x,y)

#plt.plot(x,y)
#plt.show()

print a.hypothesis(1)

print a.cost_function(1)


print a.stochastic_gradient_descent(0.1)
#a.batch_gradient_descent(0.1,25)
#print(a.least_squares())

print a.cost_function(0)
