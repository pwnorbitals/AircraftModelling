import numpy as np
import control
from StateSpaceModel import A_reduced, B_reduced
from sisopy31 import *
import matplotlib.pyplot as plt

# Open loop definition
Cq = np.array([[0, 0, 1, 0, 0]])
Dq = np.array([[0]])

# Open loop analysis
sys_qopen = ss(A_reduced, B_reduced, Cq, Dq)
tf_open = control.tf(sys_qopen)

# Closed loop gain
Kq = -0.19235

# Closed loop definition
Aq = A_reduced - (Kq * np.dot(B_reduced,Cq))
Bq = Kq * B_reduced


# Closed loop analysis
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

# Washout filter
tau = 2/(res[0][1]*2*np.pi)
num = [tau]
den = [tau, 1]
sys_t = control.tf(num, den)
Ktau = control.dcgain(sys_t)

Aq_tau = A_reduced - (Ktau * np.dot(B_reduced,Cq))
Bq_tau = Ktau * B_reduced
systau = control.StateSpace(Aq_tau, Bq_tau, Cq, Dq)
tf_tau = control.tf(systau)






# Graphs and tuning
if __name__ == "__main__":
    control.matlab.damp(sys_qopen)
    #sisotool(-sys_original)

    sisotool(sys)

    T, yout = control.step_response(tf_k)
    T_tau, youtau = control.step_response(tf_tau)
    T_open,youtopen = control.step_response(tf_open)
    plt.plot(T,yout, label='Closed loop')
    plt.plot(T,youtau, label ='Whasout filter')
    plt.plot(T,youtopen, label ='Open loop')
    plt.title("Step response")
    plt.legend()
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude (rad/s)")
    plt.show()





    
