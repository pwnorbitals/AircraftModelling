import numpy as np

from sisopy31 import *

from Tp1_study import r_g, Cz_eq, V_eq, Q, S, Cx_eq, m, new_F_px, new_alpha_eq, Cx_delta_m, l_ref, X, Y, k
np.set_printoptions(precision=4, suppress=True)

Cz_alpha = 2.2
gamma_eq = 0
Ftho = 0
Cm_q = -0.27
IYY = m * r_g**2
g0 = 9.81

Cz_delta_m = 0.35

Cx_alpha = 2*k*Cz_eq*Cz_alpha
Cm_alpha = X / l_ref * (Cx_alpha * np.sin(new_alpha_eq) + Cz_alpha * np.cos(new_alpha_eq))
Cm_delta_m = Y / l_ref * (Cx_delta_m * np.sin(new_alpha_eq) + Cz_delta_m * np.cos(new_alpha_eq))

Xv = 2 * Q *S * Cx_eq / (m * V_eq) 

Xalpha = new_F_px / (m * V_eq) * np.sin(new_alpha_eq) + Q*S*Cx_alpha/(m*V_eq) 
Xgamma = g0 * np.cos(gamma_eq) / V_eq
Xdelta_m = Q *S* Cx_delta_m / (m * V_eq)
Xtho = - Ftho * np.cos(new_alpha_eq) / (m*V_eq) 

mv = 0
malpha = Q*S*l_ref * Cm_alpha / IYY 
mq = Q*S*l_ref**2*Cm_q / (V_eq*IYY) 
mdelta_m = Q*S*l_ref*Cm_delta_m / IYY 

Zv = 2*Q*S*Cz_eq / (m*V_eq) 
Zalpha = new_F_px * np.cos(new_alpha_eq) / (m * V_eq) + Q*S*Cz_alpha / (m*V_eq) 
Zgamma = g0*np.sin(gamma_eq) / V_eq
Zdelta_m = Q*S*Cz_delta_m / (m*V_eq) 
Ztho = Ftho * np.sin(new_alpha_eq) / (m*V_eq)


A = np.array([
        [-Xv, -Xgamma, -Xalpha, 0, 0, 0],
        [Zv, 0, Zalpha, 0, 0, 0],
        [-Zv, 0, -Zalpha, 1, 0, 0],
        [0, 0, malpha, mq, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, V_eq, 0, 0, 0, 0]
    ])

B = np.c_[[0, Zdelta_m, -Zdelta_m, mdelta_m, 0, 0]]
C = np.eye(6)
D = np.zeros((6,1))
sys_original = ss(A, B, C, D)
print(A)
print(B)


A_reduced = A[1:6, 1:6]
B_reduced = B[1:6, 0:1]
Cq = np.array([[0, 0, 1, 0, 0]])
Dq = np.array([[0]])

sys = ss(A_reduced, B_reduced, Cq, Dq)

if __name__== "__main__":
    control.matlab.damp(sys_original)
    sisotool(-sys)
    print("A_reduced", A_reduced)
    print("B_reduced", B_reduced)


