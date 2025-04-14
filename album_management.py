class Album:
    def __init__(self, album_name, album_artist, number_of_songs):
        self.album_name = album_name
        self.album_artist = album_artist
        self.number_of_songs = number_of_songs

    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"

albums1 = [
    Album("Thriller", "Michael Jackson", 9),
    Album("25", "Adele", 11),
    Album("Divide", "Ed Sheeran", 12),
    Album("Future Nostalgia", "Dua Lipa", 11),
    Album("After Hours", "The Weeknd", 14)
]

print("Original albums1 list:")
for album in albums1:
    print(album)

albums1.sort(key=lambda a: a.number_of_songs)
print("\nSorted by number of songs:")
for album in albums1:
    print(album)

albums1[0], albums1[1] = albums1[1], albums1[0]
print("\nAfter swapping first two albums:")
for album in albums1:
    print(album)

albums2 = [
    Album("1989", "Taylor Swift", 13),
    Album("DAMN.", "Kendrick Lamar", 14),
    Album("In the Lonely Hour", "Sam Smith", 10),
    Album("Fine Line", "Harry Styles", 12),
    Album("Born to Die", "Lana Del Rey", 15)
]

print("\nOriginal albums2 list:")
for album in albums2:
    print(album)

albums2.extend(albums1)

albums2.append(Album("Dark Side of the Moon", "Pink Floyd", 9))
albums2.append(Album("Oops!... I Did It Again", "Britney Spears", 16))

albums2.sort(key=lambda a: a.album_name)
print("\nSorted albums2 by album name:")
for album in albums2:
    print(album)

for i, album in enumerate(albums2):
    if album.album_name == "Dark Side of the Moon":
        print(f"\n'Dark Side of the Moon' found at index {i}")
        break
