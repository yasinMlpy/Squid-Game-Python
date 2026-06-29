# Squid-Game-Python
Number Guessing Game

A simple command-line game where you try to guess a random number chosen by the computer.

How It Works


You enter a number between 1 and 10.
The computer then picks its own random number between 1 and 10.
If your number matches the computer's number, you win.
If it doesn't match, you lose — and the correct number is revealed.
Enter 0 at any time to exit the game.


Requirements


Python 3.x
My Python version:3.13.7 


Usage

Run the script from your terminal:

bashpython squidgame.py

Then follow the prompt:

choose number of 1of10: and 0=Exit:7
you lost, computer choose:3
choose number of 1of10: and 0=Exit:3
you win, computer choose:3
choose number of 1of10: and 0=Exit:0

Input Validation


Non-numeric input (e.g. letters or symbols) is caught and won't crash the program — you'll be asked to try again.
Numbers outside the 1–10 range are rejected with a message asking you to choose again.


Notes


The random number is generated after your guess is entered (and only if it's not 0), so an invalid guess doesn't "use up" a random number.
The game loops indefinitely until you choose to exit by entering 0

Created by Yasin 
