import scrapy
from bookscrapper.items import BookItem

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
       
      
        # print("***********************************************")
        # books = response.css("article.product_pod")
        
        
    def parse_book_page(self,response):

        # title = response.css('div.product_main h1::text').get()
        # print(title)
        table_rows = response.css(".table-striped tr")
        bookitem= BookItem()
                    
        bookitem["title"]=response.xpath("/html/body/div/div/div[2]/div[2]/article/div[1]/div[2] /h1/text()").get(),
        bookitem["url"]=response.url,
        bookitem["product_type"]=table_rows[1].css("td ::text").get(),
        bookitem["price_excel_tax"]=table_rows[2].css("td ::text").get(),
        bookitem["price_incl_tax"]=table_rows[3].css("td ::text").get(),
        bookitem["Availability"]=table_rows[5].css("td ::text").get(),
        bookitem["ratting"]=response.css("p.star-rating ::attr('class')").get()[12:],
        bookitem["price"]= response.css("div.product_main .price_color::text").get(),
        bookitem["description"]=response.xpath('//*[@id="content_inner"]/article/p/text()').get()
        yield bookitem
                    

                

            
        
        


        
            

            
            
