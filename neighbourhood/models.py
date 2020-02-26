from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    email = models.EmailField()
    bio = models.TextField(max_length= '255', blank=True)
    avatar = models.ImageField(upload_to='images/profile_picture/', default = 'images/profile_picture/default.png')
    

    def __str__(self):
        return self.user.username


class Neighbourhood(models.Model):
    hood_name = models.CharField(max_length=255)
    hood_location = models.CharField(max_length=255)
    count = models.IntegerField()
    user = models.ForeignKey(Profile, on_delete = models.CASCADE)

    def __str__(self):
        return self.hood_name

    def create_neighbourhood(self):
        self.save()
        
    @classmethod
    def delete_neighbourhood(cls, hood_name):
        cls.objects.filter(hood_name=hood_name).delete()

    @classmethod
    def find_neighbourhood(cls, search_term):
        search_results = cls.objects.filter(hood_name__icontains = search_term)
        return search_results

    def update_neighbourhood(self, hood_name):
        self.hood_name = hood_name
        self.save()



class Business(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(Profile, on_delete = models.CASCADE)
    description = models.TextField(max_length=255, blank=True)
    hood = models.ForeignKey(Neighbourhood, on_delete = models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.name

    def create_business(self):
        self.save()
        
    @classmethod
    def delete_business(cls, name):
        cls.objects.filter(name=name).delete()

    @classmethod
    def find_business(cls, search_term):
        search_results = cls.objects.filter(name__icontains = search_term)
        return search_results

    def update_business(self, name):
        self.name = name
        self.save()

class Post(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(Profile, on_delete = models.CASCADE)
    hood = models.ForeignKey(Neighbourhood, on_delete = models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, blank=True)
    description = models.TextField(max_length=600)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self): # new
        return reverse('post_detail', args=[str(self.id)])

    

    