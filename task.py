import random

class Video:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.view = 0  

class Movie(Video):
    def __init__(self, title, year, genre):
        super().__init__(title, year, genre)

    def play(self):
        self.view += 1  

    def __str__(self):
        return f"{self.title}, {self.year}, {self.genre}, Obejrzano: {self.view}"

class Series(Video):
    def __init__(self, title, year, genre, episode, season):
        super().__init__(title, year, genre)
        self.episode = episode
        self.season = season

    def play(self):
        self.view += 1  

    def __str__(self):
        season_str = f"S{self.season:02d}"
        episode_str = f"E{self.episode:02d}"
        return f"{self.title}, {self.year}, {self.genre}, {season_str}{episode_str}, Obejrzenia: {self.view}"


library = [
    Movie(title="Spiderman 1", year=2002, genre="Akcja"),
    Movie(title="Szybcy i Wściekli", year=2001, genre="Akcja"),
    Movie(title="Pacific Rim", year=2013, genre="Sci-Fi"),
    Series(title="Wiedźmin", year=2019, genre="Fantasy", season=1, episode=1),
    Series(title="Cobra Kai", year=2018, genre="Dramat", season=1, episode=1),
    Series(title="Młody Sheldon", year=2017, genre="Komedia", season=1, episode=1)
]


def generate_views():
    for item in library:
        item.view = random.randint(1, 100)  

        
def get_movies():
    sorted_movies = sorted(library, key=lambda x: x.title)
    print("\nFilmy dostępne w bibliotece:")
    for item in sorted_movies:
        if isinstance(item, Movie):
            print(item)

def get_series():
    sorted_series = sorted(library, key=lambda x: x.title)
    print("\nSeriale dostępne w bibliotece:")
    for item in sorted_series:
        if isinstance(item, Series):
            print(item)

def content_type():
    choice = input("Wybierz Filmy lub Seriale ('filmy'/'seriale'): ").lower()

    if choice == "filmy":
        generate_views()  
        get_movies()
    elif choice == "seriale":
        generate_views()  
        get_series()
    else:
        print("Niepoprawny wybór. Wybierz 'filmy' lub 'seriale'.")

def search(search_query):
    results = []
    for item in library:
        if search_query.lower() in item.title.lower():
            results.append(item)

    if results:
        generate_views()  
        print("\nZnalezione tytuły:")
        for result in results:
            print(result)
    else:
        print("\nNie znaleziono żadnych tytułów.")

def top_titles():
    generate_views()
    top_sorted=sorted(library, key=lambda x:x.view, reverse=True)
    print("\nNajpopularniejsze tutuły: ".upper())
    for item in top_sorted:
        if isinstance(item, Video):
            print(item)

def main():
    print("\nBiblioteka filmów i seriali".upper())
    main_choice = input("Wyszukaj/Wybierz/Top: ").lower()
    if main_choice == "wyszukaj":
        search_query = input("Podaj fragment tytułu do wyszukania: ")
        search(search_query)
    elif main_choice == "wybierz":
        content_type()
    elif main_choice=="top":
        top_titles()

    else:
        print("\nNiepoprawny wybór. Wybierz 'wyszukaj' 'wybierz' lub 'top' .")
        main()

main()
