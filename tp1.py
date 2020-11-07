### AircraftModelling practical works 

endTime = 60 #s
initialState = []
integrationStep = 1 

def derivatives(state, time):
    pass


def integrator_step(state, time, derivatives) :
        k1 = integrationStep*derivatives(state, currentTime)
        k2 = integrationStep*derivatives(r + k1/2.0, currentTime + integrationStep/2.0)
        k3 = integrationStep*derivatives(r + k2/2.0, currentTime + integrationStep/2.0)
        k4 = integrationStep*derivatives(r + k3, currentTime + integrationStep)
        r += (k1 + 2.0*k2 + 2.0*k3 + k4)/6.0 
    return integrationStep


currentTime = 0
state = initialState
if __name__ == "__main__":
    while currentTime < endTime:
        deltaTime, state = integrator_step(state, currentTime, derivatives)
        currentTime += deltaTime