import random
import time
import sys
from random import randint

#player class
#weapon class
#possible location class
#functions for each part of the story

#answer validation
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "C"]


#validation to ensure user enters valid answer
required = ("\nUse only the valid keys\n")

class player():
    def __init__(self):
        self.name = "" #allows user to enter their own name and weapon
        self.weapon = ""
        self.health = 1
        self.max_health = 1
        self.inventory = []
    def attack(self, enemy):
        damage = min(
            max(randint(0, self.health) - randint(0, enemy.health), 0),
            enemy.health)
        enemy.health = enemy.health - damage

#two types of enemy

class enemy1():
    def __init__(self):
        self.health = 2
        if self.health == 0:
            print("The alien drops down to the floor dead")

class enemy2():
    def __init__(self):
        self.health = 5
        
p = player()#used to reference the player class     
e = enemy1()
#name choice        
def chooseName():
    

    #name choice
    nameEntered = False
    while nameEntered == False:
        p.name = input("Please enter a name")
        if len(p.name) > 0:
            nameEntered = True
            print("Hello", p.name)
        
    
   
    chooseWeapon()


#weapon choice
def chooseWeapon():
    print("Choose your weapon:'\n'"
      "A: Pistol '\n'"
      "B: Knife")
    #p.weapon = input()
    #weapon = input()
    choice = input(">>> ") #Assigns the choice variable to mean the user input
    if choice in answer_A: #uses the user validation
        p.weapon = "Pistol" #sets the weapon of the player 
        print("You have chosen the Pistol")
        
        
    elif choice in answer_B:
        p.weapon = "Knife"
        print("You have chosen the Knife")
        
        
    else:
        print(required)
        chooseWeapon()

            
    intro() #continues to next part of the game

#intro function to set the scene        
def intro():
    print(p.name, "you have found yourself trapped on a strange ship with no"
          " recollection of what happened. All you have is a", p.weapon,
          " You must find a way out, try and find some clues")
    carryOn()


def carryOn():
    
    
        
    print("You come across a scrap of paper, you begin to read it")
    
    print("The note is addressed to you and states that the mission went wrong"
              " you went to invesitgate a rogue ship which was believed to contain"
              " alien lifeforms. The note then carries on to say if you are reading"
              " this then the writer is dead. It says that you must finish the mission"
              " and get out alive")
    time.sleep(1)
    
    
        
    print("You take the note and must choose to believe it. Suddenly you see"
          " a flashing figure ahead of you."
          "Do you: '\n'"
          "A: Move forward '\n'"
          "B: Shout out")
    choice = input(">>> ")
    if choice in answer_A:
        moveForward()
        
    elif choice in answer_B:
        shoutOut()
    else:
        print(required)
        carryOn()

        


def moveForward():
    
    print("As you approach the figure you soon realise that is unlike anything you have seen before."
          " You see the face of something that is dead inside,"
          " the body of something truly disturbing."
          " As you stop to take in the gruesome nature of what you're seeing,"
          " the creature screams out and begins to charge at you")
    print("What do you do: '\n'"
          "A: Use your weapon '\n'"
          "B: Attempt to communicate '\n'"
          "C: Run away")
    choice = input(">>> ")
    if choice in answer_A:
        print("You use your", p.weapon)
        useWeapon()
        print("The creature is angered by this and it gains on you")
        runAway()
        
    elif choice in answer_B:
        shoutOut()
        
    elif choice in answer_C:
        runAway()
        
    else:
        print(required)
        moveForward()

        

        


def shoutOut():
    print("You shout at the figure, demanding to know what is happening,"
          " the figure responds with a loud and disturbing scream."
          " Quickly, it begins to move closer to you, with each metre closer"
          " you can sense that it is hostile"
          " Do you: '\n'"
          " A: Use your weapon '\n'"
          " B: Run away")
    choice = input(">>> ")
    if choice in answer_A:
        print("You use your", p.weapon)
        useWeapon()
        print("The creature is angered by this and it gains on you")
        runAway()
    elif choice in answer_B:
        runAway()
    else:
        print(required)
        shoutOut()

        
def useWeapon():
    if p.weapon == "Pistol":
        print("You fire at the alien delivering damage, it screams in pain")
        e.health -= 1
        if e.health == 0:
            print("The enemy dies")
        #use attack function from player class
    elif p.weapon == "Knife":
        p.weapon = ""
        print("You wait until the enemy is within range and you attempt to stab...")
        print("The figure suddenly swipes for your knife and crushes it instantly")
        dead()
    
    
              
def runAway():
    print("You start to run as fast as you can, with the thing close behind you,"
          " you come across a door, you must act fast, do you: '\n'"
          " A: Kick it down '\n'"
          " B: Keep running")
    choice = input(">>> ")
    if choice in answer_A:
        print("You kick the door down and continue running")
        nextRoom()
    elif choice in answer_B:
        print(" You come across a dead end and the figures surround you, you try and fight your way out"
              " but to no avail")
        dead()
    else:
        print(required)
        runAway()

        
def nextRoom():
    print("As you keep running, you realise that the creature is no longer behind you."
          " You find yourself facing another room, with no choice but to carry on."
          " Entering the room, you find more dead bodies on the floor, suddenly the"
          " memories come flooding back, these men were your friends. Whatever killed them"
          " certainly wasn't human. Looking around you see strange writings on the wall"
          " and a flashing computer screen")
    print("Do you: '\n'"
          " A: Look at screen '\n'"
          " B: Attempt to read the wall")
    choice = input(">>> ")
    if choice in answer_A:
        readScreen()
    elif choice in answer_B:
        print("As you attempt to read the writings you realise that whoever was writing them stopped"
              " stopped abruptly. You soon realise that it must have been your collegues. The writing"
              " says: WE ARE WEAK, WE NEED URGENT HELP, THEY WANT TO KI- then it ends."
              " Quickly, you go the computer screen to investigate further")
        readScreen()
    else:
        print(required)
        nextRoom()


def readScreen():
    print("While reading the screen, you find a diary entry from a collegue. It states that after"
          " an intense investigation, they found the alien lifeforms to be extremely powerful and"
          " intelligent. All they want is to survive after thousands of years of suffering. "
          " They survive by feeding off humans. This entry is followed by a video log which"
          " shows a collegue acting very disturbingly, they are shouting at the camera, showing"
          " a deranged state of mind. You hear some brief words: 'Bomb, detonate, kill them all"
          " Suddenly the video is cut off by a bellowing scream. "
          " After watching this, do you: '\n'"
          " A: Keep moving while attempting to find an escape '\n':"
          " B: Turn back and attempt to fight the alien and avenge your friends")
    choice = input(">>> ")
    if choice in answer_A:
        escapeAttempt()
    elif choice in answer_B:
        attackAlien()
    else:
        print(required)
        readScreen()

def attackAlien():
    print("Filled with rage and revenge, you let out a war cry to get the attention of the aliens."
          "You hear a scream which mirrors yours. Footsteps echoe through the room, they are near."
          "Suddenly, a figure bursts through the door and charges at you, you must attack")
    useWeapon()
    print("The creature lets out another scream, but keeps going, it then attempts to swing at you"
          " Do you '\n'"
          " A: Use your weapon again '\n'"
          " B: Dodge the attack '\n'"
          " C: Run out of the room")
    choice = input(">>> ")
    if choice in answer_A:
        useWeapon()
        print("Thats one down you think to yourself. You decide to keep moving through the ship."
              " Maybe you can find the bomb")
        continueRoom()
    elif choice in answer_B:
        print("You attempt to dodge, but the alien grabs you with its other hand and crushes you")
        dead()
    elif choice in answer_C:
        dead()
    else:
        print(required)
        attackAlien()
        
def continueRoom():
    print("As you move into the next room, you hear more screams bounce around the ship, how many"
          " more of them? Suddenly you are faced with another alien who just stands and watches you"
          " Do you: '\n'"
          " A: Attack it '\n'"
          " B: Keep moving")
    choice = input(">>> ")

    if choice in answer_A:
        useWeapon();
        print("The alien does not react. Still filled with rage, you shoot it again")
        useWeapon()
        print("The aliens begin to surround you")
        aliensCommunicate()
    elif choice in answer_B:
        print("As you continue to move, you come up to a turning. The aliens begin to surround"
              " you, but they are only walking and no longer screaming, their faces are empty."
              " All of their mouths open and they begin to communicate")
        aliensCommunicate()
    else:
        print(required)
        nextRoom()


def aliensCommunicate():
    print(" You are motionless, the aliens all speak at the same time in a human like manner but"
          " without emotion. 'All your fellow humans are dead, you will be next, we are back from"
          "our years of enslavement at the hands of your race. You will kill no more of us and"
          " you will see our true power!' The voice became more menacing: 'WE ARE BECOMING STRONGER AGAIN"
          " AND YOU WILL FACE OUR WRATH HUMAN. Conform or be killed!'")
    print(" You say to them: '\n'"
          " A: 'We were only here to investigate, you cannot kill us for what our past generations have done.'\n'"
          " B: 'You killed my friends and attacked me, i'm not conforming!' '\n'"
          " C: You see the detonate button on the wall and make a dash for that")
    choice = input(">>> ")
    if choice in answer_A:
        print("The aliens respond: 'We have seen how you treat other races as slaves, you do not learn"
              " you will be killed'. They all rush at you")
        dead()
    elif choice in answer_B:
        print("They reply: 'That is an unintelligent choice'. They attack you, you attack as many as you can but"
              " you cannot stop them")
        dead()
    elif choice in answer_C:
        detonate()
    else:
        print(required)
        aliensCommunicate()


def detonate():
    print("As you charge towards the button you are hit by a flailing arm of an alien, you shoot at them in reply")
    useWeapon()
    print("As you come up to the button, you see that the escape pod is too far away and you can't make it"
          " You realise that to avenge your friends and save the human race you must sacrafice yourself and the investigation dies with you."
          " You make one final glance at the aliens that are coming towards you, they have fear and sadness in their eyes now."
          " You must make this sacrafice. While looking, you see an escape pod with the detonate button just outside it."
          " You could save yourself and all this would not be for nothing. Do you '\n':"
          " A: Run to the escape pod '\n'"
          " B: Press the detonate button now")
    choice = input(">>> ")
    if choice in answer_A:
        print("You attempt to sprint towards the escape pod but quickly you see an alien come towards you from that side."
              " It attacks you and throws you to the ground. As you lie there, you realise you have failed, your vision soon"
              " becomes ruined and you close your eyes to meet the darkness")
        dead()
    elif choice in answer_B:
        print("Without risking falure, you slam the detonate button with all your power. The aliens begin to realise whar you have done"
              " and start to scream in agony and despair. 'WHAT HAVE YOU DONE' they bellow. You are destroying the last of an ancient race"
              " to save your own race, this thought stays with you as the ship erupts into flames and you embrace the victory")
        time.sleep(1)
        print("You close your eyes and then nothing...")
    else:
        print(required)
        detonate()

    

    
          

    

def escapeAttempt():
    print("You leave the room, attempting to find any means of escape. Suddenly, an ear piercing screech echoes"
          " around the ship, they are close. You muzt escape. Getting your weapon ready just in case, you"
          " see more bodies, sadness and pain fill your head. Escape, escape, escape. The screams increase in decibels,"
          " they are closer. You come up to a turning. Do you '\n':"
          " A: Turn left '\n'"
          " B: Turn right")
    choice = input(">>> ")
    if choice in answer_A:
        print("An alien is there as you turn, without hesitating you are killed")
        dead()
    elif choice in answer_B:
        print("Ahead of you is filled with an eerie emptyness. You keep running, finding escape pods either side of you."
              " Without thinking twice, you jump in the nearest one. As you strap yourself in, you exhale deeply, are "
              " you free yet? What of the mission? You have the notes of your collegues so atleast you will be able to report"
              " back. Scanning the escape pod, you see a button with the word 'DETONATE' sprayed onto it."
              " Suddenly your heart sinks, is this the bomb that was mentioned on the video clip. Do you: '\n'"
              " A: Destroy the ship and the rest of this alien species '\n"
              " B: Spare them and just ensure that you live")
        choice = input(">>> ")
        if choice in answer_A:
            detonateBomb()
        elif choice in answer_B:
            escape()
        else:
            print(required)
            escapeAttempt()

    


def detonateBomb():
    print("As you eject the pod, you are quickly thrown back by one of the aliens. This shakes the entire pod, "
          " but you rapidly move your finger onto the detonate button, you look at the alien that is shaking the pod,"
          " breathe deeply and slam the button down. As you steer the pod away you are hit by the desperate arm of"
          " the alien who screams in pain, before erupting into flames. The screams continue as you are flung into"
          " space. Looking back, you see the ship engulfed in flames, the last of a species dead.")
    time.sleep(3)
    print("As you fall through space, you continue to fly towards the surface of what is left of Earth."
          "When you land, you exit the pod and ponder the thought of finishing an entire species. They would have done the"
          " same, or would they, given the choice? Was it your right to play god? You fall to your knees, having lost everything but your life.")
    
        

def escape():
    print("You desperately slam the escape button down, suddenly you are flung away from the ship and into empty space."
          "But, as you look back you see the twisted faces of the aliens, they appear to be laughing at you, but why?"
          " When suddenly you realise in horror that they now have control of the spacecraft. This dark thought escalates as"
          " you had the option to destroy them, but could not bring yourself to finish off an entire species."
          " Will the aliens share this mercy as they set their course for Earth.")
          
    





    
def dead():
    print("Sadly you are dead, please pick an option: '\n'"
          " A: Play again '\n'"
          " B: Quit game")
    choice = input(">>> ")
    if choice in answer_A:
        chooseName()
    elif choice in answer_B:
        quit()


        
chooseName()#begins the game
