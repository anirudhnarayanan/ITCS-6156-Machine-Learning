#!/usr/bin/env python

import numpy as np




class GradientDescent:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.thetas = np.zeros(x.shape[1])
        self.thetas = np.asmatrix(self.thetas)
        self.data_size = x.shape[0]
        self.parameter_size = x.shape[1]


    def hypothesis(self,i):
        feature_vector = np.asmatrix(self.x[i]).T
        return float(self.thetas.dot(feature_vector))

    def cost_function(self,i):
        return self.hypothesis(i) - float(self.y[i])

    
    def stochastic_gradient_descent(self,alpha):
        for i in range(self.data_size):
            error = self.cost_function(i)
            print error
            print self.x[i]
            update_value = (alpha*error)*self.x[i]
            print update_value
            self.thetas = self.thetas - update_value
            print self.thetas
        print "returning stochastic"
        return self.thetas
    
    def batch_gradient_descent(self,alpha,iterations):
        for i in range(iterations):
            x_transpose = self.x.T
            temp = self.thetas.dot(self.x.T)
            error = temp.T - self.y
            print "error"
            print error.T
            new_x = error.T.dot(self.x)
            self.thetas = self.thetas - ((alpha/self.data_size)*new_x)
            print "thetas"
            print self.thetas

        return self.thetas

    def least_squares(self):
        xtx = self.x.T.dot(self.x) 
        print xtx
        print xtx.shape
        self.thetas = np.linalg.pinv(xtx).dot(self.x.T).dot(self.y)
        self.thetas = self.thetas.T
        return self.thetas.T
    

        

            
            

        

