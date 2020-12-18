import numpy as np
import control
from StateSpaceModel import A_reduced, B_reduced, Cq, Dq

Kr = -0.18817

Ak = A_reduced - Kr * np.dot(B_reduced,Cq)
Bk = Kr * B_reduced
Ck = Cq # As we want q as an output
Dk = Dq # = 0


sys = control.StateSpace(Ak,Bk,Ck,Dk)
res = control.damp(sys)
tf_k= control.tf(sys)


print("Transfert function : ", tf_k)
print("pulsation 1 : ", res[0][0]*2*np.pi, " rad/s")
print("pulsation 2 : ", res[0][1]*2*np.pi, " rad/s")
print("pulsation 3 : ", res[0][2]*2*np.pi, " rad/s")
