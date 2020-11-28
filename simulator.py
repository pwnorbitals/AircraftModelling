### AircraftModelling practical works 


import csv
import numpy as np

endTime = 60 #s
integrationStep = 0.01 #s
stateNames = ["V", "gamma", "alpha", "q", "theta", "z"]
initialState = np.array([0., 0., 0., 0., 0., 0.]).T





def derivatives(state, time):

    V, gamma, alpha, q, theta, z = state
    
    # Slide 69
    A = np.array([
        [-Xv, -Xgamma, -Xalpha, 0, 0, 0],
        [Zv, 0, Za, 0, 0, 0],
        [-Zv, 0, -Zalpha, 1, 0, 0],
        [0, 0, malpha, mq, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, Veq, 0, 0, 0, 0]
    ])
    B = np.array([0, Zdeltam, -Zdeltam, mdeltam, 0, 0]).T
    # Yoann : C is eye(6*6), D is zeros

    input = np.array([deltam])
    stateDerivatives = A*state + B*input
    output           = C*state + D*input

    


    return np.array([1/(time**2 + 1)])





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
    with open('sim_out.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Time", *stateNames])
        writer.writerow([currentTime, *state])
        while currentTime < endTime:
            deltaTime, state = integrator_step(state, currentTime, derivatives)
            currentTime += deltaTime
            writer.writerow([currentTime, *state])