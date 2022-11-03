from Getters import *

def Story3(debug = False):
    if debug: print("Story3 Function")

    print("\n")
    friendName1 = getWord("Enter a name: ", debug)
    clothingstore1 = getWord("Enter a clothing store: ", debug)
    thing1 = getWord("Enter a thing: ", debug)
    place1 = getWord("Enter a place: ",debug)
    
    
    out = "\n"
    out += " Once upon a time my friend " + friendName1
    out += " and I went to " + clothingstore1
    out += " \n and to our suprise there was " + thing1
    out += " We bought it and took it to the " + place1
    out += " and we used our new " +thing1
    
    return out
