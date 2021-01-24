import numpy as np
import control
from StateSpaceModel import A_reduced, B_reduced, Cq, Dq
from sisopy31 import *
import matplotlib.pyplot as plt

Kq = -0.19235

Aq = A_reduced - (Kq * np.dot(B_reduced,Cq))
Bq = Kq * B_reduced

print("q state space :")
print(Aq, Bq, Cq, Dq)

print("State space, damp, tf")
sys = control.StateSpace(Aq, Bq, Cq, Dq)
res = control.damp(sys)
tf_k = control.tf(sys)



print("Transfer function : ", tf_k)
print("pulsation 1 : ", res[0][0]*2*np.pi, " rad/s")
print("pulsation 2 : ", res[0][1]*2*np.pi, " rad/s")
print("pulsation 3 : ", res[0][2]*2*np.pi, " rad/s")

print("ss")
sys = control.ss(Aq, Bq, Cq, Dq)

if __name__ == "__main__":
    sisotool(sys)

    T, yout = control.step_response(tf_k)
    plt.plot(T,yout)
    plt.title("Step response q feedback loop")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude (rad/s)")
    plt.show()

    tau = 2/(res[0][1]*2*np.pi)
    print("tau < ", tau)
