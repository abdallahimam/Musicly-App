import sqlite3
import errno
from models.Playlist import Playlist
from models.Song import Song
from models.InAlbum import InAlbum
from models.Album import Album
from models.Band import Band
from models.Artist import Artist


class SongController:
    'This class is The controller of song(add/remove/....)'

    def add_song(self, song):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        try:
            sqlStatement = '''INSERT INTO SONG(NAME, FEATURED_ARTIST, ABUM_TITLE, BAND_NAME_1, BAND_NAME_2, PLAYLIST_NAME, 
                                               SONG_TYPE,RELEASED_DATE,GENRE,LYRICS,DURATION) VALUES(?,?,?,?,?,?,?,?,?,?,?)
                           '''
            if song.get_type() == 'Single' or song.get_type() == 'single':
                cur.execute(sqlStatement,
                            (song.get_name(), song.get_featured_artist(), None, song.get_band()[0], song.get_band()[1],
                             song.get_playlist_name(), song.get_type(), song.get_released_date(), song.get_genre(),
                                song.get_lysics(), song.get_duration(),
                             ))
            else:
                cur.execute(sqlStatement,
                            (song.get_name(), song.get_featured_artist(), song.get_album, song.get_band()[0],
                             song.get_band()[1], song.get_playlist_name(
                            ), song.get_type(), song.get_released_date(),
                                song.get_genre(), song.get_lysics(), song.get_duration(),
                            ))
            connection.commit()
        except Exception as ex:
            return 'error'
        connection.close()

    def delete_song(self, song_name):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        rs = None
        try:
            sqlStatement = 'SELECT PLAYLIST_NAME FROM SONG WHERE NAME=?'
            rs = cur.execute(sqlStatement, (song_name,))
            playlist_name = rs.fetchone()[0]
            sqlStatement = 'DELETE FROM SONG WHERE NAME=?'
            cur.execute(sqlStatement, (song_name,))
            connection.commit()
            sqlStatement = 'SELECT NAME FROM SONG WHERE PLAYLIST_NAME=?'
            rs = cur.execute(sqlStatement, (playlist_name,))
            number_of_songs = len(rs)
            self.update_playlist_number_of_songs(
                playlist_name, number_of_songs)
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()

    def get_song(self, song_name):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        row = None
        try:
            connection.row_factory = sqlite3.Row
            sqlStatement = 'SELECT * FROM SONG WHERE NAME=?'
            cur.execute(sqlStatement, (song_name,))
            row = cur.fetchone()
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()
        # return SongController.map_to_song_object(row)
        my_song = None
        type_of_my_song = row[6]
        if type_of_my_song == 'Single':
            my_song = Song(row[0], row[1], [row[3], row[4]],
                           row[5], row[6], row[7], row[8], row[9], row[10])
        else:
            my_song = InAlbum(row[0], row[1], row[2],
                              [row[3], row[4]], row[5], row[6], row[7], row[8], row[9], row[10])
        return my_song

    def get_songs_by_album(self, album_title):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        rs = None
        try:
            connection.row_factory = sqlite3.Row
            sqlStatement = 'SELECT * FROM SONG WHERE ALBUM_TITLE=?'
            cur.execute(sqlStatement, (album_title,))
            rs = cur.fetchall()
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()
        return self.map_result_set_to_list_of_objects(rs)

    def get_songs_by_genre(self, genre):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        rs = None
        try:
            connection.row_factory = sqlite3.Row
            sqlStatement = 'SELECT * FROM SONG WHERE GENRE=?'
            cur.execute(sqlStatement, (genre,))
            rs = cur.fetchall()
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()
        return self.map_result_set_to_list_of_objects(rs)

    def get_songs_by_band(self, band_name):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        rs = None
        try:
            connection.row_factory = sqlite3.Row
            sqlStatement = 'SELECT * FROM SONG WHERE BAND_NAME_1=? OR BAND_NAME_2=?'
            cur.execute(sqlStatement, (band_name, band_name,))
            rs = cur.fetchall()
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()
        return self.map_result_set_to_list_of_objects(rs)

    def get_songs_by_artist(self, artist_name):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        rs = None
        try:
            connection.row_factory = sqlite3.Row
            sqlStatement = 'SELECT NAME FROM BAND WHERE ARTIST_NAME=?'
            cur.execute(sqlStatement, (artist_name,))
            band_name_for_artist = cur.fetchone()
            # print(band_name_for_artist)
            sqlStatement = 'SELECT * FROM SONG WHERE FEATURED_ARTIST=? OR BAND_NAME_1=? OR BAND_NAME_2=?'
            cur.execute(sqlStatement, (artist_name,
                                       band_name_for_artist[0], band_name_for_artist[0],))
            rs = cur.fetchall()
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()
        return self.map_result_set_to_list_of_objects(rs)

    def get_songs_by_playlist(self, playlist_name):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        rs = None
        try:
            connection.row_factory = sqlite3.Row
            sqlStatement = 'SELECT * FROM SONG WHERE PLAYLIST_NAME=?'
            cur.execute(sqlStatement, (playlist_name,))
            rs = cur.fetchall()
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()
        return self.map_result_set_to_list_of_objects(rs)

    def get_all_songs(self):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        rs = None
        try:
            connection.row_factory = sqlite3.Row
            sqlStatement = 'SELECT * FROM SONG'
            cur.execute(sqlStatement)
            rs = cur.fetchall()
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()
        return self.map_result_set_to_list_of_objects(rs)

    def delete_songs_by_album(self, album_title):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        rs = None
        try:
            sqlStatement = 'SELECT PLAYLIST_NAME FROM SONG WHERE ALBUM_TITLE=?'
            rs = cur.execute(sqlStatement, (album_title,))
            playlist_name = rs.fetchone()[0]

            sqlStatement = 'DELETE FROM SONG WHERE ALBUM_TITLE=?'
            cur.execute(sqlStatement, (album_title,))
            connection.commit()

            sqlStatement = 'SELECT NAME FROM SONG WHERE PLAYLIST_NAME=?'
            rs = cur.execute(sqlStatement, (playlist_name,))
            number_of_songs = len(rs)
            self.update_playlist_number_of_songs(playlist_name, number_of_songs)
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()

    def delete_songs_by_band(self, band_name):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        try:
            sqlStatement = 'SELECT PLAYLIST_NAME FROM SONG WHERE BAND_NAME_1=? OR BAND_NAME_2=?'
            rs = cur.execute(sqlStatement, (band_name, band_name,))
            playlist_name = rs.fetchone()[0]

            sqlStatement = 'DELETE FROM SONG WHERE BAND_NAME_1=? OR BAND_NAME_2=?'
            cur.execute(sqlStatement, (band_name, band_name,))
            connection.commit()

            sqlStatement = 'SELECT NAME FROM SONG WHERE PLAYLIST_NAME=?'
            rs = cur.execute(sqlStatement, (playlist_name,))
            number_of_songs = len(rs)
            self.update_playlist_number_of_songs(playlist_name, number_of_songs)
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()

    def delete_songs_by_band(self, band_name):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        try:
            sqlStatement = 'DELETE * FROM SONG WHERE BAND_NAME_1=? OR BAND_NAME_2=?'
            cur.execute(sqlStatement, (band_name, band_name,))
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()

    def delete_songs_by_playlist(self, playlist_name):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        try:
            sqlStatement = 'DELETE FROM SONG WHERE PLAYLIST_NAME = ?'
            cur.execute(sqlStatement, (playlist_name,))
            connection.commit()
        except Exception as ex:
            print("There Is An Exception.")
            ex.errno
        connection.close()

    def delete_songs_by_artist(self, artist_name):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        try:
            sqlStatement = 'SELECT PLAYLIST_NAME, BAND_NAME_1, BAND_NAME_2 FROM SONG WHERE FEATURED_ARTIST=?'
            rs = cur.execute(sqlStatement, (artist_name,))
            playlist_name = rs.fetchone()[0]

            sqlStatement = 'DELETE FROM SONG WHERE FEATURED_ARTIST=?'
            cur.execute(sqlStatement, (artist_name,))
            connection.commit()

            sqlStatement = 'SELECT NAME FROM BAND WHERE ARTIST_NAME=?'
            rs = cur.execute(sqlStatement, (artist_name,))
            band_name_for_artist = rs.fetchone()[0]

            sqlStatement = 'SELECT NAME FROM SONG WHERE PLAYLIST_NAME=? OR BAND_NAME_1=? OR BAND_NAME_2=?'
            rs = cur.execute(sqlStatement, (playlist_name, band_name_for_artist, band_name_for_artist,))
            number_of_songs = len(rs)
            self.update_playlist_number_of_songs(playlist_name, number_of_songs)
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()

    def update_song_playlist(self, playlist_name, new_playlist_name):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        try:
            sqlStatement = 'UPDATE SONG SET PLAYLIST_NAME=? WHERE PLAYLIST_NAME=?'
            cur.execute(sqlStatement, (new_playlist_name, playlist_name,))
            connection.commit()
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()

    def add_song_to_playlist(self, song_name, playlist_name):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        try:
            sqlStatement = 'UPDATE SONG SET PLAYLIST_NAME=? WHERE NAME=?'
            cur.execute(sqlStatement, (playlist_name, song_name,))
            connection.commit()
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()

        def update_playlist_number_of_songs(self, playlist_name, number_of_songs):
            connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        try:
            sqlStatement = 'UPDATE PLAYLIST SET NUMBER_OF_SONGS=? WHERE NAME=?'
            cur.execute(sqlStatement, (number_of_songs, playlist_name,))
            connection.commit()
        except Exception as ex:
            print("There Is An Exception.")
            ex.errno
        connection.close()

    def update_playlist_number_of_songs(self, playlist_name, number_of_songs):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        try:
            sqlStatement = 'UPDATE PLAYLIST SET NUMBER_OF_SONGS=? WHERE NAME=?'
            cur.execute(sqlStatement, (number_of_songs, playlist_name,))
            connection.commit()
        except Exception as ex:
            print("There Is An Exception.")
            ex.errno
        connection.close()

    def map_result_set_to_list_of_objects(self, result_set):
        list_of_songs = []
        for row in result_set:
            type_of_my_song = row[6]
            name = row[0]
            featured_artist = row[1]
            if row[2] == None:
                album_title = ''
            else:
                album_title = row[2]
            bands_name = ['', '']
            if row[3] == None:
                if row[4] == None:
                    bands_name = ['', '']
            elif row[4] == None:
                bands_name = [row[3], '']
            else:
                bands_name = [row[3], row[4]]
            if row[5] == None:
                playlist_name = ''
            else:
                playlist_name = row[5]

            song_type = row[6]
            released_date = row[7]
            genre = row[8]
            if row[9] == None:
                lyrics = ''
            else:
                lyrics = row[9]
            duration = row[10]
            if type_of_my_song == 'Single' or type_of_my_song == 'single':
                """
                my_song = Song(row[0], row[1], [row[3], row[4]],
                               row[5], row[6], row[7], row[8], row[9], row[10])"""
                my_song = Song(name, featured_artist, bands_name, playlist_name,
                 song_type, released_date, genre, lyrics, duration)
            else:
                my_song = InAlbum(name, featured_artist, album_title, bands_name, playlist_name,
                 song_type, released_date, genre, lyrics, duration)
            list_of_songs.append(my_song)
        return list_of_songs