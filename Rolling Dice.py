Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 12:54:16) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
"""
This is a rolling dice game
"""
from random import randint
from time import sleep
def get_user_guess():
  user_guess = int(raw_input("Guess a number:"))
  return user_guess
def roll_dice(number_of_sides):
  first_roll = randint(1,number_of_sides)
  second_roll = randint(1,number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum possible value is: " + str(max_val)
  sleep(1)
  user_guess = get_user_guess()
  if user_guess > max_val:
    print "No guessing higher than the maximum possible value!"
    return
  else:
    print "Rolling..."
    sleep(2)
    print "The first value is: %d" % first_roll
    sleep(1)
    print "The second value is: %d" % second_roll
    total_roll = first_roll + second_roll
    print "The result is: %d" % total_roll
    if user_guess > total_roll:
      print "You won!"
      return
    if user_guess < total_roll:
      print "You lost, try again."
      return
roll_dice(6)
python Rolling Dice.py

