import random

from datetime import date

class Media:
    def __init__(self, title, release_year, genre):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.views = 0

    def play(self, views):
        self.views += views

    def __str__(self):
        return f"{self.title} ({self.release_year}) - {self.genre} ({self.views}) odtworzeń"
    
class Movie(Media):
    def __str__(self):
        return F"{self.title} ({self.release_year})"
    
class Series(Media):
    def __init__(self, title, release_year, genre, season, epsiode):
        super().__init__(title, release_year, genre)
        self.season = season
        self.episode = epsiode

    def play(self, views):
        super().play(views)
        self.episode += 1

    def __str__(self):
        season_str = str(self.season).zfill(2)
        episode_str = str(self.episode).zfill(2)
        return f"{self.title} S{season_str}E{episode_str}"
    
class MediaLibrary:
    def __init__(self):
        self.library = []

    def add_media(self, media):
        self.library.append(media)

    def play_random(self):
        random_media = random.choice(self.library)
        random_views = random.randint(1, 100)
        random_media.play(random_views) 

    def generate_views(self, times = 1):
        for _ in range(times):
            self.play_random()
            

def create_library():
    library = MediaLibrary()

    # Dodaj filmy
    movies = [
        Movie("Pulp Fiction", 1994, "Crime"),
        Movie("Forrest Gump", 2994, "Drama"),
        Movie("The Shawshank Redemption", 1994, "Drama"),
        Movie("The Dark Knight", 2008, "Action"),
        Movie("Inception", 2010,  "Sci-Fi")
    ]

    # Dodaj seriale
    series = [
        series("Friens", 1994, "Comedy", 1, 1),
        series("Breaking Bad", 2008, "Crime", 1, 1),
        series("Game of Thrones", 2011, "Fantasy", 1, 1),
        series("Stranger Things", 2016, "Sci-Fi", 1, 1),
        series("The Mandalorian", 2019, "Sci-Fi", 1, 1)        
    ]

    # Dodaj media do biblioteki
    library.library.extend(movies)
    library.library.extend(series)

    return library



    
    
