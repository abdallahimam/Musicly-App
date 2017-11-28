from models.Song import Song


class InAlbum(Song):
    'CLass InAlbum is used to define InAlbum Attribute'

    def __init__(self, name, featured_artist, album_title, bands_name, playlist_name,
                 song_type, released_date, genre, lyrics, duration):
        super().__init__(name, featured_artist, bands_name, playlist_name,
                         song_type, released_date, genre, lyrics, duration)
        self.album_title = album_title

    def set_album(self, album_title):
        self.album_title = album_title

    def get_album(self):
        return self.album_title
