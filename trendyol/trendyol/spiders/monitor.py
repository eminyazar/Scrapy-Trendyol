import scrapy


class MonitorSpider(scrapy.Spider):
    name = "monitor"
    allowed_domains = ["www.trendyol.com"]
    start_urls = ["https://www.trendyol.com/monitor-x-c103668"]

    def parse(self, response):
        product_names = response.css("span.prdct-desc-cntnr-name.hasRatings::text").getall()
        product_prices = response.css("div.prc-box-dscntd::text").getall()
        product_titles = response.css("span.prdct-desc-cntnr-ttl::text").getall()

        yield {
                "product_titles": product_titles,
                "product_names": product_names,
                "product_prices": product_prices,
              
            }