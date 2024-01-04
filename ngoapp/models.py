from django.db import models



class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    organizer = models.CharField(max_length=255)
    image = models.ImageField(upload_to='event_images/')
    description = models.TextField()
    time = models.CharField(max_length=255)
    location = models.CharField(max_length=255)


class Volunteer(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    email = models.EmailField(max_length=254)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    # Add other fields for volunteers

class Task(models.Model):
    description = models.TextField()
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)

