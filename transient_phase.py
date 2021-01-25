import numpy as np
import control
import matplotlib.pyplot as plt


from StateSpaceModel import A,B

A_ph = A[:2,:2]
print("A_ph",A_ph)
B_ph = B[:2,0].reshape((2,1))
print("B_ph", B_ph)
C_ph = np.eye(2)
D_ph = np.zeros((2,1))

A_sp = A[2:4,2:4]
print("A_sp" , A_sp)
B_sp = B[2:4,0].reshape((2,1))
print("B_sp ", B_sp)
C_sp = np.eye(2)
D_sp = np.zeros((2,1))


print("\nPhugoid\n")
sys = control.StateSpace(A_ph,B_ph,C_ph,D_ph)
res = control.damp(sys)
tf_ph = control.tf(sys)
print("Transfert function : ", tf_ph)
T_ph, yout_ph = control.step_response(tf_ph)
#print("T_ph.shape ", T_ph.shape)
#print("yout_ph.shape ", yout_ph.shape)
#print("yout_ph[0,:].shape ",yout_ph[0,:].shape )


plt.plot(T_ph, yout_ph[0,:]) # V in m/s
plt.title("V Step Response")
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude in m/s')
plt.show()


plt.plot(T_ph, yout_ph[1,:])
plt.title('Gamma Step Response')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude in rad')
plt.show()



print("\nShort Frequency\n")
sys = control.StateSpace(A_sp,B_sp,C_sp,D_sp)
res = control.damp(sys)
tf_sp = control.tf(sys)
print("Transfer function : ", tf_sp)
T_sp, yout_sp = control.step_response(tf_sp)

plt.plot(T_sp, yout_sp[0,:]) # Gamma
plt.title("Alpha Step Response")
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude in rad')
plt.show()

plt.plot(T_sp, yout_sp[1,:]) # Alpha
plt.title('q Step Response')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude in rad/s')
plt.show()






