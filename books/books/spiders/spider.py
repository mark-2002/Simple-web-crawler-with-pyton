import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        all_the_books = response.xpath("//article")

        for books in all_the_books:
            title = books.xpath(".//h3/a/@title").extract_first()#telling scrapy to check within the element,using .extract() will bring a list rather use .extract_first()
            prices = books.xpath('.//p[@class = "price_color"]/text()').extract_first() # /text gets the text from it
            images = self.start_urls[0] + books.xpath(".//a/img/@src").extract_first() #using self. to append prefix of images to the original url
            print(title)
            print(prices)
            print(images)

            yield{
                'Title':title,
                'Prices':prices,
                'Image_link':images
            }
            #you can dump it into a file with scrapy crawl spider -o filename

        

