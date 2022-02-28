import scrapy

class FilmesSpider(scrapy.Spider):
    name = 'filmes'
    start_urls = [
        'https://www.metacritic.com/browse/movies/score/metascore/all/filtered'
    ]
    
    def parse(self, response):
        for filme in response.css('table.clamp-list tr'):
            yield{
                'imagem': filme.css('td.clamp-image-wrap a img::attr("src")').get(),
                'nome': filme.css('td.clamp-summary-wrap a.title h3::text').get(),
                'descricao': filme.css('td.clamp-summary-wrap div.summary::text').get()
            }
        
    
    
