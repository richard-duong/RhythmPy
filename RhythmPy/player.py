from pydub import AudioSegment
from pydub.playback import play
import multiprocessing
import time

class Player:
    def __init__(self):
        self.p = None

    def play_audio(self, file_name: str):
        song = AudioSegment(file_name, "mp4")
        self.p = multiprocessing.Process(target=play, args=(song,))
        self.p.start()

    def stop_audio(self):
        p.terminate()
        
