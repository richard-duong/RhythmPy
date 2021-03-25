from os import system, name
from time import sleep

from RhythmPy.internal.constants import *
from RhythmPy.parser import Parser

class Interface:
    def __init__(self, symbol: str = ">"):
        self.symbol = symbol
    
    def prompt(self):
        print(f"{self.symbol}", end=" ")

    def welcome_menu(self):
        print("Welcome to RhythmPy")
        print("Type !help for a full list of commands")

    def clear_screen(self): 
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")

    def help_menu(self):
        print("Commands for RhythmPy")
        print("=====================")
        print("!play <link/query>")
        print("\tPlays song under link or query")
        print("!search <query>")
        print("\tSearches for a query")
        print("")
        print("!clear")
        print("\tClears screen")
        print("")
        print("!nowplaying")
        print("\tShows what song Rhythm is currently playing")
        print("")
        print("!replay")
        print("\tReplays the last played song")
        print("")
        print("!loop")
        print("\tLoops the current queue")
        print("")
        print("!skip")
        print("\tSkips the current song in queue")
        print("")
        print("!stop")
        print("\tStops the current song")

        
        
    
