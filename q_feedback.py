import numpy as np
import control
from StateSpaceModel import A_reduced, B_reduced, Cq, Dq
from sisopy31 import *
import matplotlib.pyplot as plt

Kr = -0.18817

Ak = A_reduced - (Kr * np.dot(B_reduced,Cq))
Bk = Kr * B_reduced
Ck = Cq # As we want q as an output
Dk = Dq # = 0


sys = control.StateSpace(Ak,Bk,Ck,Dk)
res = control.damp(sys)
tf_k= control.tf(sys)


print("Transfer function : ", tf_k)
print("pulsation 1 : ", res[0][0]*2*np.pi, " rad/s")
print("pulsation 2 : ", res[0][1]*2*np.pi, " rad/s")
print("pulsation 3 : ", res[0][2]*2*np.pi, " rad/s")

sys = control.ss(Ak, Bk, Ck, Dk)

if __name__ == "__main__":
    sisotool(sys)

T, yout = control.step_response(tf_k)
plt.plot(T,yout)
plt.title("Step resonse q feedback")
plt.xlabel("Time sample")
plt.ylabel("Amplitude")
plt.show()

tau = 2/(res[0][1]*2*np.pi)
print("tau = ", tau)
