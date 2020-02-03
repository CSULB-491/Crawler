from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s" % (self.firstName, self.lastName)


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
