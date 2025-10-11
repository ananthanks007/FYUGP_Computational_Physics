import numpy as np

# Trapezoidal Rule for given set of values


t = np.array([0,2,4,6,8,10])
v = np.array([0,6,10,14,18,20])

def trapez(t,v):
    h = t[1] - t[0]

    v_0 = v[0]
    v_n = v[-1]
    v_sum = np.sum(v[1:-1]) # sum of all middle terms

    s = (h/2) * (v_0 + 2*v_sum+ v_n)

    return s

integral = trapez(t,v)
print(integral)



