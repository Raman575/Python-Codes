""" 

Objects and attributes=Track, Artists, Duration
 
 
"""
class Songs:
    def __init__(self, track="", artist=0, duration=4.0):
        self.track = track
        self.artist = artist
        self.duration = duration
    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        print("TRACK:", self.track)
        
        print("ARTIST:", self.artist)
        
        print("DURATION:", self.duration)
        
        print("~~~~~~~~~~~~~~~~~~~~~~~~")

song1 = Songs("Udd Jaa Kaale Kaava", "Udit Narayan, Mithoon,Uttam Singh,Alka Yagnik", "04:48")

song2 = Songs("Gustakhiyan", "Gurnam Bhullar", "03:39")

song3 = Songs("Desperado", "Raghav,Tesher", "04:07")

song4 = Songs("Chorni", "DIVINE, Sidhu Moose Wala", "03:01")

song5 = Songs("Kasol", "Mani Longia, Starboy X", "02:40")

song6 = Songs("Car Keys", "Alok, Ava Max", "02:26")

song7 = Songs("Yahi Toh Hai Zindagi", "Suhit Abhyankar", "03:14")

song8 = Songs("Check It Out", "Parmish Verma, Paradox", "03:15")

song9 = Songs("Speed Drive", "Charli XCX", "01:57")

song10 = Songs("Yaar Ka Sataya Hua Hai", "B Praak, Jaani, Nawazuddin Siddiqui, Shehnaz Kaur Gill", "04:28")

print(vars(song1))
print(vars(song2))
print(vars(song3))


print(vars(song4))

print(vars(song5))
print(vars(song6))

print(vars(song7))

print(vars(song8))

print(vars(song9))

print(vars(song10))

song1.show()

song2.show()

song3.show()

song4.show()

song5.show()
song6.show()
song7.show()
song8.show()
song9.show()
song10.show()