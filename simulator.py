### AircraftModelling practical works 


import csv
import numpy as np
from StateSpaceModel import Xv, Xgamma, Xalpha, Zv, Zalpha, malpha, mq, Zdelta_m as Zdeltam, mdelta_m as mdeltam
from Tp1_study import V_eq as Veq, delta_m_0 as deltam0
import os
import sys

endTime = 60 #s
integrationStep = 0.01 #s
stateNames = ["V", "gamma", "alpha", "q", "theta", "z"]
initialState = np.c_[[0., 0., 0., 0., 0., 0.]]
doCSV = True
doStdout = False





def derivatives(state, time):
    
    # Slide 69
    A = np.array([
        [-Xv, -Xgamma, -Xalpha, 0, 0, 0],
        [Zv, 0, Zalpha, 0, 0, 0],
        [-Zv, 0, -Zalpha, 1, 0, 0],
        [0, 0, malpha, mq, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, Veq, 0, 0, 0, 0]
    ])
    B = np.c_[[0, Zdeltam, -Zdeltam, mdeltam, 0, 0]]
    
    # output is full state vector
    C = np.eye(6)
    D = np.zeros((6,1))

    input = np.c_[[deltam0]]
    stateDerivatives = np.dot(A,state) + np.dot(B,input)
    output           = np.dot(C,state) + np.dot(D,input)

    


    return stateDerivatives





def integrator_step(state, time, derivatives) :
    k1 = integrationStep*derivatives(state, currentTime)
    k2 = integrationStep*derivatives(state + k1/2.0, currentTime + integrationStep/2.0)
    k3 = integrationStep*derivatives(state + k2/2.0, currentTime + integrationStep/2.0)
    k4 = integrationStep*derivatives(state + k3, currentTime + integrationStep)
    state += (k1 + 2.0*k2 + 2.0*k3 + k4)/6.0 
    return integrationStep, state






currentTime = 0
state = initialState    









if __name__ == "__main__":
    with open(os.path.join(sys.path[0], 'sim_out.csv'), 'w') as csvfile:
        
        # Writer init
        if doCSV :
            writer = csv.writer(csvfile)
            writer.writerow(["Time", *stateNames])
            writer.writerow([currentTime, *state.flatten()])

        if doStdout :
            print(*stateNames)
            print(*state.flatten())

        
        # Main loop
        while currentTime < endTime:
            
            # Time step
            deltaTime, state = integrator_step(state, currentTime, derivatives)
            assert(not np.isnan(state).any())
            currentTime += deltaTime


            # Writer update
            if doCSV :
                writer.writerow([currentTime, *state.flatten()])  

            if doStdout :
                print(*state.flatten())

            
