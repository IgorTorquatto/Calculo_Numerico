import numpy as np

x= np.array([1,2,3,4])
y= np.array([1,2,3,4])

xx = np.concatenate((x,[x[0]]))
xy = np.concatenate((y,[y[0]]))

S1= np.dot(xx[0:-1],xy[1:])
S2= np.dot(xx[1:],xy[0:-1])

S1,S2