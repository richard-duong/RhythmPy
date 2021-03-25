from pytube import YouTube
from RhythmPy.parser import Parser
from RhtyhmPy.interface import Interface
from RhythmPy.internal.constants import *

def Core:
    def __init__(self):
        self.interface = Interface()
        pass

    def __play_video__(self, parser: Parser):
        link = parser.args[1]
        source = YouTube(link)
        

    def __running_state__(self, prompt_symbol: str = ">"):


        while True:
            parser = Parser()
            user_input = input(prompt_symbol + " ") 
            parse_check = parser.parse(user_input)
             
            if parse_check == False:
                # display error  

            elif parser.mode == CommandMode.play_video:
                self.__play_video__(parser)
               
                

            
        
                
    def start(self):
        self.interface.welcome_screen()
        self.__running_state__()
