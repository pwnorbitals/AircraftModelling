import numpy as np
import control
from q_feedback import Aq, Bq, Cq, Dq, Kq
from StateSpaceModel import A_reduced, B_reduced
from sisopy31 import *
import matplotlib.pyplot as plt

# Gamma open loop definition
Ag = A_reduced - (Kq * np.dot(B_reduced,Cq))
Bg = Kq * B_reduced
Cg = np.array([[1, 0, 0, 0, 0]])
Dg = Kq*Dq

# Gamma open loop analysis
sys = control.StateSpace(Ag,Bg,Cg,Dg)
res = control.damp(sys)
print("damp gamma open : ")
control.damp(sys)
tf_g = control.tf(sys)
   
# Gamma closed loop gains
Kg1 = 23.94   # zoom on the graph and minimize tr with PM >= 7db and GM >= 35°
KgC = 19.92   # zoom on the graph and minimize tr with OS < 5% and xi > 0.5

# Gamma closed loop definition
AgC = Ag - (KgC * np.dot(Bg,Cg))
BgC = KgC * Bg
CgC = np.array([[1, 0, 0, 0, 0]])
DgC = KgC*Dg

# Gamma closed loop analysis
print(AgC, BgC, CgC, DgC)
sys2 = control.StateSpace(AgC, BgC, CgC, DgC)
res2 = control.damp(sys2)
print("damp gamma closed : ")
control.damp(sys2)
tf_gC = control.tf(sys2)
print("Transfer function : ", tf_gC)
print("pulsation 1 : ", res2[0][0]*2*np.pi, " rad/s")
print("pulsation 2 : ", res2[0][1]*2*np.pi, " rad/s")
print("pulsation 3 : ", res2[0][2]*2*np.pi, " rad/s")

# Graphs and tuning
if __name__ == "__main__":
    sisotool(sys)
    T, yout = control.step_response(tf_gC)
    plt.plot(T,yout) 
    plt.title("Step response gama feedback")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude (rad)")
    plt.show()

