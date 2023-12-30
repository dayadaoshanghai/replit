import csv
import os  

dirname = os.path.dirname(__file__)
print(dirname)

with open("100MostStreamedSongs.csv") as file:
    reader = csv.DictReader(file) 
    for row in reader:
        # print(row)
        artist = row["Artist(s)"]
        song = row["Song"]

        artist_folder = os.path.join(dirname, artist)
        if not os.path.exists(artist_folder):
            os.mkdir(artist_folder) 

        song_path = os.path.join(artist_folder, f"{song}.txt")
        with open(song_path, "w") as song_file:
            pass
        # f = open(song_path, "w") 
        # f.close()
            

print("Done")


