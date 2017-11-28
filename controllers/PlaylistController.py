import sqlite3
import errno

from controllers.SongController import SongController


class PlaylistController:
    'This is The Controller of Playlist Model'

    def add_playlist(self, playlist):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        try:
            sqlStatement = 'INSERT INTO PLAYLIST(NAME, DESCRIPTION, NUMBER_OF_SONGS) VALUES(?,?,?)'
            cur.execute(sqlStatement, (playlist.get_name(),
                                       playlist.get_description(), playlist.get_number_of_songs(),))
            connection.commit()
        except Exception as ex:
            print("There Is An Exception.")
            ex.errno
        connection.close()

    def delete_playlist(self, playlist_name):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        try:
            songController = SongController()
            songController.delete_songs_by_playlist(playlist_name)
            sqlStatement = 'DELETE FROM PLAYLIST WHERE NAME=?'
            cur.execute(sqlStatement, (playlist_name,))
            connection.commit()
        except Exception as ex:
            print("There Is An Exception.")
            ex.errno
        connection.close()

    def get_playlist(self, playlist_name):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        rs = None
        try:
            connection.row_factory = sqlite3.Row
            sqlStatement = 'SELECT * FROM SONG WHERE NAME=?'
            cur.execute(sqlStatement, (playlist_name,))
            rs = cur.fetchall()
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()
        return rs

    def get_all_playlists(self):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        rs = None
        try:
            connection.row_factory = sqlite3.Row
            sqlStatement = 'SELECT * FROM PLAYLIST'
            cur.execute(sqlStatement)
            rs = cur.fetchall()
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()
        return rs
