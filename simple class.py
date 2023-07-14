class songs:
    pass
 

song1=songs()
song2=songs()
song3=song1
     
     
print("song1 is:", song1 , id(song1), type(song1), hex(id(song1)))
print("song2 is:", song2 , id(song2), type(song2), hex(id(song2)))
print("song3 is:", song3 , id(song3), type(song3), hex(id(song3)))
print("Data inside object:", vars(song1))
print("Data inside object:", vars(song2))
print("Data inside object:", vars(song3))

song1.track = "Chorni"
song1.artist = "Sidhu Moosewala, Divine"
song1.duration = "4 min"

song2.track = "Moosetape"
song2.artist = "Sidhu Moosewala, Divine"
song2.duration = "1hour 45min"

song3.track = "Lovesick"




print("Data inside object now:", vars(song1))
print("Data inside object now:", vars(song2))
print("Data inside object now:", vars(song3))