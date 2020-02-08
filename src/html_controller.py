import unicodedata
from bs4 import BeautifulSoup
import urllib.request


# Provides html retrieval and parsing
class HTMLParser:

    @staticmethod
    # Takes in a url(str) to an article and returns a string containing the article's text
    def get_content_from_url(url: str) -> str:
        # Get html, create parser
        article_content = ""
        html = HTMLParser.pull_html_from_url(url)
        parser = BeautifulSoup(html, "html.parser")

        # Remove scripts and unwanted html content that may be nested in <p>'s
        for unwanted_content in parser(['style', 'script', 'head', 'title', 'meta', '[document]']):
            unwanted_content.extract()

        # Extract all paragraphs and append them to the article content
        paragraphs_of_text = [paragraph.get_text() for paragraph in parser.find_all("p", text=True)]
        for paragraph in paragraphs_of_text:
            article_content += paragraph

        # Remove a few pesky unicode holdovers...doesn't seem to work atm \xa0 still appears
        unicodedata.normalize("NFKD", article_content)
        return article_content

    @staticmethod
    # Takes in a url(str) and returns its html
    def pull_html_from_url(url: str) -> bytes:
        # Try to pull HTML from url
        try:
            request = urllib.request.urlopen(url)
            return request.read()

        # Catch HTTP error
        except urllib.request.HTTPError as error:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', error.code)

        # Catch URL error
        except urllib.request.URLError as error:
            print('We failed to reach a server.')
            print('Reason: ', error.reason)

