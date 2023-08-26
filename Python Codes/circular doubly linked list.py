class Songs:
    def __init__(self, track="", artist="", duration=""):
        self.track = track
        self.artist = artist
        self.duration = duration
        self.next = None
        self.previous = None

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        print("TRACK:", self.track)
        print("ARTIST:", self.artist)
        print("DURATION:", self.duration)
        print("CURRENT:", self, "NEXT:", self.next, "PREVIOUS:", self.previous)
        print("~~~~~~~~~~~~~~~~~~~~~~~~")


def main():
    song1 = Songs("Udd Jaa Kaale Kaava", "Udit Narayan, Mithoon, Uttam Singh, Alka Yagnik", "04:48")
    song2 = Songs("Gustakhiyan", "Gurnam Bhullar", "03:39")
    song3 = Songs("Desperado", "Raghav, Tesher", "04:07")
    song4 = Songs("Chorni", "DIVINE, Sidhu Moose Wala", "03:01")
    song5 = Songs("Kasol", "Mani Longia, Starboy X", "02:40")
    song6 = Songs("Car Keys", "Alok, Ava Max", "02:26")
    song7 = Songs("Yahi Toh Hai Zindagi", "Suhit Abhyankar", "03:14")
    song8 = Songs("Check It Out", "Parmish Verma, Paradox", "03:15")
    song9 = Songs("Speed Drive", "Charli XCX", "01:57")
    song10 = Songs("Yaar Ka Sataya Hua Hai", "B Praak, Jaani, Nawazuddin Siddiqui, Shehnaz Kaur Gill", "04:28")

    # Create a linked list
    # forward direction
    song1.next = song2
    song2.next = song3
    song3.next = song4
    song4.next = song5
    song5.next = song6
    song6.next = song7
    song7.next = song8
    song8.next = song9
    song9.next = song10
    song10.next = song1

    song1.previous = song10
    song2.previous = song1
    song3.previous = song2
    song4.previous = song3
    song5.previous = song4
    song6.previous = song5
    song7.previous = song6
    song8.previous = song7
    song9.previous = song8
    song10.previous = song9

    print("Printing the linked song objects: ")
    print("Iterating in forward direction: ")
    temp = song1
    while True:
        temp.show()
        temp = temp.next
        if temp == song1:
            break

    print("Iterating in Backward Direction...")
    temp = song10
    while True:
        temp.show()
        temp = temp.previous
        if temp == song10:
            break


if __name__ == "__main__":
    main()
