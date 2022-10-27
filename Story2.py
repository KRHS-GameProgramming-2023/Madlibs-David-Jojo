from Getters import *

def Story2(debug = False):
    if debug: print("Story2 Function")

    print("\n")
    friendName1 = getWord("Enter a name: ", debug)
    vehicle1 = getVehicle("Enter a vehicle: ", debug)
    object1 = getWord("Enter a object: ", debug)
    
    out = "\n"
    out += " One day me and my friend " + friendName1
    out += " were out driving his " + vehicle1
    out += " He wasn't paying attention and crashed into a " + object1
    
    
    return out
