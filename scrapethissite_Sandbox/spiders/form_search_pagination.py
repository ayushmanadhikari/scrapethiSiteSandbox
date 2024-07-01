import scrapy
from scrapethissite_Sandbox.items import teamStats

class FormSearchPaginationSpider(scrapy.Spider):
    name = "form_search_pagination"
    start_urls = ["https://www.scrapethissite.com/pages/forms/"]


    def parse(self, response):
        team = teamStats()

        #left to handle none cases for each xpath selector
    
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



# --> forms/page/1 --> parse(parses each row of the table.. returns item object for each row) -->  