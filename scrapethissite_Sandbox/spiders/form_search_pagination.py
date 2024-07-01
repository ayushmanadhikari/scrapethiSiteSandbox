import scrapy
from scrapethissite_Sandbox.items import teamStats

class FormSearchPaginationSpider(scrapy.Spider):
    name = "form_search_pagination"
    start_urls = ["https://www.scrapethissite.com/pages/forms/"]


    #for scraping each individual item/row from table in a single page 
    #follows the url to the next page
    def parse(self, response):
        team = teamStats()

        for item in response.xpath('//tr'):
            if item.xpath('td').get() is not None:
                team['name'] = item.xpath('td[@class="name"]/text()').get().strip()
                team['year'] = item.xpath('td[@class="year"]/text()').get().strip()
                team['wins'] = item.xpath('td[@class="wins"]/text()').get().strip()
                team['losses'] = item.xpath('td[@class="losses"]/text()').get().strip()
                team['ot_losses'] = item.xpath('td[@class="ot-losses"]/text()').get().strip()
                team['goals_for'] = item.xpath('td[@class="gf"]/text()').get().strip()
                team['goals_against'] = item.xpath('td[@class="ga"]/text()').get().strip()

                if item.xpath('td[@class="pct text-success"]/text()').get() is not None:
                    team['win_percent'] = item.xpath('td[@class="pct text-success"]/text()').get().strip()
                else: 
                    team['win_percent'] = item.xpath('td[@class="pct text-danger"]/text()').get().strip()

                if item.xpath('td[@class="diff text-success"]/text()').get() is not None: 
                    team['goal_diff'] = item.xpath('td[@class="diff text-success"]/text()').get().strip()
                else: 
                    team['goal_diff'] = item.xpath('td[@class="diff text-danger"]/text()').get().strip()

                yield team

        #follows the next page to continue scraping data there too 
        for next in response.xpath('//ul[@class="pagination"]'):
            next_page = next.xpath('li/a/@href').getall()
            for next in next_page[:len(next_page)-1]:
                yield response.follow(next, callback = self.parse)



# --> forms/page/1 --> parse(parses each row of the table.. returns item object for each row) -->  