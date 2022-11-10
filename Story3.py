from Getters import *

def Story3(debug = False):
    if debug: print("Story3 Function")

    print("\n")
    friendName1 = getWord("Enter a name: ", debug)
    clothingstore1 = getWord("Enter a clothing store: ", debug)
    thing1 = getWord("Enter a thing: ", debug)
    place1 = getWord("Enter a place: ", debug)
    clothing1 = getWord("Enter a clothing: ", debug)
    
    print("\n\n")
    print('''
             __________________________________________________________________________
    |: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : |
    | : : : : : : : : : : : : : : : :_________________________: : : : : : : : :|
    |: : : : : : : : : : : : : : : _)                         (_ : : : : : : : |
    | : : : : : : : : : : : : : : )_ :  Club 40 Gift Shoppe :  _( : : : : : : :|
    |: : Elevator  : : : :__________)_________________________(__________  : : |
    | _____________ : _ :/ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ\: _ :|
    ||  _________  | /_\ '.Z.'.Z.'.Z.'.Z.'.Z.'.Z.'.Z.'.Z.'.Z.'.Z.'.Z.'.Z.' /_\ |
    || |    |    | |:=|=: |Flowers * Perfumes_________Lingerie * Candles| :=|=:|
    || |    |    | | : : :|   ______    _  .'         '.  _    ______   |: : : |
    || |    |    | |======| .' ,|,  '. /_\ |           | /_\ .'  ,|, '. |======|
    || |    |    |:|Lounge| | ;;;;;  | =|= |           | =|= |  ;;;;; | |Casino|
    || |    |    | |<---  | |_';;;'_n|     |  n______  |     |$_';;;'_| |  --->|
    || |    |    | |      | |_|-;-|__|     |-|_______|-|     |__|-;-|_| |      |
    || |    |    | |      | |________|     |           |     |________| |      |
    || |    |    | |      |                |           |                |      |
    lc_|____|____|_|______|________________|           |________________|______|
     ''')


    print("\n\n")
    
    
    out = "\n"
    out += " Once upon a time my friend " + friendName1
    out += " and I went to " + clothingstore1
    out += " \n and to our suprise there was " + thing1
    out += " We bought it and took it to the " + place1
    out += " and we used our new " + clothing1
    out += " \n which started a new fashion trend " 
    out += " You should try Story 4!"
    
    return out
