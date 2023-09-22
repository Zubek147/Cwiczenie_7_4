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
        return f"{self.title} ({self.release_year})"
    
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

    def top_titles(self, num_titles, content_type = None):
        sorted_library = sorted(self.library, key = lambda x: x.views, reverse = True) 
        if content_type:
            sorted_library = [media for media in sorted_library if isinstance(media, content_type)]
        return sorted_library[:num_titles]           

    def search(self, title):
        result = [media for media in self.library if title.lower() in media.title.lower()]
        return result
    
    def display_top_titles(self, num_titles):
        current_date = date.today().strftime("%d.%m.%Y")
        print(f"Najpopularniejsze filmy i seriale dnia {current_date}")

        def print_top_media(media_list, title):
            print(f"\nTop 3 najpopularniejsze {title}:")
            for i, media in enumerate(media_list, 1):
                print(f"{i}. {media}")

        top_media = self.top_titles(num_titles)
        for i, media in enumerate(top_media, 1):
            print(f"{i}. {media}")

        top_movies = self.top_titles(num_titles, content_type = Movie)
        print_top_media(top_movies, "filmy")

        top_series = self.top_titles(num_titles, content_type = Series)
        print_top_media(top_series, "seriale")

    def run_generate_views_multiple_times(self, num_times = 10):
        for _ in range(num_times):
            self.generate_views()

    def add_full_season(self, title, release_year, genre, season, num_episodes):
        for episode_number in range(1, num_episodes + 1):
            series = Series(title, release_year, genre, season, episode_number)
            self.add_media(series)

    def get_num_seasons_and_episodes(self, series_title):
        num_seasons = 0
        num_episodes = 0
        for media in self.library:
            if isinstance(media, Series) and media.title.lower() == series_title.lower():
                num_seasons = max(num_seasons, media.season)
                num_episodes += 1
        return num_seasons, num_episodes
    
def create_library():
    library = MediaLibrary()

    # Dodaj filmy
    movies = [
        Movie("Pulp Fiction", 1994, "Crime"),
        Movie("Forrest Gump", 1994, "Drama"),
        Movie("The Shawshank Redemption", 1994, "Drama"),
        Movie("The Dark Knight", 2008, "Action"),
        Movie("Inception", 2010,  "Sci-Fi")
    ]

    # Dodaj seriale
    series = [
        Series("Friens", 1994, "Comedy", 1, 1),
        Series("Breaking Bad", 2008, "Crime", 1, 1),
        Series("Game of Thrones", 2011, "Fantasy", 1, 1),
        Series("Stranger Things", 2016, "Sci-Fi", 1, 1),
        Series("The Mandalorian", 2019, "Sci-Fi", 1, 1)        
    ]

    # Dodaj media do biblioteki
    library.library.extend(movies)
    library.library.extend(series)

    return library

if __name__ == "__main__":
    print("Biblioteka filmów:")
    library = create_library()

    # Wygeneruj odtworzenia
    library.generate_views(10)

    # Wyświetl top 3 najpopularniejszych tytułów
    library.display_top_titles(3)

    # Wyszukaj film lub serial po tytule
    search_title = "Pulp Fiction"
    results = library.search(search_title)
    print(f"\nWyszukiwanie dla \"{search_title}\":")
    for i, media in enumerate(results, 1):
        print(f"{i}. {media}")

    # Wyświetl serial jako string
    series_to_display = Series("Game of Thrones", 2011, "Fantasy", 1, 5)
    print(f"\nSerial jako string: {series_to_display}")
    print()

    # Wyswietl komunikat o liczbie seoznów danego serialu
    series_title_to_check = "Game of Thrones"
    num_seasons, num_episodes = library.get_num_seasons_and_episodes(series_title_to_check)
    print(f"Liczba sezonów dla serialu {series_title_to_check}: {num_seasons}")
    print(f"Liczba odcinków dla serialu {series_title_to_check}: {num_episodes}")

    
    
