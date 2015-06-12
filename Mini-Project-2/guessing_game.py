# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

lives = 0

hi_range = 100

secret_number = 0
user_guess = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here

    global secret_number 
    global hi_range
    global lives
    
    secret_number = random.randrange(0, hi_range)
    lives = math.ceil(math.log(hi_range, 2))
    chance.set_text("Remaining chance " + str(lives))
    #print secret_number
    #print lives
    
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    global hi_range
    hi_range = 100
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global hi_range
    hi_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global user_guess
    global lives
    
    print lives
    
    if (lives > 0):
        user_guess = int(guess)
        if (user_guess > secret_number):
            status.set_text("lower")
            lives -= 1
            chance.set_text("Remaining lives " + str(lives))
        elif (user_guess < secret_number):
            status.set_text("Higher")
            lives -= 1
            chance.set_text("Remaining lives " + str(lives))
        else:
            status.set_text("Correct")
            chance.set_text("Remaining lives " + str(lives))
    else:
        status.set_text("You are out of lives!")

    
# create frame
frame = simplegui.create_frame("Guessing Game", 250, 250)


# register event handlers for control elements and start frame
range_100 = frame.add_button("Range 1-100", range100)
range_1000 = frame.add_button("Range 1-1000", range1000)
guess_input = frame.add_input("Enter your guess", input_guess, 100)
status = frame.add_label("Your guess status")
chance = frame.add_label("Remaining Chance")

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
