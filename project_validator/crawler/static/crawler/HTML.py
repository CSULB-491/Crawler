from bs4 import BeautifulSoup
import urllib.request


class ArticleHTMLParser:

    def get_content_from_url(self, url):
        # Get html, create parser
        article_content = ""
        html = self.pull_html_from_url(url)
        parser = BeautifulSoup(html, "html.parser")

        # Remove scripts and unwanted content that may be nested in <p>'s
        for unwanted_content in parser(['style', 'script', 'head', 'title', 'meta', '[document]']):
            unwanted_content.extract()

        # Extract all paragraphs and append them to the content
        paragraphs_of_text = [paragraph.get_text() for paragraph in parser.find_all("p", text=True)]
        for paragraph in paragraphs_of_text:
            article_content += paragraph
        return article_content

    def pull_html_from_url(self, url):
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

