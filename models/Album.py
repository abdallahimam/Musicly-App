from models.Song import Song


class Album:
    'CLass Album is used to define Album Attribute'

    def __init__(self, title, band_name, number_of_songs, list_of_songs):
        self.title = title
        if self.band_name == None:
            self.band_name = ''
        else:
            self.band_name = band_name
        if self.number_of_songs == None:
            self.number_of_songs = 0
        else:
            self.number_of_songs = number_of_songs
        if self.list_of_songs == None:
            self.list_of_songs = []
        else:
            self.list_of_songs = list_of_songs

    def set_title(self, title):
        self.title = title

    def set_band_name(self, bands_name):
        self.bands_name = bands_name

    def set_list_of_songs(self, list_of_songs):
        self.list_of_songs = list_of_songs

    def get_title(self):
        return self.title

    def get_band_name(self):
        return self.bands_name

    def get_list_of_songs(self):
        return self.list_of_songs

    def add_song_to_album(self, song):
        if song == None:
            return
        if self.list_of_songs == None:
            self.list_of_songs = []
        self.list_of_songs.append(song)
        self.number_of_songs += 1

    def remove_song_from_album(self, song):
        if song == None or self.list_of_songs == None:
            return
        position = -1
        for i, iSong in enumerate(list_of_songs):
            if iSong.get_name() == song.get_name():
                position = i
                break
        if position != -1:
            self.list_of_songs.remove(position)
            self.number_of_songs -= 1

    def get_list_of_songs(self):
        return self.list_of_songs

    def get_number_of_songs(self):
        if self.number_of_songs != None:
            return self.number_of_songs
        return 0
