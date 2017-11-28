class Song:
    'CLass Song is used to define Song Attribute'

    def __init__(self, name, featured_artist, bands_name, playlist_name,
                 song_type, released_date, genre, lyrics, duration):
        self.name = name
        self.featured_artist = featured_artist
        self.released_date = released_date
        self.genre = genre
        self.lyrics = lyrics
        self.duration = duration
        if bands_name == None:
            self.bands_name = ['','']
        else:
            self.bands_name = bands_name
        if playlist_name == None:
            self.playlist_name = ''
        else:
            self.playlist_name = playlist_name
        self.type = song_type

    def set_name(self, name):
        self.name = name

    def set_featured_artist(self, featured_artist):
        self.featured_artist = featured_artist

    def set_released_date(self, released_date):
        self.released_date = released_date

    def set_genre(self, genre):
        self.genre = genre

    def set_lyrics(self, lyrics):
        self.lyrics = lyrics

    def set_duration(self, duration):
        self.duration = duration

    def set_bands_name(self, bands_name):
        self.bands_name = bands_name

    def set_playlist_name(self, playlist_name):
        self.playlist_name = playlist_name

    def set_type(self, song_type):
        self.type = song_type

    def get_name(self):
        return self.name

    def get_featured_artist(self):
        return self.featured_artist

    def get_released_date(self):
        return self.released_date

    def get_genre(self):
        return self.genre

    def get_lyrics(self):
        return self.lyrics

    def get_duration(self):
        return self.duration

    def get_band(self):
        return self.bands_name

    def get_bands_name(self):
        return self.bands_name

    def get_playlist_name(self):
        return self.playlist_name

    def get_type(self):
        return self.type
