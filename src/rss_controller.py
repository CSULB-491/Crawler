import feedparser
from src.html_controller import HTMLParser


class Crawler:
    banned_sites = []
    rss_attributes = ['title', 'author', 'publisher', 'contributors', 'tags', 'link', 'published']
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

    # Takes an rss feed and returns a dict containing its attributes(Author, publisher, date...)
    def parse_rss_feed(self, rss_feed: feedparser.FeedParserDict) -> dict:
        article_content = {"content": "null"}
        for attribute in self.rss_attributes:
            if hasattr(rss_feed, attribute):
                article_content[attribute] = rss_feed[attribute] if rss_feed[attribute] else "null"

        return article_content

    # Pulls a single hardcoded rss feed and prints its info to console
    def update_rss_feeds(self):
        # Hardcoded feed
        rss_source = feedparser.parse(self.rss_feeds[2])

        # Parse each feed in the rss source (a source can supply more than 1 feed)
        for current_feed in rss_source.entries:
            article_attributes = self.parse_rss_feed(current_feed)
            article_attributes["content"] = HTMLParser.get_content_from_url(article_attributes["link"])

            # can add these in later if so inclined
            # logo = article.feed.logo if article.feed.logo else "No logo"
            # image = article.feed.image if article.feed.image else "No image"

            try:
                print(article_attributes, "\n")  # If you are printing \u2019 and such run <chcp 65001> in the terminal
            except Exception as e:
                print(str(e))

            # @TODO decide what nulls are going to look like for article attributes, be careful with "null"
            # @TODO create a textfile with all the parsed content and then create a db entry
            # @TODO create a reliable hash to store in the db so rss_source can be quickly checked for existence
            # @TODO need to make crawling asynchronous
            # @TODO remove tags with :None
            # @TODO handle 404 errors gracefully in html crawler + add timeouts
            # @TODO put everything in a loop that won't exceed the nlp's money constraints
            # @TODO create all the authors and such as parsed
            # @TODO decide on how to separate authors with same name/ identify those who write for 2+ publishers
            # @TODO \xa0 still shows up
            # @TODO Create a manager aspect that handles articles rated by NLP and user interactions with articles?
            # @TODO Decide how to sanitize user entered rss feeds
            # @TODO Handle site bans


Crawler()
