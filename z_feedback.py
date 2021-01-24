import numpy as np
import control
from gamma_feedback import AgC, BgC, CgC, DgC, KgC
from sisopy31 import *
import matplotlib.pyplot as plt


# Open loop definition
#Az = AgC - (KgC*np.dot(BgC,CgC))
#Bz = KgC * BgC
#Cz = np.array([[0, 0, 0, 0, 1]])
#Dz = KgC*DgC
Az= AgC
Bz = BgC
Cz = CgC
Dz = DgC


# Open loop analysis
sys = control.StateSpace(Az,Bz,Cz,Dz)
res = control.damp(sys)
tf_z = control.tf(sys)

# Closed loop gain
Kz = 0.00232     # On zoom beaucoup et on cherche une valeur tq OS <= 5% et xi >= 0.5 et on minimise tr
   
# Closed loop definition
Az2 = Az - (Kz * np.dot(Bz,Cz))
Bz2 = Kz * Bz
Cz2 = np.array([[0, 0, 0, 0, 1]])
Dz2 = Kz*Dz


# Closed loop analysis
print("Z closed loop")
print(Az2, Bz2, Cz2, Dz2)
sys2 = control.StateSpace(Az2, Bz2, Cz2, Dz2)
res2 = control.damp(sys2)
print("damp z closed : ")
control.damp(sys2)
tf_z2 = control.tf(sys2)

print("Transfer function : ", tf_z2)
print("pulsation 1 : ", res[0][0]*2*np.pi, " rad/s")
print("pulsation 2 : ", res[0][1]*2*np.pi, " rad/s")
print("pulsation 3 : ", res[0][2]*2*np.pi, " rad/s")
sys = control.ss(Az, Bz, Cz, Dz)

# Graphs and tuning
if __name__ == "__main__":
    sisotool(sys)
    T, yout = control.step_response(tf_z)
    plt.plot(T,yout)
    plt.title("Step resonse z feedback")
    plt.xlabel("Time sample")
    plt.ylabel("Amplitude")
    plt.show()
