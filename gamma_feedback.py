import numpy as np
import control
from q_feedback import Ak, Bk, Ck, Dk, Kr
from StateSpaceModel import A_reduced, B_reduced, Cq, Dq
from sisopy31 import *
import matplotlib.pyplot as plt



#Ag = Ak - Kr*np.dot(Bk,Ck)
#Bg = Kr * Bk

Ag = A_reduced - (Kr * np.dot(B_reduced,Cq))
Bg = Kr * B_reduced

Cg = np.array([[1, 0, 0, 0, 0]])
Dg = Kr*Dk

sys = control.StateSpace(Ag,Bg,Cg,Dg)
res = control.damp(sys)
print("damp : ")
control.damp(sys)
tf_g = control.tf(sys)

if __name__ == "__main__":
    sisotool(sys)

Kg1 = 23.94 # On a modifié le code interne de sisopy31 en modifiant le Gain max à 70 (l.386 kmax),
# on a zoomé sur le graphe et cherché le tr opti tq PM >= 7db et GM >= 35°


Kg2 = 19.92 # Pb -> OS est toujours à 0%

print("Transfer function : ", tf_g)
print("pulsation 1 : ", res[0][0]*2*np.pi, " rad/s")
print("pulsation 2 : ", res[0][1]*2*np.pi, " rad/s")
print("pulsation 3 : ", res[0][2]*2*np.pi, " rad/s")

sys = control.ss(Ag, Bg, Cg, Dg)
if __name__ == "__main__":
    T, yout = control.step_response(tf_g)
    plt.plot(T,yout) # T ou yout
    plt.title("Step resonse gama feedback")
    plt.xlabel("Time sample")
    plt.ylabel("Amplitude")
    plt.show()

