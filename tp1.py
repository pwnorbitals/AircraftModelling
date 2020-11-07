### AircraftModelling practical works 

endTime = 60 #s





def integrator() :
    return 1


currentTime = 0
state = []
if __name__ == "__main__":
    while currentTime < endTime:
        # Compute state derivatives
        derivatives = []

        # Integrate state
        currentTime += integrator(state, derivatives)
