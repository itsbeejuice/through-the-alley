print("welcome to this game I made^^")
print("Here are the rules")
a=input("1. please be respectful to the game\n 2. please only use the options provided \n3. please contact the op if you have any questions of concerns \nThis is a Y/N type game so vibe with that\n ~Press enter to continue")
       #tfw you are op and you're not making this to really show anyone *drops mic like a boss*
start=input("Are you ready to start? Y/N ")
if start.lower()== "n":
    print("gg bro, come back later")

elif start.lower()=="y":
    print("welcome to the game.")
    b=input ("You find yourself in a dark alleyway walking home from the club")
    #if something goes wrong check here
    c=input ("You suddenly hear footsteps behind you.")
    d=input ("What do you wanna do?")
    print("~Look behind you?")
    print("~Run away") #fucking wimp
    e=input ("Make your move: ")
    if e.lower()== "look behind you?":
        print('Why would you do that? Do you lack common sense?')
        print('You have died')
        print("they fucking killed you")
    elif e.lower()=="run away":
        print ("you run away and pass an open building but nowhere else to run")
        print ("what do you want to do?")
        print ("~Go inside")
        print ("~Keep running [maybe we'll find a way out]")
        f=input ("choose now: ")
        if f.lower()=="keep running":
            print("I told you There's nowhere to run. Do you even listen to me? You do realize I have feelings too? What, You thought I was fake? You don't think I'm actively narrating YOUR life? I have a wife and kids buster, I could be at home with them right now. I don't want to be in this situation any more than you d-")
            g=input ("Sorry, I lost my cool there where were we?")
            print ("Ah yes, you kept running")
            print ("You suddenly hear an explosion, you just narrowly escaped death")
            print ("Your followers were not as lucky and burned in the building while they were looking for you. You are safe now and can return home")
        elif f.lower()== "go inside":
            print("You hear a ticking sound coming from the wall")
            print("~investigate it?")
            print("~leave it alone")
            h= input("What do you wanna do?")
            if h.lower()=="investigate it":
                    print("it was a bomb bro-")
                    print("you died")
            elif h.lower()== "leave it alone":
                    print("it was a bomb bro-")
                    print("you didn't get out in time")
                    print("you died")
        else:
            print ("please choose between the options go inside and keep running")
            #get back to f from here
    else:
        print("please choose the options only")
else:
    print("please come back when you are ready")
            
    
