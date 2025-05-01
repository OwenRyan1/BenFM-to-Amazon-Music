from src.BenFM import get_songs_from_BenFM 
from src.SongList import song_list_generator 
from src.TuneMyMusic import connecting_to_amazon_playlist
import os

#gets paths to files
base_dir = os.path.dirname(os.path.abspath(__file__))
ADDED_SONGS_TXT = os.path.join(base_dir, 'data', 'AddedSongs.txt')
SONG_LIST_TXT = os.path.join(base_dir, 'data', 'SongList.txt')

PLAYLIST_NAME = "BenFM 2025" # MUST BE CREATED FIRST WITH ONE SONG

def main():
    listOfSongs = get_songs_from_BenFM()
    newSongsBool = song_list_generator(listOfSongs, SONG_LIST_TXT, ADDED_SONGS_TXT)
    connecting_to_amazon_playlist(newSongsBool, ADDED_SONGS_TXT, PLAYLIST_NAME)

if __name__ == "__main__":
    main()
