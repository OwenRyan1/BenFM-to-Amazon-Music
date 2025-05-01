""" 
params: 
    newSongList (list) - list of songs found on BenFM from BenFM.py
    SongList_file (str) - location of master song list
    AddedSongs_file (str) - location of newly added songs

summary: 
    goes through songs from BenFM and checks if any are not in the master list of already added songs. 
    then adds any new songs and updates the AddedSongs.txt file that will be used within TuneMyMusic.py

returns:
    songsAdded (bool) - determinate if any new songs were discovered
"""
def song_list_generator(newSongList, SongList_file, AddedSongs_file):

    with open(SongList_file, 'a+') as SongList_txt:
        SongList_txt.seek(0)
        list_txt = SongList_txt.readlines()

        # Removing newline characters
        SongList_listed_txt = [i.strip() for i in list_txt]

        #correcting format (fixed weird formatting in BenFM)
        overall_list = []
        skip = True
        for i in range(len(newSongList)):
            if skip == False:
                skip = True
                continue
            elif newSongList[i] == "":
                skip = False
                continue
            elif newSongList[i] in overall_list:
                continue
            else:
                overall_list.append(newSongList[i].strip()) #fixes songs with space after name

        #AddedSongs_txt = open('../data/AddedSongs.txt','w')

        #tracker to see if new songs are found
        songsAdded = False  

        with open(AddedSongs_file, 'w') as AddedSongs_txt:
            
            #checking if song already in txt fil
            for i in overall_list:
                if i in SongList_listed_txt:
                    continue
                else:
                    #adds only non dups to then add to playlist
                    AddedSongs_txt.write(i)
                    AddedSongs_txt.write('\n')
                    songsAdded = True

                    #to show what songs were added
                    print(i)
                    
                    #writes to master log to always check for dups
                    SongList_txt.write(i)
                    SongList_txt.write('\n')

            return songsAdded
