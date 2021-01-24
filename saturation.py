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


def dicho(alpha):
    # trouver alphamax
    alpha_0 = 0.012
    deltan_z = (alpha - alpha_eq) / (alpha_eq - alpha_0)
    alphamax = alpha_eq + (alpha_eq - alpha_0)*deltan_z


    #dichotomie - gamamax (0 - pi, bornes)
    #step de boucle fermée gamma avec gamma actuel
    #alpha = max de la step response

    # how I do to get alpha ?
    tf_s = control.tf(sys)
    T, yout = control.step_response(tf_s)
    t, y = control.step_response(sys)
    step()





