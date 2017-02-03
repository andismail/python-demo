from django.db import models

# Just like the tables
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    type = models.CharField(max_length=10, default='Def')
    album_logo = models.CharField(max_length=1000)
    album_desc = models.CharField(max_length=1000, default="default album describe")

    def __str__(self):
        return self.artist + "-" + self.album_title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10, default="mp3")
    file_size = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    song_desc = models.CharField(max_length=250, default="default describe")



#python3 manage.py migrate
#python3 manage.py makemigrations music
    # Create or modify tables under music app
#python3 manage.py sqlmigrate music 0001



