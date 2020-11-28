import numpy as np
import control


from StateSpaceModel import A,B,C,D

A_ph = A[:2,:2]
B_ph = B[2:4,0].reshape((2,1))
C_ph = np.eye(2)
D_ph = np.zeros((2,1))

A_sp = A[2:4,2:4]
B_sp = B[2:4,0].reshape((2,1))
C_sp = np.eye(2)
D_sp = np.zeros((2,1))

print("A_sp", A_sp.shape)
#print("B_ph", B_ph)

print("\nPhugoid\n")
sys = control.StateSpace(A_ph,B_ph,C_ph,D_ph)
res = control.damp(sys)
tf_ph = control.tf(sys)
T_ph, yout_ph = control.step_response(tf_ph)


print("\nShort Frequency\n")
sys = control.StateSpace(A_sp,B_sp,C_sp,D_sp)
res = control.damp(sys)
tf_sp = control.tf(sys)
T_sp, yout_sp = control.step_response(tf_sp)

# polynome_c = np.poly(Ar)
# roots = np.roots(polynome_c)
#
# print(polynome_c)
# print("\n",roots)


# frequency_short_preriod = np.sqrt(roots[0] * roots[1])
# dumping_short_period = (roots[0] + roots[1])/(2 * frequency_short_preriod)
#
# frequency_phugoid = np.sqrt(roots[2] * roots[3])
# dumping_phugoid = (roots[2] + roots[3])/(2 * frequency_phugoid)
#
# print("frequency_short_preriod ", frequency_short_preriod)
# print("dumping_short_period ", dumping_short_period)
#
# print("frequency_phugoid ", frequency_phugoid)
# print("dumping_phugoid ", dumping_phugoid)


