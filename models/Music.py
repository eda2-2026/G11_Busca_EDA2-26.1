class music:

    def __init__(self, id, name, artist, genre, year):
        self.id = id
        self.name = name
        self.artist = artist
        self.genre = genre
        self.year = year

    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nArtist: {self.artist}\nGenre: {self.genre}\nYear: {self.year}"