import feedparser
from crawler.static.crawler.HTML import ArticleHTMLParser
from .models import Author
from .models import Publisher
from .models import Article


# Create your views here.
class Crawler:
    banned_sites = []
    possible_article_attributes = ['title', 'author', 'publisher',
                                   'contributors', 'tags', 'link', 'published']
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
        self.parse_rss()
        # with open('crawler/static/crawler/test.html', encoding="utf8") as html_file:
        #     self.html_parser.get_content_from_html(html_file)

    @classmethod
    def gather_article_attributes(cls, article):
        current_article = {"content": "null"}
        for attribute in cls.possible_article_attributes:
            if hasattr(article, attribute):
                current_article[attribute] = article[attribute] if article[attribute] else "null"

        return current_article

    @classmethod
    def parse_rss(cls):
        rss_source = feedparser.parse(cls.rss_feeds[2])

        for article in rss_source.entries:
            article_attributes = cls.gather_article_attributes(article)
            article_attributes["content"] = cls.html_parser.get_content_from_url(article_attributes["link"])

            # can add these in later if so inclined
            # logo = article.feed.logo if article.feed.logo else "No logo"
            # image = article.feed.image if article.feed.image else "No image"

            try:
                print(ascii(article_attributes), "\n")
            except:
                print("couldn't print an encoded character")

            # @TODO decide what nulls are going to look like, be careful with "null" currently inplace
            # @TODO create a textfile with all the parsed content and then create a db entry
            # @TODO create a reliable hash to store in the db so rss_source can be quickly checked for existence
            # @TODO need to make crawling asynchronous
            # @TODO refine the paragraphs parsed from html: include <h>?, remove leading <p>, remove <href>
            # @TODO remove tags with :None
            # @TODO fix ascci/unicode conversion errors for " and ', &#39, \u201d\u201c\u2019\u2017\u2014\u2018;
            # @TODO handle 404 errors gracefully in html crawler + add timeouts

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

