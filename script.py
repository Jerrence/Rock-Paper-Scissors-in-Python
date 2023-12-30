import random;
import time;
import sys;

choice = input("\nRock, Paper or Scissors\n").lower();

# check if choice doesn't match rock, paper and scissors
while choice != "rock" and choice != "paper" and choice != "scissors":
    choice = input("\nMake sure you typed: Rock, Paper or Scissors\n");

# Generates a random number between 1 and 3
bot_choice = random.randint(1, 3);

if bot_choice == 1:
    bot_choice = "rock";
elif bot_choice == 2:
    bot_choice = "paper";
elif bot_choice == 3:
    bot_choice = "scissors";

print("\nYour opponent chose " + bot_choice);

# Waits two seconds
time.sleep(2);

def print_loss():
    print("\nYour opponent won :(\n");

def print_victory():
    print("\nYou won!\n");

# choice = "rock"
if choice == "rock":
    if bot_choice == "paper":
        print_loss();
    elif bot_choice == "scissors":
        print_victory();

# choice = "paper"
if choice == "paper":
    if bot_choice == "scissors":
        print_loss();
    elif bot_choice == "rock":
        print_victory();

# choice = "scissors"
if choice == "scissors":
    if bot_choice == "rock":
        print_loss();
    elif bot_choice == "paper":
        print_victory();

# if both choices are equal
if choice == bot_choice:
    print("\nIt's a draw!\n");
