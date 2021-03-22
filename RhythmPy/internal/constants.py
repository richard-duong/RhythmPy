"""Queries for identifying how to parse user input"""
class CommandQuery:
    play = "!play"              # complete parse is complete
    search = "!search"          # complete search is complete
    clear = "!clear"            # complete clear command
    nowplaying = "!nowplaying"  # complete nowplaying command
    replay = "!replay"          # complete replay command
    loop = "!loop"              # complete loop command
    skip = "!skip"              # complete
    stop = "!stop"              # complete
    pause = "!pause"            # optional
    resume = "!resume"          # optional
    seek = "!seek"              # optional
    rewind = "!rewind"          # optional
    forward = "!forward"        # optional


"""Identify which mode to run after parsing user input""" 
class CommandMode:
    unknown = -1
    default = 0
    play_video = 1
    play_playlist = 2
    play_query = 3
    play_error = 4
    search_query = 6
    search_error = 7
    clear_screen = 8
    clear_error = 9
    nowplaying_screen = 10
    nowplaying_error = 11
    replay_song = 12
    replay_error = 13
    loop_song = 14
    loop_error = 15
    skip_song = 16
    skip_error = 17
    stop_song = 18
    stop_error = 19



"""
Regexes to match videos or playlists

Sources:
(modified to handle edge cases)
video: https://stackoverflow.com/questions/19377262/regex-for-youtube-url, https://stackoverflow.com/questions/2964678/jquery-youtube-url-validation-with-regex
playlist: https://stackoverflow.com/questions/5288941/validating-youtube-playlist-url-using-regex
"""

class YoutubeRegex:
    video = r"^(?:https?:\/\/)?(?:www\.)?((?:youtu\.be\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=)?)|(?:youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=)))((\w|-){11})"
    playlist = r"^(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/)(?:playlist\?list=)(\w|-)+"
