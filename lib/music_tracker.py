class MusicTracker():
    def __init__(self):
        self.list_music = []

    def add_tracks_ive_listened(self, song):
        self.list_music.append(song)
        songs = " "
        for song in self.list_music[:-1]:
            songs += song + " , "
        songs += f" and {self.list_music [-1]}"
        return f"Ive listened to {songs}"

    def see_list_of_tracks (self):
        return self.list_music
