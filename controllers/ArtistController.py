import sqlite3
from controllers.SongController import SongController
from models.Artist import Artist

class ArtistController:
    'this is the controlle of the Artist Model'

    def add_artist(self, artist):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        try:
            sql_statement = 'INSERT INTO ARTIST(NAME, BIRTH_OF_DATE) VALUES(?,?)'
            cur.execute(sql_statement, (artist.get_name(),
                                        artist.get_birth_of_date(),))
            connection.commit()
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()

    def delete_artist(self, artist_name):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        try:
            song_controller = SongController()
            song_controller.delete_songs_by_artist(artist_name)
            sql_statement = 'DELETE FROM ARTIST WHERE NAME=?'
            cur.execute(sql_statement, (artist_name,))
            connection.commit()
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()

        def get_all_artists(self):
            connection = sqlite3.connect("musicly.db", timeout=100)
        cur = connection.cursor()
        rs = None
        try:
            connection.row_factory = sqlite3.Row
            sql_statement = 'SELECT * FROM ARTIST'
            cur.execute(sql_statement)
            rs = cur.fetchall()
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()
        return rs

    def get_artist(self, artist_name):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        rs = None
        try:
            connection.row_factory = sqlite3.Row
            sql_statement = 'SELECT * FROM ARTIST WHERE NAME=?'
            cur.execute(sql_statement, (artist_name,))
            rs = cur.fetchall()
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()
        return rs

    def get_all_artists(self):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        rs = None
        try:
            connection.row_factory = sqlite3.Row
            sql_statement = 'SELECT * FROM ARTIST'
            cur.execute(sql_statement)
            rs = cur.fetchall()
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()
        list_of_artists =[]
        for row in rs:
            list_of_artists.append(Artist(row[0], row[1]))
        return list_of_artists
