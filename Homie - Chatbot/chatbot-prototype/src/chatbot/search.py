class Search:
    def __init__(self, web_scraper):
        self.web_scraper = web_scraper

    def search_houses(self, criteria):
        # This method will use the web scraper to find houses based on the given criteria
        search_results = self.web_scraper.scrape_links(criteria)
        return search_results