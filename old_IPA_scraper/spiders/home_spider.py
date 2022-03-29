import scrapy
from scrapy.http import HtmlResponse


class HomeSpider(scrapy.Spider):
    name = "home"

    def start_requests(self):
        home_url = "https://www.wulihub.com.cn/gc/JY1VKy/index.html"
        yield scrapy.Request(url=home_url, callback=self.parse)

    def parse(self, response: HtmlResponse, **kwargs):
        # 怀旧游戏
        titles = response.css(".allPlayGame > ul > li > a:nth-child(1)::attr(title)").getall()
        links = response.css(".allPlayGame > ul > li > a:nth-child(2)::attr(href)").getall()
        print(titles)
        print(links)
        # 应用专题
        # 游戏分类
        # 推荐游戏
        # 低栏
        pass
