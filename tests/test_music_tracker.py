from lib.music_tracker import *

def test_empty_list():
    music_tracker = MusicTracker()
    result = music_tracker.see_list_of_tracks()
    assert result == []

def test_adding_song_to_list():
    music_tracker = MusicTracker()
    music_tracker.add_tracks_ive_listened("Lateralus")
    result = music_tracker.see_list_of_tracks()
    assert result == ["Lateralus"]

def test_adding_multiple_songs():
    music_tracker = MusicTracker()
    music_tracker.add_tracks_ive_listened("Lateralus")
    music_tracker.add_tracks_ive_listened("Parabola")
    music_tracker.add_tracks_ive_listened("The patient")
    result = music_tracker.see_list_of_tracks()
    assert result == ["Lateralus", "Parabola", "The patient"]

    # just fo the time of the recording i will add
    #one by one the songs
    #with more time i know i find the solution.

    # i stopped the video so i could find a solution for this
    # and I found a way using a video from the examples to do this

