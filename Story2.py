from Getters import *

def Story2(debug = False):
    if debug: print("Story2 Function")

    print("\n")
    friendName1 = getWord("Enter a name: ", debug)
    vehicle1 = getVehicle("Enter a vehicle: ", debug)
    object1 = getWord("Enter a object: ", debug)
    vehicle2 = getWord("Enter a vehicle: ", debug)
    time1 = getWord("Enter a time: ", debug)
    buidling1 = getWord("Enter a building: ", debug)
    
    
    out = "\n"
    out += " One day me and my friend " + friendName1
    out += " were out driving his " + vehicle1
    out += " He wasn't paying attention and crashed into a " + object1
    out += " then we called the E.M.T and when they got there they loaded us into a " + vehicle2
    out += " It took " + time1
    out += " for the E.M.T's to arrive at " + building1
    
    return out
