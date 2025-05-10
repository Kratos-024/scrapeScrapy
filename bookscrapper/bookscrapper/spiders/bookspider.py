import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]
    count=1

    def parse(self, response):
        books = response.css("article.product_pod")
        # listt = []

        # for book in books:
        #     data = {"price" :book.css("div.product_price p::text").get(),
        #    "title" :book.css("article.product_pod h3 a::text").get()}
        #     listt.append(data)
        for book in books:
            relative_url= book.css('h3 a::attr("href")').get()
            if 'catalogue/' in relative_url:

                book_url = "https://books.toscrape.com/" + relative_url
               
            else:
                book_url = "https://books.toscrape.com/catalogue/" + relative_url
            self.count+=1
            yield response.follow(book_url,callback=self.parse_book_page) 
        next_page = response.css("li.next a::attr(href)").get()
       
        if next_page:
            
            if 'catalogue/' in next_page:
                next_page_url = "https://books.toscrape.com/" + next_page
                yield response.follow(next_page_url,callback=self.parse)
            else:
                next_page_url = "https://books.toscrape.com/catalogue/" + next_page
                yield response.follow(next_page_url,callback=self.parse)
        # print("***********************************************")
        # books = response.css("article.product_pod")
        
        
    def parse_book_page(self,response):

        # title = response.css('div.product_main h1::text').get()
        # print(title)
        table_rows = response.css(".table-striped tr")
        yield {
            "title":response.xpath("/html/body/div/div/div[2]/div[2]/article/div[1]/div[2] /h1/text()").get(),
            "url":response.url,
            "product_type":table_rows[1].css("td ::text").get(),
            "price_excel_tax":table_rows[2].css("td ::text").get(),
            "price_incl_tax":table_rows[3].css("td ::text").get(),
            "Availability":table_rows[5].css("td ::text").get(),
            "ratting":response.css("p.star-rating ::attr('class')").get()[12:]
        }
        
        


        
            

            
            
