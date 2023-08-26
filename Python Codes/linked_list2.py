from linked_list import Songs, Playlist

def main():
    play_list = Playlist()
    print("PlayList:", play_list, vars(play_list))

    play_list.append(song=Songs(track="1. Udd Jaa Kaale Kaava", artists="Udit Narayan, Alka Yagnik", duration=4.48))
    play_list.append(song=Songs(track="2. Gustakhiyan", artists="Gurnam Bhullar", duration=3.5))
    play_list.append(song=Songs(track="3. Desperado", artists="Raghav, Tesher", duration=5.6))
    play_list.append(song=Songs(track="4. Chorni", artists="DIVINE, Sidhu Moose Wala", duration=4.12))
    play_list.append(song=Songs(track="5. Kasol", artists="Mani Longia, Starboy X", duration=2.28))
    play_list.append(song=Songs(track="6. Car Keys", artists="Alok, Ava Max", duration=2.26))
    play_list.append(song=Songs(track="7. Yahi Toh Hai Zindagi", artists="Suhit Abhyankar", duration=3.14))
    play_list.append(song=Songs(track="8. Check It Out", artists="Parmish Verma, Paradox", duration=3.15))
    play_list.append(song=Songs(track="9. Speed Drive", artists="Charli XCX", duration=1.57))
    play_list.append(song=Songs(track="10. Yaar Ka Sataya Hua Hai", artists="B Praak, Jaani, Nawazuddin Siddiqui, Shehnaz Kaur Gill", duration=4.28))


    print("PlayList:", play_list, vars(play_list))

    print("PRINTING PLAYLIST - FORWARD")
    play_list.iterate()

    print("PRINTING PLAYLIST - BACKWARD")
    play_list.iterate(1)

if __name__ == "__main__":
    main()
