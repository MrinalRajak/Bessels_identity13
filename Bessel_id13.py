
#Bessel's identity
#(13)

import numpy as np
from scipy.special import jn
from scipy.integrate import quad
from scipy.misc import derivative

x=float(input("Enter the x: "))
n=1
theta=int(input("Enter the theta: "))
LHS=np.cos(x*np.sin(theta))
term= 2*jn(2*n,x)*np.cos(2*n*theta)
RHS=jn(0,x)+term
s=0.0
while(abs(LHS-RHS)>1.0e-5):
    term= 2*jn(2*n,x)*np.cos(2*n*theta)
    s=s+term
    RHS= jn(0,x)+s
    n=n+1
print("LHS: ",LHS)
print("RHS: ",RHS)
