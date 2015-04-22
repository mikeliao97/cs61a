def counting_song():
    song = [1]
    while True:
        yield song
        song = song[0:len(song)//2 + 1] + [song[len(song)//2] + 1] + song[0:len(song)//2 + 1][::-1]
