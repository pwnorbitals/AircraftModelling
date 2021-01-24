import numpy as np
import control
from q_feedback import Aq, Bq, Cq, Dq, Kq
from StateSpaceModel import A_reduced, B_reduced, Cq, Dq
from sisopy31 import *
import matplotlib.pyplot as plt


Ag = A_reduced - (Kq * np.dot(B_reduced,Cq))
Bg = Kq * B_reduced
Cg = np.array([[1, 0, 0, 0, 0]])
Dg = Kq*Dq

sys = control.StateSpace(Ag,Bg,Cg,Dg)
res = control.damp(sys)
print("damp gamma open : ")
control.damp(sys)
tf_g = control.tf(sys)
   

Kg1 = 23.94   # zoom on the graph and minimize tr with PM >= 7db and GM >= 35°
Kg2 = 19.92   # zoom on the graph and minimize tr with OS < 5% and xi > 0.5

Ag2 = Ag - (Kg2 * np.dot(Bg,Cg))
Bg2 = Kg2 * Bg
Cg2 = np.array([[1, 0, 0, 0, 0]])
Dg2 = Kg2*Dg

print(Ag2, Bg2, Cg2, Dg2)

sys2 = control.StateSpace(Ag2, Bg2, Cg2, Dg2)
res2 = control.damp(sys2)
print("damp gamma closed : ")
control.damp(sys2)
tf_g2 = control.tf(sys2)

print("Transfer function : ", tf_g2)
print("pulsation 1 : ", res2[0][0]*2*np.pi, " rad/s")
print("pulsation 2 : ", res2[0][1]*2*np.pi, " rad/s")
print("pulsation 3 : ", res2[0][2]*2*np.pi, " rad/s")

if __name__ == "__main__":
    sisotool(sys)
    T, yout = control.step_response(tf_g2)
    plt.plot(T,yout) 
    plt.title("Step resonse gama feedback")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude (rad)")
    plt.show()

