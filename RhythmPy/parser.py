import re
from RhythmPy.internal.constants import *

class Parser: 
    def __init__(self):
        self.mode = CommandMode.default
        self.args = []
        pass



    '''
    Validation Checks
    '''

    """Checks if query is a youtube video"""
    def __is_yt_video__(self, query: str) -> bool:
        _rex = re.compile(YoutubeRegex.video)
        if _rex.fullmatch(query):
            return True
        return False

    """Checks if query is a youtube playlist""" 
    def __is_yt_playlist__(self, query: str) -> bool:
        _rex = re.compile(YoutubeRegex.playlist)
        if _rex.fullmatch(query):
            return True
        return False




    '''
    Unit Parsing
    '''


    """Runs the play parsing on !play prefix"""
    def __parse_play__(self, user_input: str) -> bool:
        self.args = user_input.split(' ', maxsplit=1)
        if len(self.args) == 1 or self.args[0] != CommandQuery.play:
            self.mode = CommandMode.play_error
            return False
        if self.__is_yt_video__(self.args[1]):
            self.mode = CommandMode.play_video
        elif self.__is_yt_playlist__(self.args[1]):
            self.mode = CommandMode.play_playlist
        else:
            self.mode = CommandMode.play_query
        return True

    """Runs the searching parser on !search prefix"""
    def __parse_search__(self, user_input: str) -> bool:
        self.args = user_input.split(' ', maxsplit=1)
        if len(self.args) == 1 or self.args[0] != CommandQuery.search: 
            self.mode = CommandMode.search_error
            return False
        else:
            self.mode = CommandMode.search_query
        return True

    """Runs the clearing parser on !clear prefix"""
    def __parse_clear__(self, user_input: str) -> bool:
        self.args = [user_input]
        if self.args[0] != CommandQuery.clear:
            self.mode = CommandMode.clear_error
            return False
        else:
            self.mode = CommandMode.clear_screen
        return True 

    """Runs the nowplaying parser on !nowplaying prefix"""
    def __parse_nowplaying__(self, user_input: str) -> bool:
        self.args = [user_input]
        if self.args[0] != CommandQuery.nowplaying:
            self.mode = CommandMode.nowplaying_error
            return False
        else:
            self.mode = CommandMode.nowplaying_screen
        return True  

    """Runs the replay parser on !replay prefix"""
    def __parse_replay__(self, user_input: str) -> bool:
        self.args = [user_input]
        if self.args[0] != CommandQuery.replay:
            self.mode = CommandMode.replay_error
            return False
        else:
            self.mode = CommandMode.replay_song
        return True

    """Runs the loop parser on !loop prefix"""
    def __parse_loop__(self, user_input: str) -> bool:
        self.args = [user_input]
        if self.args[0] != CommandQuery.loop:
            self.mode = CommandMode.loop_error
            return False
        else:
            self.mode = CommandMode.loop_song
        return True

    """Runs the skip parser on !skip prefix"""
    def __parse_skip__(self, user_input: str) -> bool:
        self.args = [user_input]
        if self.args[0] != CommandQuery.skip:
            self.mode = CommandMode.skip_error
            return False
        else:
            self.mode = CommandMode.skip_song
        return True
 
    """Runs the stop parser on !stop prefix"""
    def __parse_stop__(self, user_input: str) -> bool:
        self.args = [user_input]
        if self.args[0] != CommandQuery.stop:
            self.mode = CommandMode.stop_error
            return False
        else:
            self.mode = CommandMode.stop_song
        return True 
  

 
    '''
    Integration Parsing
    '''      

    """Parses user input and fills in appropriate mode or errors"""
    def parse(self, user_input: str) -> bool:
        if user_input.startswith(CommandQuery.play):
            self.__parse_play__(user_input)
        elif user_input.startswith(CommandQuery.search):
            self.__parse_search__(user_input)
        elif user_input.startswith(CommandQuery.clear):
            self.__parse_clear__(user_input)
        elif user_input.startswith(CommandQuery.nowplaying):
            self.__parse_nowplaying__(user_input)
        elif user_input.startswith(CommandQuery.replay):
            self.__parse_replay__(user_input)
        elif user_input.startswith(CommandQuery.loop):
            self.__parse_loop__(user_input)
        elif user_input.startswith(CommandQuery.skip):
            self.__parse_skip__(user_input)
        elif user_input.startswith(CommandQuery.stop):
            self.__parse_stop__(user_input)
        else:
            self.mode = CommandMode.unknown 
            self.args = [user_input]
