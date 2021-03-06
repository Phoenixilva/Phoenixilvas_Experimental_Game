# Phoenixilva's Experimental Nethack Style Game
# v0.1.0-DEV
# Created by Phoenixilva (Shay Rossignol)
# All code is free to change and distribute

def doors(door):
    if door == "1":
        print "There's a giant bear here eating a cheese cake. What do you do?"
        print "1. Take the cake."
        print "2. Scream at the bear."
        print "3. Stab the bear"

        bear = raw_input('> ')

        if bear == "1":
            print "The bear eats your face off. Good job!"
            return quit_or_restart()
        elif bear == "2":
            print "The bear eats your legs off. Good job!"
            return quit_or_restart()
        elif bear == "3":
            print "The bear dodges your stab! What do you do?"
            print "1. Stab again"
            print "2. Duck and cover!"
            print "3. Run away"

            fight = raw_input('> ')

            if fight == "1":
                print "The bear eats your arms off. Good job!"
                return quit_or_restart()
            elif fight == "2":
                print "The bear swings at you and misses!"
                return bear_misses()
            elif fight == "3":
                print "The bear runs you down and eats your head off. Good Job!"
                return quit_or_restart()
            else:
                return indecision_kills()
        else:
            return indecision_kills()

    elif door == "2":
        print "You stare into the endless abyss at Cthulhu's retina."
        print "1. Blueberries."
        print "2. Yellow jacket clothespins."
        print "3. Understanding revolvers yelling melodies."

        insanity = raw_input('> ')

        if insanity == "1" or insanity == "2":
            print "Your body survives powered by a mind of jello. Good job!"
            return quit_or_restart()
        else:
            print "The insanity rots your eyes into a pool of muck. Good job!"
            return quit_or_restart()

    else:
        return indecision_kills()

def bear_misses():
    print "The bear missed! What do you do?"
    print "1. Stab it in the throat"
    print "2. Kick it in the nads"
    print "3. Run away"

    bear_fight = raw_input('> ')

    if bear_fight == "1":
        print "Congrats! You killed the bear!"
        return killed_bear()
    elif bear_fight == "2":
        print "The bear looks at you quizzically, then rips your head off. Good job!"
        return quit_or_restart()
    elif bear_fight == "3":
        print "The bear runs you down and eats your head off. Good job!"
        return quit_or_restart()
    else:
        return indecision_kills()

def killed_bear():
    print "You killed the bear. You notice a door on the other side. Do you:"
    print "1. Go through the door?"
    print "2. Turn around and go through door #2?"

    which_way = raw_input('> ')

    if which_way == "1":
        print "You went through the door. You see a chest on the floor and another door. Do you:"
        print "1. Open the chest?"
        print "2. Go through the door?"
        print "3. Turn around and go through door #2?"

        what_now = raw_input('> ')

        if what_now == "1":
            print "A monster bites off your face. Good job!"
            return quit_or_restart()
        elif what_now == "2":
            print "You went through the door."
        elif what_now == "3":
            return doors('2')
        else:
            return indecision_kills()

    elif which_way == "2":
        return doors('2')
    else:
        return indecision_kills()

def indecision_kills():
    print "You stumble around and fall on a knife and die. Good job!"
    return quit_or_restart()
     
def start_game():
    print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

    whichdoor = raw_input('> ')

    doors(whichdoor)

def quit_or_restart():
    print "Do you want to:"
    print "1. Quit"
    print "2. Restart"

    quit_or_restart = raw_input('> ')

    if quit_or_restart == "1":
        quit()
    elif quit_or_restart == "2":
        start_game()
    else:
        quit() 

start_game()

quit_or_restart()
