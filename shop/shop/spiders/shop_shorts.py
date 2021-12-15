import scrapy


class ShopShortsSpider(scrapy.Spider):
    name = 'shop_shorts'
    #allowed_domains = ['https://in.seamsfriendly.com/collections/shorts']
    start_urls = ['https://in.seamsfriendly.com/collections/shorts/']

    # def parse(self, response):
    #     filename = "test.txt"
    #     title = response.xpath('//h2[contains(@class,"ProductItem") and contains(@class,"Heading")]//a/text()').extract()
    #     with open(filename, 'w') as f:
    #         for i in title:
    #             f.write(i+"\n")
    #             info = {
    #                 'title': i,
    #             }
    #             yield info
    filename = "test.txt"
    def parse(self, response):
        urls = response.xpath('//div[contains(@class,"ProductItem") and contains(@class, "Wrapper")]//a/@href').getall()
        data = {}
        for url in urls:
            # info = {
            #     'url': "https://in.seamsfriendly.com"+url,
            # }
            yield scrapy.Request(url = "https://in.seamsfriendly.com"+url, callback = self.parse_page_contents, meta = {'data':data} )

    def parse_page_contents(self, response):
        data = response.meta['data']
        
        title = response.css(".ProductMeta__Title.Heading::text").extract_first()
        discription = response.css(".ProductMeta__Description li::text").extract()
        price = response.css(".ProductMeta__Price::text").extract_first()
        image_urls = response.css(".Product__Slideshow img::attr(src)").extract()
        
        data['Title'] = title
        data['Discription'] = discription
        data['Price'] = price
        data["Image_Urls"] = image_urls            
            
        yield data  

