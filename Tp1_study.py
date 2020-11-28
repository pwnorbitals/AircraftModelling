### Study of the uncontrolled aircraft

import numpy as np


def T_P(h):
    # h in meter
    if 0 <= h <= 11000:
        Pt = 101325
        Ht = 0
        Tt = 288.15
        pente = -6.5

    elif 11000 < h <= 20000:
        Pt = 22632
        Ht = 11000
        pente = 0
        Tt = 216.65

    elif 20000 < h <= 32000:
        Pt = 5474.9
        Ht = 20000
        pente = 1
        Tt = 216.65

    elif 32000 < h <= 47000:
        Pt = 868.018
        Ht = 32000
        Tt = 228.65
        pente = 2.8

    elif 47000 < h <= 51000:
        Pt = 110.91
        Ht = 47000
        Tt = 270.65
        pente = 0

    elif 51000 < h <= 71000:
        Pt = 66.94
        Ht = 51000.
        Tt = 270.65
        pente = -2.8

    elif 71000 < h <= 80000:
        Pt = 3.96
        Ht = 71000
        Tt = 214.65
        pente = -2

    if 0 <= h <= 80000:
        T = Tt + (pente / 1000)*(h - Ht)
        g0 = 9.80665
        M = 0.0289644
        R = 8.31446261815324

        if pente == 0:
            P = Pt * np.exp(-(g0 / ((R / M) * T))*(h - Ht))
        if pente != 0:
            P = Pt * (1 + (h / 1000 - Ht / 1000) * pente / Tt)**(-g0 / ((pente / 1000)*(R / M)))
    elif h > 80000:
        print("Error, h over 80 000 meters -> h = ", h)
        T = 'error'
        P = 'error'
    return T, P #Pressure expressed in Pa

def rho(h):

    temp, pressure = T_P(h)
    rho = (pressure * 28.976) / (8.3144621 * temp)

    return rho

def sound_speed(h):

    temp, _ = T_P(h)
    c = 20.05 * np.sqrt(temp)

    return c

def ft2m(h_ft):
    # h_ft = distance in ft
    # h_m = distance in m

    h_m = 0.3048 * h_ft

    return h_m

def compute_equilibrium(Q,S,m, delta_m_0, Cx_0, k, Cz_delta_m, Cz_alpha, X, Y, epsilon):

    alpha_eq = 0
    F_px = 0
    g0 = -9.81

    while(True):
        Cz_eq = 1/(Q*S) * (m*g0 - F_px * np.sin(alpha_eq))
        Cx_eq = Cx_0 + k*Cz_eq**2

        Cx_delta_m = 2 * k *Cz_eq*Cz_delta_m
        delta_m_eq = delta_m_0 - (Cx_eq * np.sin(alpha_eq) + Cz_eq * np.cos(alpha_eq))/(Cx_delta_m * np.sin(alpha_eq) + Cz_delta_m * np.cos(alpha_eq)) * X *(Y - X)

        new_alpha_eq = alpha_eq + Cz_eq / Cz_alpha - Cz_delta_m/ Cz_alpha * delta_m_eq
        new_F_px = Q * S * Cx_eq / np.cos(new_alpha_eq)

        if np.abs(new_alpha_eq - alpha_eq) < epsilon :
            return new_alpha_eq, new_F_px,delta_m_eq, Cx_delta_m, Cx_eq, Cz_eq
        else :
            alpha_eq = new_alpha_eq
            F_px = new_F_px



mach = 1.8
l_ref = 5.24 # m reference length
l_t = 3/2.0 * l_ref # total length
m = 8400 # mass in kg
c = 0.52
S = 34 # m^2 Area
r_g = 2.65 # m Gyration radius

h_m = ft2m(24000)

delta_m_0 = -0.01
C_x0 = 0.029
k = 0.505

Cz_delta_m = 0.34
Xf = 0.608
Xg = -c * l_t
f_delta = 0.9
Xf_delta = f_delta * l_t

Cz_alpha = 2.2

X = Xf - Xg
Y = Xf_delta - Xg

V_eq = mach * sound_speed(h_m)
Q = 1/2. * rho(h_m) * V_eq**2

epsilon = 1e-3

new_alpha_eq, new_F_px, delta_m_eq, Cx_delta_m, Cx_eq, Cz_eq = compute_equilibrium(Q, S, m, delta_m_0, C_x0, k, Cz_delta_m, Cz_alpha, X, Y, epsilon)

if __name__ == "__main__":
    print("new_alpha_eq ", new_alpha_eq * 180/np.pi)





