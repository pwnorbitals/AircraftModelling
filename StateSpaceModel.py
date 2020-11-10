import numpy as np

from Tp1_study import r_g, Cz_eq, V_eq, Q, S, Cx_eq, m, new_F_px, new_alpha_eq, Cx_delta_m, l_ref, X, Y, k, Cz_alpha


Cz_alpha = 2.2
gamma_eq = 0
Ftho = 0
Cm_q = -0.27
IYY = m * r_g**2

Cz_delta_m = 0.35

Cx_alpha = 2*k*Cz_eq*Cz_alpha
Cm_alpha = X / l_ref * (Cx_alpha * np.sin(new_alpha_eq) + Cz_alpha * np.cos(new_alpha_eq))
Cm_delta_m = Y / l_ref * (Cx_delta_m * np.sin(new_alpha_eq) + Cz_delta_m * np.cos(new_alpha_eq))


g0 = -9.81

Xv = 2 * Q *S * Cx_eq / (m * V_eq) #

Xalpha = new_F_px / (m * V_eq) * np.sin(new_alpha_eq) + Q*S*Cx_alpha/(m*V_eq) #
Xgamma = g0 * np.cos(gamma_eq) / V_eq
Xdelta_m = Q *S* Cx_delta_m / (m * V_eq)
Xtho = - Ftho * np.cos(new_alpha_eq) / (m*V_eq) #

mv = 0
malpha = Q*S*l_ref**2 * Cm_alpha / IYY #
mq = Q*S*l_ref**2*Cm_q / (V_eq*IYY) #
mdelta_m = Q*S*l_ref*Cm_delta_m / IYY #

Zv = 2*Q*S*Cz_eq / (m*V_eq) #
Zalpha = new_F_px * np.cos(new_alpha_eq) / (m * V_eq) + Q*S*Cz_alpha / (m*V_eq) #
Zgamma = g0*np.sin(gamma_eq) / V_eq
Zdelta_m = Q*S*Cz_delta_m / (m*V_eq) #
Ztho = Ftho * np.sin(new_alpha_eq) / (m*V_eq)

