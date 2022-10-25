def getMenuOption(debug = False):
    if debug: print("getMenuOption Function")
    
    goodInput = False
    
    while not goodInput:
        option = input("Please select an option: ")
        option = option.lower()
        
        if (option == "q" or 
            option == "quit" or 
            option == "x" or
            option == "exit"):
                option = "q"
                goodInput = True
        elif (option == "1" or 
            option == "one" or 
            option == "story 1" or
            option == "story1"):
                option = "1"
                goodInput = True        
                
            
        else:
            print("Please make a valid choice")
        
    return option

def getWord(prompt, debug = False):
    if debug: print("getWord Function")
    
    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("UNACCEPTABLE")
        
    return word
    
def getSport(prompt, debug = False):
    if debug: print("getSport Function")
    
    goodInput = False
    
    sports = ["soccer", 
              "football",
              "hockey",
              "wrestling",
              "lacrosse",
              "baseball",
              "softball",
              "track and field",
              "volleyball",
              "skiing",
              "snowboarding",
              "surfing",
              "throwing stuff",
              "halo",
              "sleding",
              "hiking",
              "catch",
              "video game",
              "video games",
              "throwing",
              "chess",
              "kickball",
              "checkers",
              "bass fishing",
              ]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("UNACCEPTABLE")
        elif word.lower() not in sports:
            goodInput = False
            print ("INVALID")
        
    return word
    
def isSwear(word, debug = False):
    if debug: print("isSwear Function")
    if word.lower() in swearList:
        return True
    else:
        return False

swearList = ["poop",
             "pee",
             "shit",
             "fuck",
             "ass",
             "motherfucker",
             "fucker",
             "dick",
             "asshole",
             "dipstick",
             "retard",
             "idiot",
             "cunt",
             "dickhead",
             "fucking",
             "nigger",
             "pussy",
             "penis",
             "vagina",
             "boobs",
             "boob",
             "breast",
             "breasts",
             "sex",
             "fucked",
             "bitch",
]
