import scrapy

class GoodReadsSpider(scrapy.Spider):
    # identity
    name = "goodreads"

    # requests
    def start_requests(self):
        urls = [
            "https://www.goodreads.com/quotes?page=1",
            "https://www.goodreads.com/quotes?page=2"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # response

    def parse(self, response):
        print("----------------------------------------------------")
        print(response)
        print("----------------------------------------------------")
        page_number = response.url.split("=")[1]
        _file = "{0}.html".format(page_number)
        with open(_file, "wb") as f:
            f.write(response.body)
