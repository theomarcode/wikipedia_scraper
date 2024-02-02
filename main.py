from src.scraper import WikipediaScraper

def add_first_paragraph_to_leaders_data():
    """
    This function creates a WikipediaScraper object, refreshes the cookie, gets the list of countries,
    and for each country, gets the leaders and adds the first paragraph of their Wikipedia page to the leaders data.
    Finally, it saves the leaders data to a JSON file.
    """
    scraper = WikipediaScraper()
    scraper.refresh_cookie()  # Refresh the cookie for the API calls
    countries = scraper.get_countries()  # Get the list of countries
    print(countries)
    for country in countries:  # For each country
        scraper.get_leaders(country)  # Get the leaders
        for leader in scraper.leaders_data[country]:  # For each leader
            wikipedia_url = leader.get('wikipedia_url')  # Get the Wikipedia URL
            # Add the first paragraph of the leader's Wikipedia page to the leaders data
            first_paragraph = scraper.get_first_paragraph(wikipedia_url)
            leader['first_paragraph'] = first_paragraph
    scraper.to_json_file('leaders_data.json')  # Save the leaders data to a JSON file

add_first_paragraph_to_leaders_data()