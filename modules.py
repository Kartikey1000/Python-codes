#import artists
#import artwork
#from Museum.artwork import get_artworks
#from Museum.artists import get_artists
from Museum.artists import get_artists

def main():
    artist=input("Artist: ")
    #artworks=get_artworks(query=artwork,limit=3)
    artists=get_artists(query=artist,limit=3)
    for artist in artists:
        print(f"-> {artist}")


main()