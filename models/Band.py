from models.Artist import Artist

class Band:
    'CLass Band is used to define Band Attribute'
    def __init__(self, name, list_of_artists):
        self.name = name
        self.list_of_artists = list_of_artists
    
    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    def set_list_of_artists(self, list_of_artists):
        self.list_of_artists = list_of_artists
    
    def get_list_of_artists(self):
        return self.list_of_artists
    
    def add_artist_to_band(self, artist):
        if self.list_of_artists == None:
            self.list_of_artists = []
        self.list_of_artists.append(artist)
    def remove_artist_from_band(self, artist):
        if artist == None or self.list_of_songs == None:
            return
        position = -1
        for i, iArtist in enumerate(self.list_of_artists):
            if iArtist.get_name() == artist.get_name():
                position = i
                break
        if position != -1:
            self.list_of_artists.remove(position)
    