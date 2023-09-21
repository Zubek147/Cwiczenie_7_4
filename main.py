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
    

