from bs4 import BeautifulSoup
import urllib.request


class ArticleHTMLParser():
    content = ""

    async def get_content_from_url(self, url):
        print("getting content from ", url)
        html = self.get_html_from_site(url)
        parser = BeautifulSoup(html, "html.parser")
        article_contents = [paragraph.get_text() for paragraph in parser.find_all("p", text=True)]
        for paragraph in article_contents:
            self.content += paragraph
        return self.content

    async def get_content_from_html(self, html):
        # @TODO refine the paragraphs parsed from html
        # @TODO fix ascci/unicode conversion errors
        parser = BeautifulSoup(html, "html.parser")
        article_contents = [paragraph.get_text() for paragraph in parser.find_all("p", text=True)]
        # for items in article_contents:
        #     print(ascii(items))
            # print(items.encode("utf-8"))
        for paragraph in article_contents:
            self.content += paragraph
        return self.content

    def get_html_from_site(self, url):
        try:
            request = urllib.request.urlopen(url)
            return request.read()
            # html.unescape()
        except urllib.request.HTTPError as error:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', error.code)
        except urllib.request.URLError as error:
            print('We failed to reach a server.')
            print('Reason: ', error.reason)

