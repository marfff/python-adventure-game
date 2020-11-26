import time
# time module
import random
# random module

fruit = ["apple", "elderberry", "orange"]
items = []


def print_wait(words):
    # printing at 2 second intervals
    print(words)
    time.sleep(2)


def intro():
    # introduction starting text
    print_wait("You are needing 5 a day of FRUIT")
    print_wait("Moving forward you notice some rooms")
    print_wait("What a choice you have to make!")
    items.clear()


def restart():
    # player ability to replay

    key = input("Hit 'y' if you want to play again? ").lower()
    if key == "y":
        intro()
    else:
        print_wait("Bye for now")
        exit()


def room_choice():
    # Player choice of room
    while True:
        print_wait("There are two rooms red and blue")
        room_ch = input("Which colour room do you want to enter? ").lower()
        if "red" in room_ch:
            print_wait("You picked red")
            red_room()
        elif "blue" in room_ch:
            print_wait("You picked blue")
            blue_room()
        else:
            print_wait("I don't understand")
    return room_choice


def red_room():
    # red room decisions
    if "vitamix" in items:
        print_wait("You now have a Vitamix")
        print_wait("You can use the Vitamix to get rid of all the fruit")

    elif "spoon" in items:
        print_wait("You carefully look around the red room")
        print_wait("What do you see?")
        print_wait("A Vitamix...")
        fruit_type = random.choice(fruit)
        print_wait("A Vitamix hidden behind an " + fruit_type)
        print_wait("You eat the fruit with your spoon")
        print_wait("Yum! Yum!\nYou take the Vitamix")
        items.append("vitamix")

    else:
        print_wait("You carefully look around the red room")
        print_wait("What do you see?")
        print_wait("A Vitamix...")
        fruit_type = random.choice(fruit)
        print_wait("A Vitamix hidden behind an " + fruit_type)
        print_wait("You need a spoon to eat the fruit")
        print_wait("You'll need to find a spoon")


def blue_room():
    # blue room decisions
    print_wait("You carefully look around the blue room")
    print_wait("What do you see?")
    print_wait("Some spoons...")
    fruit_type = random.choice(fruit)
    print_wait("Some spoons and a pile of " + fruit_type + "s")
    if "vitamix" in items:
        print_wait("You have a Vitamix so you pulverise the fruit ...")
        print_wait("...thinking I NEVER HAVE TO EAT FRUIT AGAIN!")
        print_wait("")
        print_wait("                  YOU WON")
        print_wait("")

        restart()

    elif "spoon" in items:
        print_wait("You already have a spoon and leave the room")
    else:
        items.append("spoon")
        print_wait("You take a spoon and leave the room")

        if "vitamix" in items:
            print_wait("you used the vitamix to get rid of all the fruit")
            print_wait("you never need to eat fruit again")


intro()
room_choice()
red_room(items)
blue_room(items)
