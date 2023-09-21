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
    

    
