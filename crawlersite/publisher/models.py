from django.db import models
from django.urls import reverse


# Every time django creates a publishers, it will create a unique primary key starting from 1, then 2 and so forth
class Publisher(models.Model):
    publisher_name = models.CharField(max_length=250)
    publisher_link = models.CharField(max_length=1000)
    publisher_logo = models.FileField()
    publisher_slug = models.CharField(max_length=200, default=1)

    def get_absolute_url(self):
        return reverse('publisher:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.publisher_name + ' - ' + self.publisher_link


class Author(models.Model):
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    author_image = models.FileField()
    article_count = models.CharField(max_length=10)
    author_name = models.CharField(max_length=250)
    author_slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.author_name


# each article is linked to a publishers. So each foreign key will be linked to a primary key
# what cascade does, or for this in particular, whenever we delete a publishers, any thing that was linked
# to that particular publishers(primary key) will also delete the articles linked with it(foreignkeys)
class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    article_title = models.CharField(max_length=250)
    article_date = models.CharField(max_length=250)

    def __str__(self):
        return self.article_title
