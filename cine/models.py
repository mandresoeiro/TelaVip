from django.db import models

# Define the Genre model
class Genre(models.Model):
    name = models.CharField(max_length=255)  # Name of the genre

    def __str__(self):
        return self.name  # String representation of the genre


# Define the Streaming model
class streaming(models.Model):
    
    name = models.CharField(max_length=255)  # Name of the streaming service

    def __str__(self):
        return self.name  # String representation of the streaming service


# Define the Director model
class Director(models.Model):
    
    name = models.CharField(max_length=255)  # Name of the director

    def __str__(self):
        return self.name  # String representation of the director


# Define the Actor model
class Actor(models.Model):
    
    name = models.CharField(max_length=255)  # Name of the actor

    def __str__(self):
        return self.name  # String representation of the actor


# Define the Producer model
class Producer(models.Model):
    
    name = models.CharField(max_length=255)  # Name of the producer

    def __str__(self):
        return self.name  # String representation of the producer


# Define the Cine model
class Cine(models.Model):
    """
    Represents a movie or film.

    Attributes:
        id (int): Unique identifier for the movie.
        title (str): Title of the movie.
        genre (Genre): Genre of the movie.
        streaming (streaming): Streaming service the movie is available on.
        debut_year (int): Year the movie was released.
        actor (Actor): Actor who played in the movie.
        director (Director): Director of the movie.
        producers (Producer): Producers of the movie.
        original_writer (str): Original writer of the movie.
        resume (str): Brief summary of the movie.
        photo (ImageField): Image file for the movie.
    """
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    title = models.CharField(max_length=255)  # Title of the movie
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='cine_genre')  # Genre of the movie
    streaming = models.ForeignKey(streaming, on_delete=models.PROTECT, related_name='cine_streaming', null=True, blank=True)  # Streaming service
    debut_year = models.IntegerField(null=True, blank=True)  # Year of debut, can be null or blank
    actor = models.ForeignKey(Actor, on_delete=models.PROTECT, related_name='cine_actor', null=True, blank=True)  # Actor in the movie
    director = models.ForeignKey(Director, on_delete=models.PROTECT, related_name='cine_director', null=True, blank=True)  # Director of the movie
    producers = models.ForeignKey(Producer, on_delete=models.PROTECT, related_name='cine_producers', null=True, blank=True)  # Producers of the movie
    original_writer = models.CharField(null=True, blank=True, max_length=255)  # Original writer, can be null or blank
    resume = models.TextField(null=True, blank=True)  # Brief summary, can be null or blank
    photo = models.ImageField(upload_to="cine/", default="cine/default.jpg")  # Photo of the movie
    

    def __str__(self):
        return f"{self.title}"  # String representation of the movie

