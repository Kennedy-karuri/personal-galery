from django.db import models
import datetime as dt
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.


class Article(models.Model):
    caption = models.CharField(max_length=100)
    title = models.CharField(max_length=60)
    description = models.TextField(default='')
    location = models.TextField(
        max_length=30, null=False, blank=False, default='')
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = CloudinaryField('article')

    @classmethod
    def todays_photos(cls):
        today = dt.date.today()
        gallery = cls.objects.filter(pub_date__date=today)
        return gallery

    @classmethod
    def search_by_title(cls, search_term):
        gallery = cls.objects.filter(title__icontains=search_term)
        return gallery

    @classmethod
    def get_one_photo(cls, id):
        pictures = cls.objects.filter(id=id)
        return pictures


class Category(models.Model):
    category = models.CharField(max_length=80, null=True)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self):
        self.update()

    def __str__(self):
        return self.category


class Categories(models.Model):
    name = models.CharField(max_length=30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name
