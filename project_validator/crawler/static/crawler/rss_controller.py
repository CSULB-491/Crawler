import re
import unittest
import feedparser
from project_validator.crawler.static.crawler.html_controller import HTMLParser
from textblob import TextBlob
# from project_validator.crawler.models import Author


class Crawler:
    banned_sites = []
    rss_attributes = ['title', 'author', 'publisher', 'link', 'published', "tokenizedTitle", "words"]
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
        self.update_rss_feeds()
        # self.find_publisher()

    # Takes an rss feed and returns a dict containing its attributes(Author, publisher, date...)
    def parse_rss_feed(self, rss_feed: feedparser.FeedParserDict) -> dict:
        # Ensure content is not taken from the rss feed
        article_content = {"content": "null"}

        # Pull all other relevant feed information
        for attribute in self.rss_attributes:
            if hasattr(rss_feed, attribute):
                article_content[attribute] = rss_feed[attribute] if rss_feed[attribute] else "null"
            else:
                article_content[attribute] = "null"

        article_content["content"] = "null"
        return article_content

    # Pulls a single hardcoded rss feed and prints its info to console
    def update_rss_feeds(self):
        # Hardcoded feed
        # rss_publisher = self.rss_feeds[4]
        rss_publisher = 'https://www.npr.org/rss/rss.php?id=1045'
        rss_source = feedparser.parse(rss_publisher)

        # Parse each feed in the rss source (a source can supply more than 1 feed)
        for current_feed in rss_source.entries:
            article_attributes = self.parse_rss_feed(current_feed)
            article_attributes["publisher"] = self.find_publisher(rss_publisher)
            article_attributes["content"] = HTMLParser.get_content_from_url(article_attributes["link"])
            article_attributes["words"] = len(article_attributes["content"])

            if article_attributes["author"] != "null":
                article_attributes["author"] = self.clean_authors(article_attributes["author"])

            self.create_database_entries(article_attributes)

            self.tokenize_title(article_attributes)
            unfiltered_content = TextBlob(article_attributes["content"])
            # add word count?
            # logo = article.feed.logo if article.feed.logo else "No logo"
            # image = article.feed.image if article.feed.image else "No image"

            try:
                # print("Content: ",article_attributes["content"])
                print("Number of Words: ",article_attributes["words"])
                # print("Link: ",article_attributes["link"])
                # print("Date Published: ", article_attributes["published"])
                # print("Publisher:",article_attributes["publisher"])  # If you are printing \u2019 and such run <chcp 65001> in the terminal
                # print("Author:",article_attributes["author"])
                # print(unfiltered_content.sentiment, "\n")

            except Exception as e:
                print(str(e))

            # @TODO pass content to nlp as a string, pass parsed title to nlp as list
            # @TODO Richard - create a reliable hash to store in the db so rss_source can be quickly checked for existence (name, date, publisher)
            # @TODO need to make crawling asynchronous
            # @TODO Richard - handle 404 errors gracefully in html crawler + add timeouts
            # @TODO put everything in a loop that won't exceed the nlp's money constraints
            # @TODO create all the authors and such as parsed
            # @TODO Create a manager aspect that handles articles rated by NLP and user interactions with articles?

    def tokenize_title(self, article_attributes: dict):
        unfiltered_title = TextBlob(article_attributes["title"])
        filtered_title = []
        all_words = unfiltered_title.tags
        for word,tag in all_words:
            if tag in ("NN", "NNS", "NNP", "NNPS","JJ", "JJR", "JJS", "VBD", "VBZ","VBG","VBN","VBP") and len(word) > 1:
                filtered_title.append(word)

        print("Title: ", unfiltered_title, "->", filtered_title)
        return filtered_title

    def clean_authors(self, authors_unfiltered: str):
        filter = TextBlob(authors_unfiltered)
        return str(filter.noun_phrases)

    def create_authors(self, author_list: str):
        names = author_list.split()
        for i in range(0, len(names), 2):
            name = names[i:i + 2]
            print(name, ":author\n")
            # current_author = Author(first_name=fname, last_name=lname)
            # current_author.save()

    # def create_article(self, article_attributes: dict):

    def create_database_entries(self, article_attributes: dict):
        print("creating db entries")
        # self.create_authors(article_attributes["author"])
        # self.create_article(article_attributes)

    def find_publisher(self, feed: str) -> str:
        name_start_index = 0
        name_end_index = 0

        publisher = re.search(".+.com?", feed)

        if publisher is None:
            publisher = re.search(".+.org?", feed)

        name_start_index = publisher.group(0).index('.') +1
        name_end_index = publisher.group(0).rindex('.')

        return publisher.group(0)[name_start_index: name_end_index: 1]


class TestTitleParsing(unittest.TestCase):
    crawler = Crawler()

    def test_accuracy(self):
        title = {"title":'At Last, Billie Eilish"\'"s James Bond Theme Song Is Here'}
        a = self.crawler.tokenize_title(title)
        b = ['Last', 'Billie', 'Eilish', 'James', 'Bond', 'Theme', 'Song', 'Is']
        self.assertCountEqual(a,b)


class TestBlahParsing(unittest.TestCase):
    crawler = Crawler()

    def test_accuracy(self):
        title = {"title": 'At Last, Billie Eilish"\'"s James Bond Theme Song Is Here'}
        a = self.crawler.tokenize_title(title)
        b = ['Last', 'Billie', 'Eilish', 'James', 'Bond', 'Theme', 'Song', 'Is']
        self.assertCountEqual(a, b)


# Auto-runs all unit classes and each method method in the class
unittest.main()
