
# coding: utf-8

# In[1]:

import sqlite3
import errno
import os
import pygame



def Play_Song(songName):
    
    pathName = "songs/"
    SongName = pathName + songName
    
    if(os.path.exists(SongName)):    
        pygame.mixer.init()
        pygame.mixer.music.load(SongName)
        pygame.mixer.music.play()
    else:
        print("Can't open '%s' because it not exists !!"  %songName)
    
Play_Song("hip-hop.mp") 


# In[3]:

def Pause_Song():
    pygame.mixer.music.stop()
    
Pause_Song()    


# In[78]:

def Play_Album_Songs(albumName):
    
    connection = sqlite3.connect("musicly.db", timeout=100)
    cur = connection.cursor()    
    
    try:
        sqlStatement = "SELECT NAME FROM SONG WHERE ALBUM_TITLE = ?" 
        cur.execute(sqlStatement, (albumName,))
        songs = cur.fetchall()
        
        for song in songs:            
            song = '' .join(song)
            Play_Song(str(song))
        
    except Exception as ex:
        print("There Is An Exception with Play Album Songs")
        print(ex.errno)
        
       
    connection.close()
    
Play_Album_Songs("The Fox")        


# In[90]:

def Play_Playlist_songs(playlistName):
    
    connection = sqlite3.connect("musicly.db", timeout=100)
    cur = connection.cursor()
    
    try:
        sqlStatement = "SELECT NAME FROM SONG WHERE PLAYLIST_NAME = ?" 
        cur.execute(sqlStatement, (playlistName,))
        songs = cur.fetchall()
        
        for song in songs:            
            song = '' .join(song)
            Play_Song(str(song))
        
    except Exception as ex:
        print("There Is An Exception with Play Playlist Songs")
        print(ex.errno)
        
    connection.close()
    
Play_Playlist_songs("PLaylist 5")    


# In[92]:

def Play_Artist_songs(artistName):
    
    connection = sqlite3.connect("musicly.db", timeout=100)
    cur = connection.cursor()
    
    try:
        sqlStatement = "SELECT NAME FROM SONG WHERE FEATURED_ARTIST = ?" 
        cur.execute(sqlStatement, (artistName,))
        songs = cur.fetchall()
        
        for song in songs:            
            song = '' .join(song)
            Play_Song(str(song))
        
    except Exception as ex:
        print("There Is An Exception with Play Artist Songs")
        print(ex.errno)
        
    connection.close()
    
Play_Artist_songs("Tamer Hosny")    


# In[94]:

def Play_Genre_Songs(genreName):
    
    connection = sqlite3.connect("musicly.db", timeout=100)
    cur = connection.cursor()
    
    try:
        sqlStatement = "SELECT NAME FROM SONG WHERE GENRE = ?" 
        cur.execute(sqlStatement, (genreName,))
        songs = cur.fetchall()
        
        for song in songs:            
            song = '' .join(song)
            Play_Song(str(song))
        
    except Exception as ex:
        print("There Is An Exception with Play Artist Songs")
        print(ex.errno)
        
    connection.close()
    
Play_Genre_Songs("genre1")    


