from Getters import *

def Story3(debug = False):
    if debug: print("Story3 Function")

    print("\n")
    friendName1 = getWord("Enter a name: ", debug)
    clothingstore1 = getWord("Enter a clothesstore: ", debug)
    thing1 = getWord("Enter a thing: ", debug)
    
    
    out = "\n"
    out += " Once upon a time my friend " + friendName1
    out += " and I went to " + clothingstore1
    out += " \n To our suprise there was " + thing1
    
    return out
