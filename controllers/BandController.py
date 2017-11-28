import sqlite3

from controllers.SongController import SongController

class BandController:
    'this is the controller of Band Model'
    def add_band(self, band):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        try:
            sqlStatement = 'INSERT INTO BAND(NAME, ARTIST_NAME) VALUES(?,?)'
            for artist in band.get_list_of_songs():
                cur.execute(sqlStatement, (band.get_name(), artist.get_name(),))
            connection.commit()
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()

    def delete_band(self, band):
        connection = sqlite3.connect("musicly.db")
        cur = connection.cursor()
        try:
            songController = SongController()
            songController.delete_songs_by_band(band.get_name())
            sqlStatement = 'DELETE FROM BAND WHERE NAME=?'
            cur.execute(sqlStatement, (band.get_name(),))
            connection.commit()
        except Exception as ex:
            print("There Is An Exception.")
        connection.close()
