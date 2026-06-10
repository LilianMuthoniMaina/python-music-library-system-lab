
  


class Song:
    # Class Attributes (Shared global state)
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        # Instance Attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Dynamically reference the class to avoid hardcoding "Song"
        cls = self.__class__
        
        # 1. Increment count
        cls.count += 1
        
        # 2. Add unique genre
        if genre not in cls.genres:
            cls.genres.append(genre)
            
        # 3. Add unique artist
        if artist not in cls.artists:
            cls.artists.append(artist)
            
        # 4. Update genre counts
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1
        
        # 5. Update artist counts
        cls.artists_count[artist] = cls.artists_count.get(artist, 0) + 1