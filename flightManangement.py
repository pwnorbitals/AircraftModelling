
from z_feedback import sys as autopilot
import control
import matplotlib.pyplot as plt
import numpy as np

tstep = 0.001  # time resolution
second = round(1/tstep)

t = np.arange(0, (15+200+200+120+30+15), tstep)

terrain_ft = 197  # LFMY, Salon de Provence !
cruise_1_ft = 15000
cruise_2_ft = 35000
approach_ft = 7000
final_ft = 700

flightPlan = \
    [terrain_ft] * (15 * second)\
    + [cruise_1_ft] * (200 * second)\
    + [cruise_2_ft] * (200 * second)\
    + [approach_ft] * (120 * second)\
    + [final_ft] * (30 * second)\
    + [terrain_ft] * (15 * second)

tout, yout, xout = control.forced_response(autopilot, t, flightPlan)
plt.plot(tout, yout)
plt.show()