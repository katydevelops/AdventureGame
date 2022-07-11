import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


def valid_input(prompt, choices):
    while True:
        choice = input(prompt).lower()
        if choice in choices:
            return choice
        print_pause(f"Sorry.. your choice {choice} is invalid..")


def start_game():
    locations = ["beach", "jungle", "space"]
    random_location = random.choice(locations)
    if random_location == "beach":
        beach_game()
    if random_location == "jungle":
        jungle_game()
    if random_location == "space":
        space_game()


def beach_game():
    print_pause("\nYou find yourself on a deserted beach. "
                "There is no one around for miles - where is everyone?")
    print_pause("You yell 'HELLO!!' to see if anyone will answer you")
    print_pause("You hear nothing... but all of a sudden.."
                "you hear a creepy voice that says 'OVER HERE!!!'\n")
    response = valid_input("\nEnter 1 to be brave and go towards the voice\n"
                           "Enter 2 to run away and FAST!\n", ["1", "2"])
    if response == "1":
        print_pause("\nYou go towards the voice, "
                    "it seems to be eminating from "
                    "the dark forest trees behind the beach")
        print_pause("You keep looking and yell again ... 'HELLLLO!!'")
        print_pause("All of a sudden, out jumps .. "
                    "a scary troll-like creature!\n")
        response2 = valid_input("Enter 1 to fight the creature\n"
                                "Enter 2 to run away this time!\n", ["1", "2"])
        if response2 == "1":
            print_pause("\nYou fight the creature with your bare hands...")
            print_pause("Unfortunately you are a lover and not a fighter"
                        "and he defeats you .. quickly"
                        "- GAME OVER! \U0001F9CC \n")
        else:
            print_pause("\nYou run swiftly back to the beach .. ")
            print_pause("..however on the way there you fall into a sinkhole "
                        "that you did not notice and you perish"
                        "- GAME OVER! \U0001F573 \n")
    else:
        print_pause("You run FAST away from the sound - you are smart")
        print_pause("While running away, you spot a ship in the distance")
        print_pause("You jump and wave and hope that they see you")
        print_pause("They do see you .. they are friendly pirates "
                    "and they rescue you from the deserted beach")
        print_pause("You live happily ever after "
                    "as a benevolent pirate \U0001F497 \n")
    play_again()


def jungle_game():
    print_pause("You find yourself in a jungle - "
                "it's very beautiful but starting to get dark")
    print_pause("You look around and try to "
                "find shelter as dusk begins to set in")
    print_pause("All of a sudden you hear rustling "
                "in the bushes behind you!")
    response = valid_input("\nQuick! Enter 1 to investigate "
                           "the source of the rustling\n"
                           "Enter 2 to climb the closest "
                           "tree and look out from above \n", ["1", "2"])
    if response == "1":
        print_pause("\nYou are a brave soul .. you move the brush "
                    "to peer forward towards the source of the noise")
        print_pause("You are having trouble seeing .. "
                    "but then all of a sudden you realize it's a TIGER!")
        print_pause("But the tiger actually looks really cute...")
        response2 = valid_input("\nEnter 1 to pet the tiger"
                                "\nEnter 2 to run for your life\n", ["1", "2"])
        if response2 == "1":
            print_pause("\nYou pet the creature with your bare hands...")
            print_pause("The tiger seems unsure of who "
                        "you are and what you're doing..")
            print_pause("All of a sudden - he attacks!"
                        "GAME OVER \U0001F42F \n")
        else:
            print_pause("\nYou run for your life .. you see"
                        "a tiki hut in the jungle and decide to enter.")
            print_pause("Inside are friendly tribal humans who"
                        "lock the door and help save you!! \U0001F947 \n")
    else:
        print_pause("\nYou quickly climb the nearest tree in fear")
        print_pause("You look down below in order to "
                    "see the source of the noise")
        print_pause("you see ..... a mother anteater with "
                    "4 babies walking behind her!")
        print_pause("You climb down from the tree and decide "
                    "to follow them since they're so cute")
        print_pause("They lead you outside the "
                    "jungle to safety!!! \U0001F3C6 \n")
    play_again()


def space_game():
    print_pause("You find yourself in a mysterious space station..")
    print_pause("You are in awe for a while .. but then "
                "you realize you are alone with no food or water..")
    print_pause("You need sustenance quick or you're going to perish!\n")
    response = valid_input("Enter 1 to open round door to your right\n"
                           "Enter 2 to try to radio "
                           "for help on the controls\n", ["1", "2"])
    if response == "1":
        print_pause("\nYou open the round door to your right"
                    ".. it seems safe right?")
        print_pause("You see something moving all of a sudden"
                    "... and it's ... green!!")
        print_pause("Oh my, it's an alien!!\n")
        response2 = valid_input("\nEnter 1 to communicate with the alien "
                                "\nEnter 2 to close the door "
                                "and lock the alien inside\n", ["1", "2"])
        if response2 == "1":
            print_pause("\nYou wave and try to say hi to the alien...")
            print_pause("He smiles at you - "
                        "his smile is unwavering and creepy..")
            print_pause("All of a sudden - he vaporizes you "
                        "with a lazer! GAME OVER \U0001F47D \n")
        else:
            print_pause("\nYou see the alien and immediately close the door")
            print_pause("You feel bad for him but it's for the best")
            print_pause("You throw on a space suit nearby and decide")
            print_pause("to make a run for it using the "
                        "eject button you see on the controls")
            print_pause("Someone should find you out there"
                        ".. right? \U0001F6F8 \n")
    else:
        print_pause("\nYou decide to make a rational "
                    "decision to call for help")
        print_pause("Wow the controls are so confusing though...")
        print_pause("You start pressing all the buttons .. beeboopbee")
        print_pause("All of a sudden you hear a voice come from the speaker")
        print_pause("It's Houston and they are coming "
                    "to save you!! \U0001F680 \n")
    play_again()


def play_again():
    response = valid_input("Play again? Enter yes or no"
                           " \U0001F921 \n", ["yes", "no"]).lower()
    if response == "yes":
        start_game()
    else:
        print_pause("Thanks for playing - bye now!!\n")
        exit(0)


start_game()
