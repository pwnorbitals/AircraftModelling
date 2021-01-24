import numpy as np
import control
from z_feedback import Az, Bz, Cz, Dz, Kz
from Tp1_study import new_alpha_eq as alpha_eq
from sisopy31 import *
import matplotlib.pyplot as plt

As = Az - Kz*np.dot(Bz,Cz)
Bs = Kz * Bz
Cs = np.array([[0, 1, 0, 0, 0]])
Ds = Kz*Dz
sys = control.ss(As, Bs, Cs, Ds)

# how I do to get alpha ?
tf_s = control.tf(sys)
T, yout = control.step_response(tf_s)

alpha_0 = 0.012


def dicho(gamma_min=0, gamma_max=math.pi):
    # trouver alphamax
    
    deltan_z = (alpha - alpha_eq) / (alpha_eq - alpha_0)
    alphamax = alpha_eq + (alpha_eq - alpha_0)*deltan_z

    #dichotomie - gamamax (0 - pi, bornes)
    #step de boucle fermée gamma avec gamma actuel
    #alpha = max de la step response

    tf_s = control.tf(sys)
    tstep = 0.1
    tmax = 15
    t = list(np.arange(0, tmax, tstep))

    gamma_med = gamma_min / gamma_max
    u = [gamma] * (tstep * tmax)
    t, y = control.forced_response(sys, t, u)
    alphamax_med = max(y)

    epsilon = 0.001

    if ((alphamax / alphamax_med) - 1) < epsilon:
        return gamma_med
    else:
        if alphamax > alphamax_med:
            return dicho(gamma_min, gamma_med)
        elif alphamax < alphamax_med:
            return dicho(gamma_med, gamma_max)

gamma = dicho()
print(gamma)




