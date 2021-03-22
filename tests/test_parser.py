import pytest
from RhythmPy.internal.constants import *
from RhythmPy.parser import Parser

# ===============
# Fixtures
# ===============

'''
Parser Constructors
'''
@pytest.fixture
def parser():
    '''Returns the default parser object'''
    return Parser()



'''
Youtube Video Links
'''
@pytest.fixture
def good_yt_video_links():
    '''Returns list of valid types of youtube video links'''
    yt_links = []
    yt_links.append("youtu.be/qfVuRQX0ydQ")
    yt_links.append("youtu.be/watch?v=qfVuRQX0ydQ")
    yt_links.append("http://youtu.be/qfVuRQX0ydQ")
    yt_links.append("http://youtu.be/watch?v=qfVuRQX0ydQ")
    yt_links.append("https://youtu.be/qfVuRQX0ydQ")
    yt_links.append("https://youtu.be/watch?v=qfVuRQX0ydQ")
    yt_links.append("youtube.com/watch?v=qfVuRQX0ydQ")
    yt_links.append("http://youtube.com/watch?v=qfVuRQX0ydQ")
    yt_links.append("https://youtube.com/watch?v=qfVuRQX0ydQ")
    return yt_links

@pytest.fixture
def bad_yt_video_links():
    '''Return list of invalid types of youtube video links'''
    yt_links = []
    yt_links.append("youtu.be/aaa")
    yt_links.append("youtube.com/aaa")
    yt_links.append("http://youtu.be/aaa")
    yt_links.append("http:\\\\youtu.be/qfVuRQX0ydQ")
    yt_links.append("http://youtube.com")
    yt_links.append("http://youtube.com/vi/dQw4w9WgXcQ?feature=youtube_gdata_player")
    yt_links.append("youtube.com/qfVuRQX0ydQ")
    yt_links.append("http://youtube.com/vi/oTJRivZTMLs&feature=channel")
    yt_links.append("http://www.youtube.com/ytscreeningroom?v=oTJRivZTMLs")
    yt_links.append("http://www.youtube.com/user/IngridMichaelsonVEVO#p/u/11/KdwsulMb8EQ")
    return yt_links



'''
Youtube Playlist Links
'''
@pytest.fixture
def good_yt_playlist_links():
    '''Return list of valid types of youtube playlist links'''
    yt_links = []
    yt_links.append("youtu.be/playlist?list=PLJqrye89yGLsrN8bJ5-ip7BG7rkizsHcx")
    yt_links.append("http://youtu.be/playlist?list=PLJqrye89yGLsrN8bJ5-ip7BG7rkizsHcx")
    yt_links.append("https://youtu.be/playlist?list=PLJqrye89yGLsrN8bJ5-ip7BG7rkizsHcx")
    yt_links.append("youtube.com/playlist?list=PLJqrye89yGLsrN8bJ5-ip7BG7rkizsHcx")
    yt_links.append("www.youtube.com/playlist?list=PLJqrye89yGLsrN8bJ5-ip7BG7rkizsHcx")
    yt_links.append("http://youtube.com/playlist?list=PLJqrye89yGLsrN8bJ5-ip7BG7rkizsHcx")
    yt_links.append("https://youtube.com/playlist?list=PLJqrye89yGLsrN8bJ5-ip7BG7rkizsHcx")
    return yt_links

@pytest.fixture
def bad_yt_playlist_links():
    '''Return list of invalid types of youtube playlist links'''
    yt_links = []
    yt_links.append("youtu.be/aaa")
    yt_links.append("youtube.com/aaa")
    yt_links.append("http://youtu.be/aaa")
    yt_links.append("http:\\\\youtu.be/qfVuRQX0ydQ")
    yt_links.append("http://youtube.com")
    yt_links.append("http://youtube.com/vi/dQw4w9WgXcQ?feature=youtube_gdata_player")
    yt_links.append("youtube.com/qfVuRQX0ydQ")
    yt_links.append("http://youtube.com/vi/oTJRivZTMLs&feature=channel")
    yt_links.append("http://www.youtube.com/ytscreeningroom?v=oTJRivZTMLs")
    yt_links.append("http://www.youtube.com/user/IngridMichaelsonVEVO#p/u/11/KdwsulMb8EQ")
    return yt_links



'''
Play Commands
'''
@pytest.fixture
def play_video_commands():
    '''Return list of play video commands'''
    play_commands = []
    play_commands.append("!play youtu.be/qfVuRQX0ydQ")
    play_commands.append("!play youtube.com/watch?v=qfVuRQX0ydQ")
    play_commands.append("!play https://youtube.com/watch?v=qfVuRQX0ydQ")
    return play_commands

@pytest.fixture
def play_video_args():
    '''Return list of play video arguments'''
    play_args = []
    play_args.append("youtu.be/qfVuRQX0ydQ")
    play_args.append("youtube.com/watch?v=qfVuRQX0ydQ")
    play_args.append("https://youtube.com/watch?v=qfVuRQX0ydQ")
    return play_args

@pytest.fixture
def play_playlist_commands():
    '''Return list of play playlist commands'''
    play_commands = []
    play_commands.append("!play https://www.youtube.com/playlist?list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj")
    play_commands.append("!play https://www.youtube.com/playlist?list=PLOHoVaTp8R7dfrJW5pumS0iD_dhlXKv17")
    play_commands.append("!play https://www.youtube.com/playlist?list=PLrV5OtvYx0F7SeG2F2Az7nCTOxDKmObdz")
    return play_commands

@pytest.fixture
def play_playlist_args():
    '''Return list of play playlist arguments'''
    play_args = []
    play_args.append("https://www.youtube.com/playlist?list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj")
    play_args.append("https://www.youtube.com/playlist?list=PLOHoVaTp8R7dfrJW5pumS0iD_dhlXKv17")
    play_args.append("https://www.youtube.com/playlist?list=PLrV5OtvYx0F7SeG2F2Az7nCTOxDKmObdz")
    return play_args

@pytest.fixture
def play_query_commands():
    '''Return list of play query commands'''
    play_commands = []
    play_commands.append("!play iu - 23")
    play_commands.append("!play weekly zigzag")
    play_commands.append("!play dunkey video")
    return play_commands

@pytest.fixture
def play_query_args():
    '''Return list of play query arguments'''
    play_args = []
    play_args.append("iu - 23")
    play_args.append("weekly zigzag")
    play_args.append("dunkey video")
    return play_args
    
@pytest.fixture
def play_error_commands():
    '''Return list of incorrect play commands'''
    play_commands = []
    play_commands.append("!play")
    play_commands.append("!playiu - 23")
    play_commands.append("!play,iu - 23")
    return play_commands



'''
Search Commands
'''
@pytest.fixture
def search_query_commands():
    '''Return list of search query commands'''
    search_commands = []
    search_commands.append("!search iu - 23")
    search_commands.append("!search niki indigo")
    search_commands.append("!search best super smash combos 64")
    return search_commands

@pytest.fixture
def search_query_args():
    '''Return list of search query arguments'''
    search_args = []
    search_args.append("iu - 23")
    search_args.append("niki indigo")
    search_args.append("best super smash combos 64")
    return search_args

@pytest.fixture
def search_error_commands():
    '''Return list of search error commands'''
    search_commands = []
    search_commands.append("!search")
    search_commands.append("!search,niki indigo")
    search_commands.append("!searchiu - 23")
    return search_commands



'''
Clear Commands
'''
@pytest.fixture
def clear_screen_commands():
    '''Returns clear command'''
    return ["!clear"]

@pytest.fixture
def clear_error_commands():
    '''Returns list of clear error commands'''
    clear_commands = []
    clear_commands.append("!clear...")
    clear_commands.append("!clear youtube.com")
    clear_commands.append("!clearscreen")
    return clear_commands



'''
Nowplaying Commands
'''
@pytest.fixture
def nowplaying_screen_commands():
    '''Returns nowplaying command'''
    return ["!nowplaying"]

@pytest.fixture
def nowplaying_error_commands():
    '''Returns list of nowplaying error commands'''
    nowplaying_commands = []
    nowplaying_commands.append("!nowplaying...")
    nowplaying_commands.append("!nowplaying youtube.com")
    nowplaying_commands.append("!nowplaying my movie")
    return nowplaying_commands



'''
Replay Commands
'''
@pytest.fixture
def replay_song_commands():
    '''Returns replay command'''
    return ["!replay"]

@pytest.fixture
def replay_error_commands():
    '''Returns list of replay error commands'''
    replay_commands = []
    replay_commands.append("!replay...")
    replay_commands.append("!replay youtube.com")
    replay_commands.append("!replay my movie")
    return replay_commands



'''
Loop Commands
'''
@pytest.fixture
def loop_song_commands():
    '''Returns loop command'''
    return ["!loop"]

@pytest.fixture
def loop_error_commands():
    '''Returns list of loop error commands'''
    loop_commands = []
    loop_commands.append("!loop...")
    loop_commands.append("!loop youtube.com")
    loop_commands.append("!loop my movie")
    return loop_commands



'''
Skip Commands
'''
@pytest.fixture
def skip_song_commands():
    '''Returns skip command'''
    return ["!skip"]

@pytest.fixture
def skip_error_commands():
    '''Returns list of skip error commands'''
    skip_commands = []
    skip_commands.append("!skip...")
    skip_commands.append("!skip youtube.com")
    skip_commands.append("!skip my movie")
    return skip_commands



'''
Stop Commands
'''
@pytest.fixture
def stop_song_commands():
    '''Returns stop command'''
    return ["!stop"]

@pytest.fixture
def stop_error_commands():
    '''Returns list of stop error commands'''
    stop_commands = []
    stop_commands.append("!stop...")
    stop_commands.append("!stop youtube.com")
    stop_commands.append("!stop my movie")
    return stop_commands




# ================
# Acts and Asserts
# ================

'''
Unit Test Parser Constructor
'''
def test_parser_default(parser):
    assert parser.mode == CommandMode.default 
    assert parser.args == list() 



'''
Unit Test Youtube Video Identification
'''
def test_is_video_true(parser, good_yt_video_links):
    for link in good_yt_video_links:
        assert parser.__is_yt_video__(link) == True

def test_is_video_false(parser, bad_yt_video_links, good_yt_playlist_links):
    for link in bad_yt_video_links:
        assert parser.__is_yt_video__(link) == False
    for link in good_yt_playlist_links:
        assert parser.__is_yt_video__(link) == False



'''
Unit Test Youtube Playlist Identification
'''
def test_is_playlist_true(parser, good_yt_playlist_links):
    for link in good_yt_playlist_links:
        assert parser.__is_yt_playlist__(link) == True

def test_is_playlist_false(parser, bad_yt_playlist_links, good_yt_video_links):
    for link in bad_yt_playlist_links:
        assert parser.__is_yt_playlist__(link) == False
    for link in good_yt_video_links:
        assert parser.__is_yt_playlist__(link) == False



'''
Unit Test Parse Play Commands
'''
def test_parse_play_video(parser, play_video_commands, play_video_args):
    for cmd, arg in zip(play_video_commands, play_video_args):
        parser.args = cmd.split(' ', maxsplit=1)
        parser.__parse_play__(cmd)
        assert parser.args[0] == "!play"
        assert parser.args[1] == arg
        assert parser.mode == CommandMode.play_video

def test_parse_play_playlist(parser, play_playlist_commands, play_playlist_args):
    for cmd, arg in zip(play_playlist_commands, play_playlist_args):
        parser.args = cmd.split(' ', maxsplit=1)
        parser.__parse_play__(cmd)
        assert parser.args[0] == "!play"
        assert parser.args[1] == arg
        assert parser.mode == CommandMode.play_playlist

def test_parse_play_query(parser, play_query_commands, play_query_args):
    for cmd, arg in zip(play_query_commands, play_query_args):
        parser.args = cmd.split(' ', maxsplit=1)
        parser.__parse_play__(cmd)
        assert parser.args[0] == "!play"
        assert parser.args[1] == arg
        assert parser.mode == CommandMode.play_query

def test_parse_play_error(parser, play_error_commands):
    for cmd in play_error_commands:
        parser.args = cmd.split(' ', maxsplit=1)
        parser.__parse_play__(cmd)
        assert parser.mode == CommandMode.play_error



'''
Unit Test Parse Search Commands
'''
def test_parse_search_query(parser, search_query_commands, search_query_args):
    for cmd, arg in zip(search_query_commands, search_query_args):
        parser.args = cmd.split(' ', maxsplit=1)
        parser.__parse_search__(cmd)
        assert parser.mode == CommandMode.search_query

def test_parse_search_error(parser, search_error_commands):
    for cmd in search_error_commands:
        parser.args = cmd.split(' ', maxsplit=1)
        parser.__parse_search__(cmd)
        assert parser.mode == CommandMode.search_error


'''
Unit Test Parse Clear Commands
'''
def test_parse_clear_screen(parser, clear_screen_commands):
    for cmd in clear_screen_commands:
        parser.args = cmd
        parser.__parse_clear__(cmd)
        assert parser.mode == CommandMode.clear_screen

def test_parse_clear_error(parser, clear_error_commands):
    for cmd in clear_error_commands:
        parser.args = cmd
        parser.__parse_clear__(cmd)
        assert parser.mode == CommandMode.clear_error 
         


'''
Unit Test Parse Now Playing Commands
'''
def test_parse_nowplaying_screen(parser, nowplaying_screen_commands):
    for cmd in nowplaying_screen_commands:
        parser.args = cmd
        parser.__parse_nowplaying__(cmd)
        assert parser.mode == CommandMode.nowplaying_screen

def test_parse_nowplaying_error(parser, nowplaying_error_commands):
    for cmd in nowplaying_error_commands:
        parser.args = cmd
        parser.__parse_nowplaying__(cmd)
        assert parser.mode == CommandMode.nowplaying_error
    


'''
Unit Test Parse Replay Commands
'''
def test_parse_replay_song(parser, replay_song_commands):
    for cmd in replay_song_commands:
        parser.args = cmd
        parser.__parse_replay__(cmd)
        assert parser.mode == CommandMode.replay_song

def test_parse_replay_error(parser, replay_error_commands):
    for cmd in replay_error_commands:
        parser.args = cmd
        parser.__parse_replay__(cmd)
        assert parser.mode == CommandMode.replay_error



'''
Unit Test Parse Loop Commands
'''
def test_parse_loop_song(parser, loop_song_commands):
    for cmd in loop_song_commands:
        parser.args = cmd
        parser.__parse_loop__(cmd)
        assert parser.mode == CommandMode.loop_song

def test_parse_loop_error(parser, loop_error_commands):
    for cmd in loop_error_commands:
        parser.args = cmd
        parser.__parse_loop__(cmd)
        assert parser.mode == CommandMode.loop_error



'''
Unit Test Parse Skip Commands
'''
def test_parse_skip_song(parser, skip_song_commands):
    for cmd in skip_song_commands:
        parser.args = cmd
        parser.__parse_skip__(cmd)
        assert parser.mode == CommandMode.skip_song

def test_parse_skip_error(parser, skip_error_commands):
    for cmd in skip_error_commands:
        parser.args = cmd
        parser.__parse_skip__(cmd)
        assert parser.mode == CommandMode.skip_error



'''
Unit Test Parse Stop Commands
'''
def test_parse_stop_song(parser, stop_song_commands):
    for cmd in stop_song_commands:
        parser.args = cmd
        parser.__parse_stop__(cmd)
        assert parser.mode == CommandMode.stop_song

def test_parse_stop_error(parser, stop_error_commands):
    for cmd in stop_error_commands:
        parser.args = cmd
        parser.__parse_stop__(cmd)
        assert parser.mode == CommandMode.stop_error



'''
Integration Test Parse
'''
def test_integration_parse_play_video(parser):
    pass

def test_integration_parse_play_playlist(parser):
    pass

def test_integration_parse_play_query(parser):
    pass

def test_integration_parse_play_error(parser):
    pass



def test_integration_parse_search_query(parser):
    pass

def test_integration_parse_search_error(parser):
    pass



def test_integration_parse_clear_screen(parser):
    pass

def test_integration_parse_clear_error(parser):
    pass



def test_integration_parse_nowplaying_screen(parser):
    pass

def test_integration_parse_nowplaying_error(parser):
    pass



def test_integration_parse_replay_song(parser):
    pass

def test_integration_parse_replay_error(parser):
    pass



def test_integration_parse_loop_song(parser):
    pass

def test_integration_parse_loop_error(parser):
    pass



def test_integration_parse_skip_song(parser):
    pass

def test_integration_parse_skip_error(parser):
    pass



def test_integration_parse_stop_song(parser):
    pass

def test_integration_parse_stop_error(parser):
    pass


