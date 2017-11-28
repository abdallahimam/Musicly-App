'This is the module of view for the user interface'

import sqlite3
import errno
import os
import pygame

from models.Playlist import Playlist
from models.Song import Song
from models.InAlbum import InAlbum
from models.Album import Album
from models.Band import Band
from models.Artist import Artist

from controllers.PlaylistController import PlaylistController
from controllers.SongController import SongController
from controllers.AlbumController import AlbumController
from controllers.BandController import BandController
from controllers.ArtistController import ArtistController

# controllers
playlist_controller = PlaylistController()
artist_controller = ArtistController()
album_controller = AlbumController()
song_controller = SongController()

list_of_all_songs = []
list_of_all_albums = []
list_of_all_artists = []
list_of_all_playlists = []
current_palylist_songs = []


def back_to_home():
    'back to the main view'
    main()


def view_song(song):
    'view the song'
    print('\n')
    print('    {:20}{}'.format('Name:', song.get_name()))
    print('    {:20}{}'.format(
        'Featured Artist:', song.get_featured_artist()))
    print('    {:20}{}'.format('Released Date:', song.get_released_date()))
    print('    {:20}{}'.format('Genre:', song.get_genre()))
    print('    {:20}{}'.format('Duration:', song.get_duration()))
    print('    {:20}{}'.format('Song Type:', song.get_type()))
    if song.get_type() == 'Single':
        print('    {:20}'.format('Album Name:'))
        if song.get_band() == None:
            print('    {:20}'.format('Band:'), end='')
        else:
            print('    {:20}'.format('Band:'), end='')
            if len(song.get_band()) == 0:
                print()
            if len(song.get_band()) == 1:
                print(song.get_band()[0])
            else:
                print(song.get_band()[0], ' / ', song.get_band()[1])
        if song.get_playlist_name() == None:
            print('    {:20}'.format('Playlist:'))
        else:
            print('    {:20}{}'.format(
                'Playlist Name:', song.get_playlist_name()))
        if song.get_genre() == None:
            print('    {:20}'.format('Lyrics:'))
        else:
            print('    {:20}{}'.format('Lyrics:', song.get_genre()))
        print('\n')
    else:
        if song.get_band() == None:
            print('    {:20}'.format('Band:'), end='')
        else:
            print('    {:20}'.format('Band:'), end='')
            if len(song.get_band()) == 0:
                print()
            if len(song.get_band()) == 1:
                print(song.get_band()[0])
            else:
                print(song.get_band()[0], ' / ', song.get_band()[1])
        if song.get_album() == None:
            print('    {:20}'.format('Album:'))
        else:
            print('    {:20}{}'.format('Album Name:', song.get_album()))
        if song.get_playlist_name() == None:
            print('    {:20}'.format('Playlist:'))
        else:
            print('    {:20}{}'.format(
                'Playlist Name:', song.get_playlist_name()))
        if song.get_genre() == None:
            print('    {:20}'.format('Lyrics:'))
        else:
            print('    {:20}{}'.format('Lyrics:', song.get_genre()))
        print('\n')
    return


def view_playlist_songs(playlist_name):
    'this is the view to show playlist songs'
    list_of_songs = song_controller.get_songs_by_playlist(playlist_name)
    print('do yo view it sorted or not')
    print('1. sorted.                 2.not sorted')
    choice = int(input('Chooce: '))
    if (choice == 1):
        print('1. Sort by name.                             2. Sort by artist')
        print('3. Sort by band.                             4. Sort by genre')
        print('5. Sort by released date.')
        choice = int(input('Chooce the sort attribute: '))
        print("1. Ascending Order.           2. Descending Order.")
        ascending = int(input('Chooce the sort type: '))
        if choice == 1:
            if ascending == 1:
                sorted_list_of_songs = sorted(list_of_songs, key=lambda song: song.get_name())
            else:
                sorted_list_of_songs = sorted(list_of_songs, key=lambda song: song.get_name(), reverse=True)
        elif choice == 2:
            if ascending == 1:
                sorted_list_of_songs = sorted(list_of_songs, key=lambda song: song.get_featured_artist())
            else:
                sorted_list_of_songs = sorted(list_of_songs, key=lambda song: song.get_featured_artist(), reverse=True)
        elif choice == 3:
            if ascending == 1:
                sorted_list_of_songs = sorted(list_of_songs, key=lambda song: song.get_band())
            else:
                sorted_list_of_songs = sorted(list_of_songs, key=lambda song: song.get_band(), reverse=True)
        elif choice == 4:
            if ascending == 1:
                sorted_list_of_songs = sorted(list_of_songs, key=lambda song: song.get_genre())
            else:
                sorted_list_of_songs = sorted(list_of_songs, key=lambda song: song.get_genre(), reverse=True)
        elif choice == 5:
            if ascending == 1:
                sorted_list_of_songs = sorted(list_of_songs, key=lambda song: song.get_released_date())
            else:
                sorted_list_of_songs = sorted(list_of_songs, key=lambda song: song.get_released_date(), reverse=True)
        list_of_songs = sorted_list_of_songs
        """for song in sorted_list_of_songs:
            print('    {:40} Duration:{:8}'.format(song.get_name(), song.get_duration()))"""

    print('{:^60}'.format('Welcome To Our Musicly.'))
    print(playlist_name)
    print('Number of songs: ', len(list_of_songs))
    print()
    print('{:15} {:20} {:10} {:15} {:15} {:15} {:15}'.format('Name', 'Artist', 'Genre', 'Released Date', 'Duration', 'Band 1', 'Band 2'))
    for song in list_of_songs:
        print('{:15} {:20} {:10} {:15} {:15} {:15} {:15}'.format(song.get_name(),
              song.get_featured_artist(), song.get_genre(), song.get_released_date(),
              song.get_duration(), song.get_bands_name()[0], song.get_bands_name()[1]))

    print()
    print('1. View specific song information.           2. delete a song.')
    print('3. play song.                                4. back to home.')

    choice = int(input('choose: '))
    if choice == 1:
        while True:
            song_name = input('Choose the song: ')
            found = False
            viewed_song = None
            for song in list_of_songs:
                if song_name == song.get_name():
                    found = True
                    viewed_song = song
                    break
            if found == True:
                view_song(viewed_song)
                break
            else:
                print('Invalid song name!!.   try again.')
        view_playlist_songs(playlist_name)
    elif choice == 2:
        while True:
            song_name = input('Choose the song: ')
            found = False
            viewed_song = None
            for song in list_of_songs:
                if song_name == song.get_name():
                    found = True
                    viewed_song = song
                    break
            if found == True:
                song_controller.delete_song(song_name)
                break
            else:
                print('Invalid song name!!.   try again.')
        view_playlist_songs(playlist_name)
    elif choice == 3:
        while True:
            song_name = input('Choose the song: ')
            found = False
            for song in list_of_songs:
                if song_name == song.get_name():
                    found = True
                    break
            if found == True:
                play_song(song_name)
                break
            else:
                print('Invalid song name!!.   try again.')
        #view_playlist_songs(playlist_name)
    elif choice == 4:
        back_to_home()
    else:
        print('Invalid song name!!.   try again.')
    return


def add_playlist(playlist_name, playlist_description):
    playlist = Playlist(playlist_name, playlist_description, None, 0)
    playlist_controller.add_playlist(playlist)
    view_playlists()


def delete_playlist(playlist_name):
    'playlist function to delete playlist from view and then from database'
    playlist_controller.delete_playlist(playlist_name)
    view_playlists()


def view_playlists():
    'view playlist function'
    result = playlist_controller.get_all_playlists()
    print('{:^60}'.format('Welcome To Our Musicly.'))
    print('Playlists:')
    for row in result:
        print('    {:40}'.format(row[0]), end='')
        if row[-1] == None or row[-1] == 0:
            print(' Tracks/Songs:{:^6}'.format('Empty'))
        else:
            print(' Tracks/Songs:{:^4}'.format(row[-1]))
        list_of_all_playlists.append(Playlist(row[0], row[1], row[2], None))
    print('\n')
    print('1.View Playlist                    2.Back To Home')
    print('3.Add Playlist                     4.Delete Playlist')
    choice = int(input('Enter Your Choice: '))
    if choice == 1:
        playlist_name = input('Enter Playlist Name: ')
        for row in result:
            if row[0] == playlist_name:
                view_playlist_songs(playlist_name)
                break
    elif choice == 2:
        back_to_home()
    elif choice == 3:
        playlist_name = input('Enter Playlist Name: ')
        found = False
        for row in result:
            if row[0] == playlist_name:
                found = True
                break
        if found == False:
            playlist_description = input('Enter Playlist Description: ')
            add_playlist(playlist_name, playlist_description)
    elif choice == 4:
        playlist_name = input('Enter Playlist Name: ')
        found = False
        for row in result:
            if row[0] == playlist_name:
                found = True
                break
        if found == True:
            delete_playlist(playlist_name)
    return


def play_all_songs(list_of_songs):
    return


def view_artist_songs(artist_name):
    list_of_songs = song_controller.get_songs_by_artist(artist_name)
    print('{:^60}'.format('Welcome To Our Musicly.'))
    print(artist_name)
    print(len(list_of_songs))
    print()
    for song in list_of_songs:
        print('    {:40} Duration:{:8}'.format(song.get_name(), song.get_duration()))
    print()
    print('1. View specific song information.            2. delete a song.')
    print('3. play song.                                 4. back to home.')
    print('5. Play all songs.')
    choice = int(input('choose: '))
    if choice == 1:
        song_name = input('Choose the song: ')
        found = False
        viewed_song = None
        for song in list_of_songs:
            if song_name == song.get_name():
                found = True
                viewed_song = song
                break
        if found == True:
            view_song(viewed_song)
        else:
            print('Invalid song name!!.   try again.')
        view_artist_songs(artist_name)
    elif choice == 2:
        song_name = input('Choose the song: ')
        found = False
        for song in list_of_songs:
            if song_name == song.get_name():
                found = True
                break
        if found == True:
            song_controller.delete_song(song_name)
        else:
            print('Invalid song name!!.   try again.')
        view_artist_songs(artist_name)
    elif choice == 3:
        song_name = input('Choose the song: ')
        found = False
        for song in list_of_songs:
            if song_name == song.get_name():
                found = True
                break
        if found == True:
            play_song(song_name)
        else:
            print('Invalid song name!!.   try again.')
        view_artist_songs(artist_name)
    elif choice == 4:
        back_to_home()
    elif choice == 5:
        play_all_songs(list_of_songs)
        view_artist_songs(artist_name)
    else:
        print('Invalid song name!!.   try again.')
        view_artist_songs(artist_name)
    return


def add_new_artist(artist_name):
    date_of_birth = input('Enter date of birth: ')
    artist = Artist(artist_name, date_of_birth)
    artist_controller.add_artist(artist)
    view_artists()


def delete_artist(artist_name):
    artist_controller.delete_artist(artist_name)
    view_artists()


def view_artists():
    'view playlist function'
    result = artist_controller.get_all_artists()
    print('\nArtists:')
    for artist in result:
        print(artist.get_name())
    print()
    print('1.View Artist                      2.Back To Home')
    print('3.Add Artist                       4.Delete Artist')
    choice = int(input('Enter Your Choice: '))
    if choice == 1:
        artist_name = input('Enter Artist Name: ')
        found = False
        for artist in result:
            if artist.get_name() == artist_name:
                found = True
                break
        if found == True:
            view_artist_songs(artist_name)
    elif choice == 2:
        back_to_home()
    elif choice == 3:
        artist_name = input('Enter Artist Name: ')
        found = False
        for artist in result:
            if artist.get_name() == artist_name:
                found = True
                break
        if found == False:
            add_new_artist(artist_name)
        view_artists()
    elif choice == 4:
        artist_name = input('Enter Artist Name: ')
        found = False
        for artist in result:
            if artist.get_name() == artist_name:
                found = True
                break
        if found == True:
            delete_artist(artist_name)
        view_artists()
    return


def view_album_songs(album_name):
    list_of_songs = song_controller.get_songs_by_album(album_name)
    print('{:^60}'.format('Welcome To Our Musicly.'))
    print(album_name)
    print(len(list_of_songs))
    print('\n')
    for song in list_of_songs:
        print('    {:40} Duration:{:8}'.format(song.get_name, song.get_duration()))

    print('\n')
    print('1. View specific song information.            2. delete a song.')
    print('3. play song.                                 4. back to home.')
    print('5. Play all songs.')
    choice = int(input('choose: '))
    if choice == 1:
        while True:
            song_name = input('Choose the song: ')
            found = False
            viewed_song = None
            for song in list_of_songs:
                if song_name == song.get_name():
                    found = True
                    viewed_song = song
                    break
            if found == True:
                view_song(viewed_song)
                break
            else:
                print('Invalid song name!!.   try again.')
    elif choice == 2:
        while True:
            song_name = input('Choose the song: ')
            found = False
            for song in list_of_songs:
                if song_name == song.get_name():
                    found = True
                    break
            if found == True:
                song_controller.delete_song(song_name)
                break
            else:
                print('Invalid song name!!.   try again.')
    elif choice == 3:
        while True:
            song_name = input('Choose the song: ')
            found = False
            for song in list_of_songs:
                if song_name == song.get_name():
                    found = True
                    break
            if found == True:
                play_song(song_name)
                break
            else:
                print('Invalid song name!!.   try again.')
    elif choice == 4:
        back_to_home()
    else:
        play_all_songs(list_of_songs)
        print('Invalid song name!!.   try again.')
    return


def add_new_album(album_title):
    #date_of_birth = input('Enter date of birth: ')
    album = Album(album_title, None, 0, None)
    album_controller.add_album(album)
    view_albums()
    return


def delete_album(album_title):
    album_controller.delete_album(album_title)
    view_albums()


def view_albums():
    'view albums function'
    result = album_controller.get_all_albums()
    for album in result:
        print('{:20}:  {}'.format(album.get_title(), album.get_number_of_songs()))
    print()
    print('1.View Album                       2.Back To Home')
    print('3.Add Album                        4.Delete Artist')
    choice = int(input('Enter Your Choice: '))
    if choice == 1:
        album_name = input('Enter Album Title: ')
        found = False
        for artist in result:
            if artist == album_name:
                found = True
                break
        if found == True:
            view_album_songs(album_name)
    elif choice == 2:
        back_to_home()
    elif choice == 3:
        album_name = input('Enter Album Title: ')
        found = False
        for album in result:
            if album.get_title() == album_name:
                found = True
                break
        if found == False:
            add_new_album(album_name)
    elif choice == 4:
        album_name = input('Enter Album Title: ')
        found = False
        for album in result:
            if album.get_title() == album_name:
                found = True
                break
        if found == True:
            delete_album(album_name)
    return


def add_new_song(song_name):
    song_featured_artist = input('Enter song artist: ')
    song_released_date = input('Enter song released date: ')
    song_duration = input('Enter song duration: ')
    song_band_name_1 = input('Enter song band name 1: ')
    song_band_name_2 = input('Enter song band name 2: ')
    bands_name = [song_band_name_1, song_band_name_2]
    song_type = input('Enter song type(Single/In Album): ')
    song_genre = input('Enter song genre: ')
    song_lyrics = input('Enter song lyrics: ')
    song_playlist = input('Enter song playlist name: ')
    new_song = None
    if song_type == 'Single' or song_type == 'single':
        new_song = Song(song_name, song_featured_artist, bands_name, song_playlist,
                        song_type, song_released_date, song_genre, song_lyrics, song_duration)
    else:
        song_album_title = input('Enter song album title: ')
        new_song = InAlbum(song_name, song_featured_artist, song_album_title, bands_name, song_playlist,
                           song_type, song_released_date, song_genre, song_lyrics, song_duration)
    result = song_controller.add_song(new_song)
    if result == 'error':
        'Error:  Please enter a valid song features.'
    view_library()


def view_library():
    'view playlist function'
    list_of_songs = song_controller.get_all_songs()
    for song in list_of_songs:
        print('    {:20} {:20}{}'.format(
            song.get_name(), 'Duration:', song.get_duration()))
    print('1.View song                          2.Back To Home')
    print('3.Add new song                       4.Delete song')
    print('5. Play song                         6.Play all songs')
    print()
    choice = int(input('Enter Your Choice: '))
    if choice == 1:
        song_name = input('Enter song name: ')
        found = False
        for song in list_of_songs:
            if song.get_name() == song_name:
                found = True
                break
        if found == True:
            view_song(song_name)
    elif choice == 2:
        back_to_home()
    elif choice == 3:
        song_name = input('Enter new song: ')
        found = False
        for song in list_of_songs:
            if song.get_name() == song_name:
                found = True
                break
        if found == False:
            add_new_song(song_name)
    elif choice == 4:
        song_name = input('Choose the song: ')
        found = False
        for song in list_of_songs:
            if song_name == song.get_name():
                found = True
                break
        if found == True:
            song_controller.delete_song(song_name)
        else:
            print('Invalid song name!!.   try again.')
        view_library()
    elif choice == 5:
        song_name = input('Choose the song: ')
        found = False
        for song in list_of_songs:
            if song_name == song.get_name():
                found = True
                break
        if found == True:
            play_song(song_name)
        else:
            print('Invalid song name!!.   try again.')
    elif choice == 6:
        play_all_songs(list_of_songs)
    else:
        print('Invalid Input!')


def play_song(song_name):
    'Play certain song'
    path_name = "songs/"
    os.startfile("C:\\Users\\Abdullah\\Desktop\\CPL2\\songs\\" + song_name + ".mp3"  )
    '''
    song_name = path_name + song_name + '.mp3'
    if os.path.exists(song_name):
        pygame.mixer.init()
        pygame.mixer.music.load(song_name)
        pygame.mixer.music.play()
    else:
        print("Can't open '%s' because it not exists !!" % song_name)
    '''
    view_library()


def pause_song():
    pygame.mixer.music.stop()


def play_album_songs(album_name):
    'Play certain album'
    connection = sqlite3.connect("musicly.db", timeout=100)
    cur = connection.cursor()
    try:
        sql_statement = "SELECT NAME FROM SONG WHERE ALBUM_TITLE = ?"
        cur.execute(sql_statement, (album_name,))
        songs = cur.fetchall()
        for song in songs:
            song = '' .join(song)
            play_song(str(song))
    except Exception as ex:
        print("There Is An Exception with Play Album Songs")
    connection.close()


def play_playlist_songs(playlist_name):
    'play certain playlist'
    connection = sqlite3.connect("musicly.db", timeout=100)
    cur = connection.cursor()
    try:
        sql_statement = "SELECT NAME FROM SONG WHERE PLAYLIST_NAME = ?"
        cur.execute(sql_statement, (playlist_name,))
        songs = cur.fetchall()
        for song in songs:
            song = '' .join(song)
            play_song(str(song))
    except Exception as ex:
        print("There Is An Exception with Play Playlist Songs")
    connection.close()


def play_artist_songs(artist_name):
    'play certain playlist'
    connection = sqlite3.connect("musicly.db", timeout=100)
    cur = connection.cursor()
    try:
        sql_statement = "SELECT NAME FROM SONG WHERE FEATURED_ARTIST = ?"
        cur.execute(sql_statement, (artist_name,))
        songs = cur.fetchall()
        for song in songs:
            song = '' .join(song)
            play_song(str(song))
    except Exception as ex:
        print("There Is An Exception with Play Artist Songs")
    connection.close()


def play_genre_songs(genre_name):
    'play a certain genre songs'
    connection = sqlite3.connect("musicly.db", timeout=100)
    cur = connection.cursor()
    try:
        sqlStatement = "SELECT NAME FROM SONG WHERE GENRE = ?"
        cur.execute(sqlStatement, (genre_name,))
        songs = cur.fetchall()
        for song in songs:
            song = '' .join(song)
            play_song(str(song))
    except Exception as ex:
        print("There Is An Exception with Play Artist Songs")
    connection.close()


def main():
    'main function'
    print('{:^60}'.format('Welcome To Our Musicly.'))
    print("  1. Playlists.")
    print("  2. Artists.")
    print("  3. Albums.")
    print("  4. Library.")
    choice = int(input('Enter You Choice: '))
    if choice == 1:
        view_playlists()
    elif choice == 2:
        view_artists()
    elif choice == 3:
        view_albums()
    elif choice == 4:
        view_library()
    else:
        print('Incorrect Input!\n')


main()
