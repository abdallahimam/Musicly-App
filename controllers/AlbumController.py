import sqlite3
from controllers.SongController import SongController


class AlbumController:
    'This class is The controller of Album(add/remove/....)'

    def add_album(self, album):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        try:
            sql_statement = 'INSERT INTO ALBUM(TITLE, NUMBER_OF_SONGS) VALUES(?,?)'
            cur.execute(sql_statement, (album.get_title(),
                                        album.get_number_of_songs(),))
            connection.commit()
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()

    def delete_album(self, album):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        rs = None
        try:
            song_controller = SongController()
            song_controller.delete_songs_by_album(album.get_title())
            sql_statement = 'DELETE FROM ALBUM WHERE TITLE=?'
            cur.execute(sql_statement, (album.get_title(),))
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()

    def get_album(self, album_title):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        result_sets = None
        try:
            connection.row_factory = sqlite3.Row
            sql_statement = 'SELECT * FROM ALBUM WHERE TITLE=?'
            cur.execute(sql_statement, (album_title,))
            result_sets = cur.fetchall()
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()
        return result_sets

    def get_all_albums(self):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        result_sets = None
        try:
            connection.row_factory = sqlite3.Row
            sql_statement = 'SELECT * FROM ALBUM'
            cur.execute(sql_statement)
            result_sets = cur.fetchall()
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()
        return result_sets
