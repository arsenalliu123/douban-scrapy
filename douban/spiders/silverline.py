from scrapy.selector import Selector
from douban.items import RatingItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request
import re

class MovieRatingSpider(CrawlSpider):
    name = "MovieRating"
    allowed_domains = ["movie.douban.com"]
    whichcookie = 0
    start_urls = [
        "http://movie.douban.com/subject/1292722/",
        "http://movie.douban.com/subject/1652587/"
    ]

    rules = [
        #Rule(SgmlLinkExtractor(allow=('/tag/.*$', )), follow=True, process_request='add_cookie'),
        Rule(SgmlLinkExtractor(allow=('/subject/[0-9]+/$', )), follow=True),
        Rule(SgmlLinkExtractor(allow=('/subject/[0-9]+/collections\?start=1?[0-9]0$', )), follow=True),
        Rule(SgmlLinkExtractor(allow=('/subject/[0-9]+/collections$', )), follow=True),
        Rule(SgmlLinkExtractor(allow=('/people/.+/$', )), follow=True),
        Rule(SgmlLinkExtractor(allow=('/people/.+/collect$', )), follow=True),
        Rule(SgmlLinkExtractor(allow=('/people/.+/collect\?sort=time&amp;start=0&amp;filter=all&amp;mode=list&amp;tags_sort=count$', )), follow=True, callback='parse_rating_page'),
        Rule(SgmlLinkExtractor(allow=('/people/.+/collect\?start=[0-9]{2,}&sort=time&rating=all&filter=all&mode=list$', )), follow=True, callback='parse_rating_page'),
    ]

    def add_cookie(self, request):
        self.whichcookie = (self.whichcookie + 1) % 3
        if(self.whichcookie == 0):
            request.replace(headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                           'Accept-Encoding': 'gzip,deflate,sdch',
                           'Accept-Language': 'en-US,en;q=0.8',
                           'Connection': 'keep-alive',
                           'Cookie': 'bid=01234567890; dbcl2="54109049:sv7Zd87ck/0"; ck="KVCg"; __utma=223695111.629154438.1386609445.1386609445.1386612629.2; __utmb=223695111.2.10.1386612629; __utmc=223695111; __utmz=223695111.1386612629.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=30149280.1406128969.1386611895.1386611895.1386611895.1; __utmb=30149280.14.8.1386612634661; __utmc=30149280; __utmz=30149280.1386611895.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=30149280.5410; report=ref=%2F&from=mv_a_pst; RT=s=1386613163599&r=http%3A%2F%2Fmovie.douban.com%2F',
                           'Host': 'movie.douban.com',
                           'Referer': 'http://movie.douban.com/',
                           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31'}
                            );
        if(self.whichcookie == 1):
            request.replace(headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                           'Accept-Encoding': 'gzip,deflate,sdch',
                           'Accept-Language': 'en-US,en;q=0.8',
                           'Connection': 'keep-alive',
                           'Cookie': 'bid=01234567890; dbcl2="80986831:7md+WndhqYE"; ck="KVCg"; __utma=223695111.629154438.1386609445.1386609445.1386612629.2; __utmb=223695111.2.10.1386612629; __utmc=223695111; __utmz=223695111.1386612629.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=30149280.1406128969.1386611895.1386611895.1386611895.1; __utmb=30149280.14.8.1386612634661; __utmc=30149280; __utmz=30149280.1386611895.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=30149280.5410; report=ref=%2F&from=mv_a_pst; RT=s=1386613163599&r=http%3A%2F%2Fmovie.douban.com%2F',
                           'Host': 'movie.douban.com',
                           'Referer': 'http://movie.douban.com/',
                           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31'}
                            );
        if(self.whichcookie == 2):
            request.replace(headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                           'Accept-Encoding': 'gzip,deflate,sdch',
                           'Accept-Language': 'en-US,en;q=0.8',
                           'Connection': 'keep-alive',
                           'Cookie': 'bid=01234567890; dbcl2="80987508:riCh6YcKeQE"; ck="KVCg"; __utma=223695111.629154438.1386609445.1386609445.1386612629.2; __utmb=223695111.2.10.1386612629; __utmc=223695111; __utmz=223695111.1386612629.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=30149280.1406128969.1386611895.1386611895.1386611895.1; __utmb=30149280.14.8.1386612634661; __utmc=30149280; __utmz=30149280.1386611895.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=30149280.5410; report=ref=%2F&from=mv_a_pst; RT=s=1386613163599&r=http%3A%2F%2Fmovie.douban.com%2F',
                           'Host': 'movie.douban.com',
                           'Referer': 'http://movie.douban.com/',
                           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31'}
                            );
        return request;

    def __get_id_from_url(self, url):
        m = re.search("^http://movie.douban.com/people/([^/]+)/.*$", url)
        if(m):
            return m.group(1)
        else:
            return 0

    def parse_rating_page(self, response):
        self.log("Fetch movie home page: %s" % response.url)
        sel = Selector(response)
        items = []
        for auto_increa in range(1,31):
            item = RatingItem()
            #user is movie
            userselect = '//li[@class="item"][%s]//div[@class="title"]/a/@href' % auto_increa
            user = sel.xpath(userselect).re("^.*/subject/([^/]+)/$")
            if(len(user)):
                item['user'] = user[0]
            else:
                item['user'] = 0
            #movie is user
            item['movie'] = self.__get_id_from_url(response.url)
            ratingselect = '//li[@class="item"][%s]//div[@class="date"]/span[1]/@class' % auto_increa
            rating = sel.xpath(ratingselect).re("^.*([1-5]).*$")
            if(len(rating)):
                item['rating'] = rating[0]
            else:
                item['rating'] = 0
            if(item['rating']):
                items.append(item)
        item = RatingItem()
        #user is movie
        userselect = '//li[@class="item last"]//div[@class="title"]/a/@href'
        user = sel.xpath(userselect).re("^.*/subject/([^/]+)/$")
        if(len(user)):
            item['user'] = user[0]
        else:
            item['user'] = 0
        #movie is user
        item['movie'] = self.__get_id_from_url(response.url)
        ratingselect = '//li[@class="item last"]//div[@class="date"]/span[1]/@class'
        rating = sel.xpath(ratingselect).re("^.*([1-5]).*$")
        if(len(rating)):
            item['rating'] = rating[0]
        else:
            item['rating'] = 0
        if(item['rating']):
             items.append(item)
        hand = open("ratings.data", "a")
        for item in items:
            print >> hand, "%s %s %s" % (item['movie'], item['user'], item['rating'])
        hand.close()
