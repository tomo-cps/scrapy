import scrapy
from urllib.request import urlopen
import urllib.request
import urllib.parse
import urllib


class PostsSpider(scrapy.Spider):
    name = "reviews"

    start_urls = [
        'https://www.yelp.com/biz/marufuku-ramen-san-francisco-5'
    ]

    def parse(self, response):
        for reviews in response.css('[class=" review__09f24__oHr9V border-color--default__09f24__NPAKY"]'):
            yield{
                'name':reviews.css('a[class="css-1m051bw"]::text').get(),
                'birthplace':reviews.css('span[class=" css-qgunke"]::text').get(),
                'comment':reviews.css('span[class=" raw__09f24__T4Ezm"]::text').getall()
            }



        for strpage in range(110,200,10):
            html=('https://www.yelp.com/biz/marufuku-ramen-san-francisco-5?start={0}'.format(strpage))
            yield scrapy.Request(html, callback=self.parse)
            
            

#        next_page = response.css('[class="pagination-link-component__09f24__JRiQO css-144i0wq"]::attr(href)').get()
#        if next_page is not None:
#            next_page = response.urljoin(next_page)
#            yield scrapy.Request(next_page, callback=self.parse)
            
