from Getters import *

def Story2(debug = False):
    if debug: print("Story2 Function")

    print("\n")
    friendName1 = getWord("Enter a name:",debug)
    car1 = getCar("Enter a vechile :",debug)
    thingstohit = getHit("Enter something you can hit with your car")
    
    out = "\n"
    out+= "One day me and my friend " + friendName1
    out += " were out driving his " + car1
    out += "He wasn't paying attention and crashed into a" + thingstohit
    
    
    return out
