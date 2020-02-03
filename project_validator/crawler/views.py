from django.shortcuts import render
import feedparser
from .models import Author
from .models import Publisher
from .models import Article
# Create your views here.


class Crawler:
    def __init__(self):
        self.parse()
        self.create_author("test", "author")

    @classmethod
    def parse(cls):
        parsed_feed = feedparser.parse("http://www.reddit.com/r/python/.rss")
        print(parsed_feed['feed']['title'])

    @classmethod
    def crawl_the_web(cls, time_interval):
        print("crawler is crawling")
        cls.parse()

    @classmethod
    def create_author(cls, first_name, last_name):
        author = Author()
        author.first_name = first_name
        author.last_name = last_name

    @classmethod
    def create_publisher(cls, name):
        publisher = Publisher()
        publisher.name = name

    @classmethod
    def create_article(cls, title, content):
        article = Article()
        article.title = "First Test Article Title"
        article.content = "Content for first article abcdefghijklmnopq"
        Article.objects.create(article)

    @classmethod
    def add_rss_feed(cls, url):
        print("adding feed")

    @classmethod
    def edit_rss_feed(cls, feed):
        print("editing feed")

    @classmethod
    def remove_rss_feed(cls, feed):
        print("removing feed")

