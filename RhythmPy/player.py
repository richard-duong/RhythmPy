from pydub import AudioSegment
from pydub.playback import play
import multiprocessing
import time

from RhythmPy.internal.constants import *

class Player:
    def __init__(self):
        self.play_process = None
        self.play_event = None
        self.play_mode = PlayMode.idle
        self.queue = []
        self.history = []
        self.loop = False

    def add_song(self, file_name: str):
        # store dict with title, name, duration
        self.history.append(dict)
        self.queue.append(dict)
    

    # thread waiting https://stackoverflow.com/questions/4995419/in-python-how-do-i-know-when-a-process-is-finished
    def play_song(self, file_name: str):
        self.stop_audio()
        song = AudioSegment.from_file(file_name, "mp4")
        self.p = multiprocessing.Process(target=play, args=(song,))
        self.p.start()

    def play_audio(self, file_name: str, duration: int):
        self.play_event = multiprocessing.Event()
        song = AudioSegment.from_file(file_name, "mp4")
        self.duration = (len(song) / 1000.0) 

    def stop_audio(self):
        if self.p != None
            self.p.terminate()
            self.p = None
        
