# Hangman

## Description

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## What I learned in this project

I learnt how to use classes to organise code into efficient blocks - rather than have a sprawling and difficiult-to-navigate collection of code. This is not something that I have come across before and I was implementing learning from lessons straight into the project.

I learnt a lot more about loops in practise as I didn't insert break statements appropriately in earlier versions of the code which meant loops didn't exit at the appropriate time.

I developed better strategies for debugging code - I was able to identify why the game was finishing too early when words with characters that appear multiple times (such as 'a' and 'b' in banana) lead to the game being won prematurely. My improved debugging approach meant I could identify (through print statements) that remaining unique letters was being reduced multiple times in the loop rather than just the single time required.

I practised my use of repositories in order update the manuy versions of code developed along the way!

## Files

## milestone_2.py
This file contains basic validation code for checking valid inputs for the start of the hangman project

## milestone_3.py
This file contains basic functions for validating inputs and checking the guessed letter against a random word

## milestone_4.py
Defines the Hangman class and associated methods

## milestone_5.py
Finalised Hangman class and methods. Introduces the play_game() function to run a full game