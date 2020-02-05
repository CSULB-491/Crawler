from django.shortcuts import render
import feedparser
from crawler.static.crawler.HTML import ArticleHTMLParser
from .models import Author
from .models import Publisher
from .models import Article


# Create your views here.
class Crawler:
    banned_sites = []
    possible_article_attributes = ['title', 'author', 'author_detail', 'publisher', 'publisher_detail',
                                   'contributors', 'tags', 'link', 'published', 'description', 'content', 'summary']
    html_parser = ArticleHTMLParser()
    rss_feeds = ['http://feeds.bbci.co.uk/news/world/rss.xml',
                 'http://feeds.reuters.com/Reuters/worldNews', 'http://feeds.washingtonpost.com/rss/rss_blogpost',
                 'https://www.yahoo.com/news/rss/world', 'http://rss.cnn.com/rss/edition_world.rss',
                 'http://rssfeeds.usatoday.com/usatoday-newstopstories&x=1', 'https://www.yahoo.com/news/rss/',
                 'http://feeds.reuters.com/Reuters/domesticNews', 'http://feeds.skynews.com/feeds/rss/us.xml',
                 'http://rss.cnn.com/rss/edition_us.rss', 'http://feeds.skynews.com/feeds/rss/uk.xml',
                 'http://feeds.bbci.co.uk/news/rss.xml', 'http://feeds.reuters.com/reuters/UKdomesticNews',
                 'https://www.theguardian.com/uk/rss', 'https://techcrunch.com/rssfeeds/',
                 'http://rss.slashdot.org/Slashdot/slashdot', "https://news.google.com/news/rss",
                 'https://spectrum.ieee.org/rss/blog/tech-talk/fulltext', 'https://www.techworld.com/news/rss',
                 'https://www.wired.com/feed',
                 'http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml',
                 'https://www.npr.org/rss/rss.php?id=1045',
                 'https://www.fandango.com/rss/newmovies.rss', 'http://www.metacritic.com/rss/movies',
                 'https://www.rogerebert.com/feed',
                 'http://www.movies.com/rss-feeds/movie-news-rss', 'http://www.si.com/rss/si_topstories.rss',
                 'http://feeds1.nytimes.com/nyt/rss/Sports', 'https://talksport.com/rss/sports-news/all/feed',
                 'http://feeds.sport24.co.za/articles/Sport/Featured/TopStories/rss',
                 'http://rss.cnn.com/rss/edition_sport.rss',
                 'http://syndication.eonline.com/syndication/feeds/rssfeeds/topstories.xml',
                 'http://feeds.reuters.com/reuters/entertainment',
                 'http://www.instyle.com/feeds/all/ins.rss',
                 'http://feeds.accesshollywood.com/AccessHollywood/LatestNews',
                 'https://www.npr.org/rss/rss.php?id=1008', 'https://api.quantamagazine.org/feed/']

    def __init__(self):
        # self.parse_rss()
        with open('crawler/static/crawler/test2.html', encoding="utf8") as html_file:
            self.html_parser.get_content_from_html(html_file)

    @classmethod
    def gather_article_attributes(cls, article):
        current_article = {"content": "null"}
        for attribute in cls.possible_article_attributes:
            if hasattr(article, attribute):
                current_article[attribute] = article[attribute] if article[attribute] else "null"

        return current_article

    @classmethod
    def parse_rss(cls):
        # @TODO need to create a pre-parse hash that will identify if article already has been processed
        articles = feedparser.parse(cls.rss_feeds[2])
        # articles = feedparser.parse('https://api.quantamagazine.org/feed/')

        for article in articles.entries:
            article_attributes = cls.gather_article_attributes(article)

            # can add these in later if so inclined
            # logo = article.feed.logo if article.feed.logo else "No logo"
            # image = article.feed.image if article.feed.image else "No image"

            # parse the link for article content if there is no content in the rss feed
            if article_attributes["content"] == "null":
                article_attributes["content"] = cls.html_parser.get_content_from_url(article_attributes["link"])

            try:
                print(article_attributes)
            except:
                print("couldn't print an encoded character")

            # @TODO need to follow links to get the full context if context not found
            # @TODO decide what nulls are going to look like, be careful with "null" currently inplace
            # @TODO create a textfile with all the parsed content and then create a db entry
            # @TODO descriptions and summaries appear to be the same thing
            # @TODO create a reliable hash to store in the db so articles can be quickly checked for existence
            # @TODO author details seem useless?
            # @TODO need to multithread/whatever python has pulling the html and all processes in general

    @classmethod
    def crawl_the_web(cls, time_interval):
        print("crawler is crawling")
        cls.parse_rss()

    @classmethod
    def create_author(cls, first_name, last_name):
        author = Author()
        author.first_name = first_name
        author.last_name = last_name
        author.save()
        cls.print_authors()

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
        cls.rss_feeds.append(url)
        print("adding feed")

    @classmethod
    def edit_rss_feed(cls, current_rss_feed, edited_rss_feed):
        index = cls.rss_feeds.index(current_rss_feed)
        cls.rss_feeds[index] = edited_rss_feed
        print("edited feed")

    @classmethod
    def remove_rss_feed(cls, feed):
        cls.rss_feeds.remove(feed)
        print("removing feed")

    @classmethod
    def filter_site(cls, url):
        print("filtering")

    @classmethod
    def print_authors(cls):
        authors = Author.objects.all()
        for author in authors:
            print(author.first_name, author.last_name)

