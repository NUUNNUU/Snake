'''
Before digging into the whole snake,
Try moving three half cylinders in 3D space

joint 1 through 3 attatched between first and second links
joint 4 through 6 attached between second and third links
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#
def so3(w): # 3x1 numpy array as an input
    w = w/sum(w)
    return np.array([[0, -w[2], w[1]], [w[2], 0, -w[0]], [-w[1], w[0], 0]])

def SO3(w,theta): # Rodrigues formula
    # exp([w]*theta) = I + sin(theta)*[w] + (1-cos(theta))*[w]^2
    return np.eye(3,dtype=int)+np.dot(np.sin(theta),so3(w))+np.dot(1-np.cos(theta),np.dot(so3(w),so3(w)))

def Screw(w,q,h=0):
    W = so3(w)
    Q = q.reshape(3,1)
    V = -np.dot(W,q)+np.dot(w,h) # was h scalar?
    S = np.vstack((np.hstack((W,V.reshape(3,1))),np.zeros((1,4))))
    return S

def G_func(w, theta):
    # G(theta)=I*theta + (1-cos(theta))*[w] + (theta-sin(theta))*[w]^2
    return np.dot(np.eye(3,dtype=int),theta)+np.dot((1-np.cos(theta)),so3(w))+np.dot((theta-np.sin(theta)),np.dot(so3(w),so3(w)))

def exponent(S, theta):

    pass

def Transf(model, init): # modeled matrix and initial position
    pass
#
