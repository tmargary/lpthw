class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

billie = Song(["Don't you know I'm no good for you?",
    "I've learned to lose you, can't afford to",
    "Tore my shirt to stop you bleedin'",
    "But nothin' ever stops you leavin'"])

finneas = Song(["Let's fall in love for the night",
    "And forget in the mornin'",
    "Play me a song that you like",
    "You can bet I'll know every line"])

billie.sing_me_a_song()

finneas.sing_me_a_song()

class person(object):
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

TM = person('Tigran', 'Margaryan', 25)
print(TM.first_name)
