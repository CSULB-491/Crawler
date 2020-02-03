from django.shortcuts import render
import feedparser
# Create your views here.


def crawl_the_web():
    print("crawler is crawling")
    parse()


def parse():
    parsedFeed = feedparser.parse("http://www.reddit.com/r/python/.rss")
    print(parsedFeed['feed']['title'])

