# To support both python 2 and python 3
from __future__ import division, print_function, unicode_literals
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
np.random.seed(2)
#libraries

X = np.random.rand(1000, 1) #array 1000*1, values in range [0,1]
y = 4 + 3 * X + .2*np.random.randn(1000, 1) # noise added #randn values have mean of 0 and standard deviation of 1

# Building Xbar 
one = np.ones((X.shape[0],1)) #array (1000,1) filled with ones
Xbar = np.concatenate((one, X), axis = 1) #columns concatenate
A = np.dot(Xbar.T, Xbar) #np.dot = matrix multiplication; .T = maxtrix transpose
b = np.dot(Xbar.T, y)
w_lr = np.dot(np.linalg.pinv(A), b)  #linear regression formula
print('Solution found by formula: w = ',w_lr.T)

# Display result
w = w_lr
w_0 = w[0][0]
w_1 = w[1][0]
x0 = np.linspace(0, 1, 2, endpoint=True) #create space to display result
y0 = w_0 + w_1*x0

# Draw the fitting line 
plt.plot(X.T, y.T, 'b.')     # data ? .T
plt.plot(x0, y0, 'r', linewidth = 2)   # the fitting line
plt.axis([0, 1, 0, 10])
plt.show()

def grad(w):
    N = Xbar.shape[0]
    return 1/N * Xbar.T.dot(Xbar.dot(w) - y) #gradient formula

def cost(w):
    N = Xbar.shape[0]
    return .5/N*np.linalg.norm(y - Xbar.dot(w), 2)**2;
def numerical_grad(w, cost):
    eps = 1e-4
    g = np.zeros_like(w)
    for i in range(len(w)):
        w_p = w.copy()
        w_n = w.copy()
        w_p[i] += eps 
        w_n[i] -= eps
        g[i] = (cost(w_p) - cost(w_n))/(2*eps) #widely used approximation
    return g 

def check_grad(w, cost, grad): #ktra dao ham tinh dc vs numerical grad
    w = np.random.rand(w.shape[0], w.shape[1])
    grad1 = grad(w)
    grad2 = numerical_grad(w, cost)
    return True if np.linalg.norm(grad1 - grad2) < 1e-6 else False 

print( 'Checking gradient...', check_grad(np.random.rand(2, 1), cost, grad))

def myGD(w_init, grad, eta):
    w = [w_init]
    for it in range(100):
        w_new = w[-1] - eta*grad(w[-1]) 
        if np.linalg.norm(grad(w_new))/len(w_new) < 1e-3: #formula
            break 
        w.append(w_new)
    return (w, it) 
#luu lai mang w hoi vo nghia khi ma chi dung phan tu cuoi cung..
w_init = np.array([[2], [1]])
(w1, it1) = myGD(w_init, grad, 1)


print('Solution found by GD: w = ', w1[-1].T, ',\nafter %d iterations.' %(it1+1))

w = w1[-1].T;
w_0 = w[0][0]
w_1 = w[0][1]
x0 = np.linspace(0, 1, 2, endpoint=True) #create space to display result
y0 = w_0 + w_1*x0

# Draw the fitting line 
plt.plot(X.T, y.T, 'b.')     # data ? .T
plt.plot(x0, y0, 'r', linewidth = 2)   # the fitting line
plt.axis([0, 1, 0, 10])
plt.show()
