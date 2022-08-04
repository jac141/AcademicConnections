import lyricsgenius
token = "8WDFe1MPF14RdPbH2eSGcbRu6XYTQ0iRB1TZvpaYTwOw7OVeBrKGCDzYCcn7yd2V"
genius = lyricsgenius.Genius(token)
terminalApplicationStatus = True

def printhelp():
    print("-help = Displays a list of commands with its appropriate syntax and its function")
    print("-stop = Shuts down terminal application")
    print(
        "-listallsongs (artist) = [RESOURCE DEMANDING COMMAND] Provides a list of all of a given artists' songs by relevance")
    print(
        "-listallsongsalpha (artist) = [RESOURCE DEMANDING COMMAND] Provides a list of all of a given artists' songs by alphanumerical order")
    print(
        "-listsongs (number of songs) (artist) = Provides a list of a given length of a given artists' songs by relevance")
    print(
        "-listsongsalpha (number of songs) (artist) = Provides a list of a given length of a given artists' songs by alphanumerical order")
    print("-searchsong (lyrics) = Provides the possible names of a song given lyrics")
    print("-lyrics (song) = Displays the lyrics of a given song")

print("< MusicGenie >")
print()
print("A terminal based music information database")
print("Developed By ADRIAN SIMON")
print("Powered By GENIUS API")
print("Type -help for more information")
print()

while terminalApplicationStatus:
    i = input("")
    ia = []
    try:
        if i == "-help":  # commands
            printhelp()
        elif i == "-stop":
            print("Terminating Application")
            terminalApplicationStatus = False
        elif i[0:14] == "-listallsongs ":
            print(genius.search_artist(i[14:len(i)], max_songs=1000).songs)
            print()
        elif i[0:19] == "-listallsongsalpha ":
            print(genius.search_artist(i[19:len(i)], max_songs=1000, sort="title").songs)
            print()
        elif i[0:11] == "-listsongs ":
            ia = i.split()
            for x in range(len(ia)):
                if x > 2:
                    ia[2] += " " + ia[x]
            print(genius.search_artist(ia[2], max_songs=int(ia[1])).songs)
            print()
        elif i[0:16] == "-listsongsalpha ":
            ia = i.split()
            for x in range(len(ia)):
                if x > 2:
                    ia[2] += " " + ia[x]
            print(genius.search_artist(ia[2], max_songs=int(ia[1]), sort="title").songs)
            print()
        elif i[0:12] == "-searchsong ":
            requestArr = genius.search_lyrics(i[12:len(i)])
            print("Potential songs containing:" + "'" + i[12:len(i)] + "':")
            for hit in requestArr['sections'][0]['hits']:
                print(hit['result']['title'] + " - " + hit['result']['artist_names'])
        elif i[0:8] == "-lyrics ":
            lyrics = []
            songs = genius.search_songs(i[8:len(i)])
            singleSongIndex = 0
            for song in songs['hits']:
                if singleSongIndex == 0:
                    url = song['result']['url']
                    song_lyrics = genius.lyrics(song_url=url)
                    print(song_lyrics)
                    singleSongIndex = 1
        else:
            print("Error")
    except:
        print("An exception occurred")
        print("Servers are having trouble processing your request")
        print("Please try again later")

