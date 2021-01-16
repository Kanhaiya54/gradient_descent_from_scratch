import numpy as np
import pandas as pd



def gradient_descent(x,y):
    m_curr = b_curr = 0
    iterations = 1000
    n=len(x)
    lr = 0.08
    
    for i in range(iterations):
        y_predicted = m_curr*x+b_curr
        cost_function = (1/n)*sum([val**2 for val in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - lr * md
        b_curr = b_curr - lr * bd
        print("m {},b {} ,cost function {},iteration {}".format(m_curr,b_curr,cost_function,i))

x = np.array([1,2,3,4,5]) #input values
y = np.array([5,7,9,11,13]) #output values

gradient_descent(x,y)

#cost function = Summation(1/n(actual-predicted)^2)
#predicted = (m*x+b)
#cost function = Summation(1/n(y-(m*+b))^2)
# in order to get a better cost function, we will need optimal values of m,b
# So find the best values of m,b with respect to cost function, by derivatives.
#start with m=0,b=0, find cost_function.
#Recalculate m,b values(optimized values)
# new(m)=old(m)-lr*(d(cost_fn)/dm)
# new(b)=old(b)-lr*(d(cost_fn)/db)
#find cost function, a better ones.




