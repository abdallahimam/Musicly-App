from models.Song import Song


class Playlist:
    'CLass Playlist is used to define Playlist Attribute'

    def __init__(self, name, description, list_of_songs, number_of_songs):
        self.name = name
        self.description = description
        if list_of_songs == None:
            self.list_of_songs = []
        else:
            self.list_of_songs = list_of_songs
        if number_of_songs == None:
            self.number_of_songs = 0
        else:
            self.number_of_songs = number_of_songs

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_number_of_songs(self):
        return self.number_of_songs

    def set_description(self, description):
        self.description = description

    def set_list_of_songs(self, list_of_songs):
        self.list_of_songs = list_of_songs

    def add_song_to_playlist(self, song):
        if song == None:
            return
        if self.list_of_songs == None:
            self.list_of_songs = []
        self.list_of_songs.append(song)
        self.number_of_songs += 1

    def remove_song_from_playlist(self, song):
        if song == None or self.list_of_songs == None:
            return
        position = -1
        for i, iSong in enumerate(self.list_of_songs):
            if iSong.get_name() == song.get_name():
                position = i
                break
        if position != -1:
            self.list_of_songs.remove(position)
            self.number_of_songs -= 1

    def get_number_of_songs(self):
        if self.number_of_songs != None:
            return self.number_of_songs
        return 0

    def get_list_of_songs(self):
        return self.list_of_songs
