from Getters import *

def Story2(debug = False):
    if debug: print("Story2 Function")

    print("\n")
    friendName1 = getWord("Enter a name: ", debug)
    carCompany1 = getcarCompany("Enter a carCompany: ", debug)
    object1 = getWord("Enter a object: ", debug)
    thing1 = getWord("Enter a thing: ", debug)
    time1 = getWord("Enter a amount of minutes: ", debug)
    building1 = getWord("Enter a building: ", debug)
    injury1 = getWord("Enter a injury: ", debug)
    
    
    out = "\n"
    out += " One day me and my friend " + friendName1
    out += " were out driving his " + carCompany1
    out += " \n He wasn't paying attention and crashed into a " + object1
    out += " then we called the E.M.T's and when they got there \n they loaded us into a " + thing1
    out += " \n It took " + time1
    out += " minutes for the E.M.T's to arrive at the " + building1
    out += " \n After the arriving "
    out += " the doctors diagnosed us with a " + injury1
    out += " You should try Story 4!"
    
    return out
