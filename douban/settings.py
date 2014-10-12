# Scrapy settings for douban project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
from scrapy.core.downloader.webclient import ScrapyHTTPClientFactory, ScrapyHTTPPageGetter

class PageGetter(ScrapyHTTPPageGetter):

    def sendCommand(self, command, path):
        self.transport.write('%s %s HTTP/1.1\r\n' % (command, path))

class HTTPClientFactory(ScrapyHTTPClientFactory):

    protocol = PageGetter

BOT_NAME = 'douban'

SPIDER_MODULES = ['douban.spiders']
NEWSPIDER_MODULE = 'douban.spiders'

DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True
#USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31'
COOKIES_ENABLED = True
DEFAULT_REQUEST_HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31'}
DOWNLOADER_HTTPCLIENTFACTORY = 'HTTPClientFactory'
