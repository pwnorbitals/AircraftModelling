import numpy as np
import control
from z_feedback import Az, Bz, Cz, Dz, Kz
from gamma_feedback import AgC, BgC, CgC, DgC
from Tp1_study import new_alpha_eq as alpha_eq
from sisopy31 import *
import matplotlib.pyplot as plt

As = AgC
Bs = BgC
Cs = CgC
Ds = DgC
sys = control.ss(As, Bs, Cs, Ds)


# how I do to get alpha ?
tf_s = control.tf(sys)
T, yout = control.step_response(tf_s)

alpha_0 = 0.012
deltan_z = 2.8
alphamax = alpha_eq + (alpha_eq - alpha_0)*deltan_z
epsilon = 0.001

def dicho(gamma_min=0, gamma_max=math.pi):

    tf_s = control.tf(sys)
    tstep = 0.1
    tmax = 15
    t = list(np.arange(0, tmax, tstep))

    gamma_med = (gamma_min + gamma_max)/2
    u = [gamma_med] * (round(1/tstep) * tmax)
    tout, yout, xout = control.forced_response(sys, t, u)
    alphamax_med = max(yout)

    print("gamma_med : ", gamma_med)
    #plt.plot(tout, yout)
    #plt.show()

    if alphamax_med ==0:
        raise "What ?!"
    
    print(alphamax, alphamax_med)

    if (np.abs(alphamax_med - alphamax)/alphamax) < epsilon:
        return gamma_med
    else:
        if alphamax > alphamax_med:
            return dicho(gamma_min, gamma_med)
        elif alphamax < alphamax_med:
            return dicho(gamma_med, gamma_max)

gamma = dicho()
print(gamma)




