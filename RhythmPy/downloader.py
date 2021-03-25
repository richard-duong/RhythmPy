from pytube import YouTube
from pytube.exceptions import *

class Downloader:
    def __init__(self):
        pass

    def download_link(self, link: str) -> bool:
        
        try:
            source = YouTube(link)
            stream = source.streams
            stream.download(output_path="temp/", filename="song")
            return True

        except VideoUnavailable as e:
            print(f"The link: {link} received a Video Unavailable Error")
            return False
    
        except IndexError as e:
            print(f"The link: {link} received an Index Error")
            return False
          
            
