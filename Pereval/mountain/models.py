from django.db import models
from django.core.files import File
# Create your models here.


class Users(models.Model):
    email = models.EmailField(max_length=128)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    patronymic = models.CharField(max_length=64)
    phone = models.CharField(max_length=20)
    
class Pereval(models.Model):
    NEW = 'NW'
    PEDING = 'PG'
    ACCEPTED = 'AC'
    REJECTED = 'RJ'
    STATUS_CHOICES = (
        ('NW', 'new'),
        ('PG', 'pending'),
        ('AC', 'accepted'),
        ('RJ', 'rejected')
    )

    beauty_title = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    other_titles = models.CharField(max_length=128)
    connect = models.CharField(max_length=128)
    add_time = models.DateTimeField(auto_now_add=True)
    tourist_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=NEW)
    level = models.ForeignKey('Level', on_delete=models.CASCADE)
    coords_id = models.OneToOneField('Coords', on_delete=models.CASCADE)


class Level(models.Model):
    
    summer = '1A'
    spring = '2A'
    autumn = '3A'
    winter = '4A'

    LEVEL_CHOICES = (
        ('1A', 'summer'),
        ('2A', 'spring'),
        ('3A', 'autumn'),
        ('4A', 'winter')
    )

    summer_lvl = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=None)
    spring_lvl = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=None)
    autumn_lvl = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=None)
    winter_lvl = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=None)

class Coords(models.Model):
     latitude = models.DecimalField(decimal_places=8, max_digits=10)
     longitude = models.DecimalField(decimal_places=8, max_digits=10)
     height = models.IntegerField(default=0)

class Images(models.Model):
    image = models.ImageField(upload_to='static/images')
    title = models.CharField(max_length=64)
    pereval_id = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name = 'images')


    def __str__(self):
        return self.title