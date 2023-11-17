# 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

>we wanto to add tracks to a list and then see all the tracks (songs) listened


# 2. Design the Class Interface
``` python 
class MusicTracker():
    
    def __init__(self):
        # parameters:
        #none
        # just an empty list
        pass

    def add_tracks_ive_listened(self, song: str)
        #parameters:
        #song: is a string with the name of the song
        #return
        # a list with the song added
        pass

    def see_list_of_tracks (self):
        #parameters:
        #return
        # a list with the songs listened
        pass
```
3. Create Examples as Tests
Make a list of examples of how the class will behave in different situations.
```python
given an empty list
return an empty list

music_tracker = MusicTracker()
music_tracker.see_list_of_tracks() #=> []

given a song listened
return the list with that song

music_tracker = MusicTracker()
music_tracker.add_tracks_ive_listened("Lateralus")
music_tracker.see_list_of_tracks() #=> ["Lateralus"]

given more than one song listened
return the list with the multiply entrys

music_tracker = MusicTracker()
music_tracker.add_tracksd_ive_listened ("Parabola", "The patient")  
music_tracker.see_list_of_tracks() #=> ["Lateralus", "Parabola", "The patient"] is possible to add two srings at the same time or one by one? i will try 

after added the song check list
return a list with the full tracks listened

music_tracker = MusicTracker()
music_tracker.see_list_of_tracks() #=> ["Lateralus", "Parabola", "The patient"] not sure if really necesary 


4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

lass MusicTracker():
    
   
