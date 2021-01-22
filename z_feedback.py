import numpy as np
import control
from gamma_feedback import Ag, Bg, Cg, Dg, Kg2
from sisopy31 import *
import matplotlib.pyplot as plt

Az = Ag - Kg2*np.dot(Bg,Cg)
Bz = Kg2 * Bg


Cz = np.array([[0, 0, 0, 0, 1]])
Dz = Kg2*Dg

sys = control.StateSpace(Az,Bz,Cz,Dz)
res = control.damp(sys)
tf_z = control.tf(sys)

Kz = 0.00232# On zoom beaucoup et on cherche une valeur tq OS <= 5% et xi >= 0.5 et on minimise tr
if __name__ == "__main__":
    sisotool(sys)

print("Transfer function : ", tf_z)
print("pulsation 1 : ", res[0][0]*2*np.pi, " rad/s")
print("pulsation 2 : ", res[0][1]*2*np.pi, " rad/s")
print("pulsation 3 : ", res[0][2]*2*np.pi, " rad/s")

sys = control.ss(Az, Bz, Cz, Dz)
if __name__ == "__main__":
    T, yout = control.step_response(tf_z)
    plt.plot(T,yout) # T ou yout
    plt.title("Step resonse z feedback")
    plt.xlabel("Time sample")
    plt.ylabel("Amplitude")
    plt.show()
