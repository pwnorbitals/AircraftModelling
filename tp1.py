### AircraftModelling practical works 

endTime = 60 #s
initialState = []
integrationStep = 1 

def derivatives(state, time):
    pass


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
    while currentTime < endTime:
        deltaTime, state = integrator_step(state, currentTime, derivatives)
        currentTime += deltaTime