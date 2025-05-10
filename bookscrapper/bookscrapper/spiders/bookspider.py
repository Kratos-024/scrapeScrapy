import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css("article.product_pod")
        for book in books:
           price = book.css("div.product_price p::text").get()
           title = book.css("article.product_pod h3 a::text").get()
           print(f'Price: {price}, Title: {title}\n')
           

