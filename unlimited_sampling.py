import numpy as np
import scipy as sp
import math 

def reconstruction_unlimited_sampling(y, lamb, beta, T, omega):
    try: 
        J=int(beta*6/lamb)
        N=math.ceil((math.log(lamb)-math.log(beta))/(math.log(T*Omega*math.e)))
        delta_n_y=np.diff(samples, N)
        m_delta_n_y=np.mod(delta_n_y, [2*lamb])
        delta_n_epsilon= m_delta_n_y -delta_n_y
        s_i_1=delta_n_epsilon
        for i in range(N-1):
            s_i=s(s_i_1, lamb)
            k_i=k(np.cumsum(np.cumsum(s_i_1)) , beta, J)
            s_i+=2*lamb*k_i
            s_i_1=s_i


        
    except:
        pass



def s(y, lamb):
    return 2*lamb*np.ceil(np.floor(np.cumsum(y)/lamb)/2)

def k(s_i, beta, J  ):
    return math.floor((s_i[1]-s_i[J+1])/(12*beta)+1/2)

print("H")