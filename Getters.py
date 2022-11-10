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
        elif (option == "2" or 
            option == "two" or 
            option == "story 2" or
            option == "story2"):
                option = "2"
                goodInput = True
        elif (option == "3" or 
            option == "three" or 
            option == "story 3" or
            option == "story3"):
                option = "3"
                goodInput = True
        elif (option == "4" or 
            option == "four" or 
            option == "story 4" or
            option == "story4"):
                option = "4"
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

def getcarCompany(prompt, debug = False):
    if debug: print("getcarCompany Function")
    
    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("UNACCEPTABLE")
        
    return word
    
def getcarCompany(prompt, debug = False):
    if debug: print("getcarCompany Function")
    
    goodInput = False
    
    carCompany =  ["car", 
						"tesla", 
						"bmw", 
						"ferrari", 
						"ford", 
						"porsche", 
						"honda", 
						"lamborghini", 
						"toyota", 
						"bentley", 
						"maserati", 
						"audi", 
						"jeep", 
						"subaru", 
						"cadillac", 
						"chrysler", 
						"chevorlet corvette",
						"dodge",
						"hyundai",
						"jaguar",
						"mazda",
						"scion",
						"nissan",
						"bugatti",
						"buick",
						"lexus",
						"rolls-royce",
						"acura",
						"aston martin",
						"chevrolet",
						"kia",
						"mercedes-benz",
						"volkswagon",
						"volvo",
						"mclaren",
						"mitsubishi",
						"gmc",
						"buick",
						"lexus",
						"rolls-royce",
						"acura",
						"aston martin",
						"chevrolet",
						"kia",
						"mercedes-benz",
						"volkswagon",
						"volvo",
						"mclaren",
						"mitsubishi",
						"gmc",
						"infiniti",
						"lincoln",
						"gm",
						"pontiac",
						"genesis",
						"suzuki",
						"lotus",
						"koenigsegg",
						"pagani",
						"hummer",
						"ram",
						"mg",
						]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("UNACCEPTABLE")
        elif word.lower() not in carCompany:
            goodInput = False
            print ("INVALID")
        
    return word
    
def isSwear(word, debug = False):
    if debug: print("isSwear Function")
    if word.lower() in swearList:
        return True
    else:
        return False


def getNumber(prompt, debug = False):
    if debug: print("getNumber Function")
    
    goodInput = False
    
    numbers = ["69"
              ]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("UNACCEPTABLE")
        elif word.lower() not in numbers:
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
             "daddy",
]
