import requests
from bs4 import BeautifulSoup
import json
import re

class WikipediaScraper:
    """
    A class used to scrape data from the Country Leaders API.

    Attributes
    ----------
    base_url : str
        The base URL of the Country Leaders API.
    country_endpoint : str
        The endpoint of the API for getting the list of countries.
    leaders_endpoint : str
        The endpoint of the API for getting the leaders of a country.
    cookies_endpoint : str
        The endpoint of the API for getting a cookie.
    leaders_data : dict
        A dictionary to store the data of the leaders.
    cookie : str
        The cookie for the API calls.

    Methods
    -------
    refresh_cookie():
        Refreshes the cookie for the API calls.
    get_countries():
        Gets the list of countries from the API.
    get_leaders(country):
        Gets the leaders of a country from the API and adds them to the leaders_data.
    """
    def __init__(self):
        """Initializes the WikipediaScraper with the base URL and endpoints."""
        
        self.base_url = "https://country-leaders.onrender.com"
        self.country_endpoint = "/countries"
        self.leaders_endpoint = "/leaders"
        self.cookies_endpoint = "/cookie"
        self.leaders_data = {}
        self.cookie = None

    def refresh_cookie(self):
        """
        Refreshes the cookie for the API calls.

        Returns
        -------
        requests.Response
            The response from the API call.
        """
        
        return requests.get(f"{self.base_url}{self.cookies_endpoint}")

    def get_countries(self):
        """
        Gets the list of countries from the API.

        Returns
        -------
        list
            The list of countries.

        Raises
        ------
        ValueError
            If the API call fails.
        """
        
        headers = {"user_cookie": self.cookie}
        response = requests.get(f"{self.base_url}{self.country_endpoint}", cookies=self.refresh_cookie().cookies)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f"Failed to fetch countries data. Status Code: {response.status_code}")

    def get_leaders(self, country):
        """
        Gets the leaders of a country from the API and adds them to the leaders_data.

        Parameters
        ----------
        country : str
            The country to get the leaders of.

        Raises
        ------
        ValueError
            If the API call fails.
        """
        
        headers = {"user_cookie": self.cookie}
        params = {'country': country}
        response = requests.get(f"{self.base_url}{self.leaders_endpoint}", cookies=self.refresh_cookie().cookies, params=params)
        if response.status_code == 200:
            leaders = response.json()
            self.leaders_data[country] = []

            for leader in leaders:
                wikipedia_url = leader.get("wikipedia_url")
                birth_date = leader.get("birth_date")
                first_name = leader.get("first_name")
                last_name = leader.get("last_name")
                if birth_date is not None:

                    birth_year = birth_date.split("-")
                else:
                    birth_year = ["9999"]

                if wikipedia_url and birth_year:
                    first_paragraph = self.get_first_paragraph(wikipedia_url, birth_year)
                    leader_info = {
                        "wikipedia_url": wikipedia_url,
                        "first_name": first_name,
                        "last_name": last_name,
                        "first_paragraph": first_paragraph
                    }
                    self.leaders_data[country].append(leader_info)
        elif response.status_code != 200:
            self.refresh_cookie
            print("Cookies refreshed")

        else:
            raise ValueError(f"Failed to fetch leaders data for {country}. Status Code: {response.status_code}")


    def get_first_paragraph(self, wikipedia_url, birth_year):
        """
    Scrapes the first paragraph of a leader's Wikipedia page that contains their birth year.

    Parameters
    ----------
    wikipedia_url : str
        The URL of the leader's Wikipedia page.
    birth_year : str
        The birth year of the leader.

    Returns
    -------
    str
        The first paragraph of the leader's Wikipedia page that contains their birth year.
        """
        
        r = requests.get(f"{wikipedia_url}").text
        soup = BeautifulSoup(r, "html.parser")
        paragraphs = soup.find_all('p')
        first_paragraph = ""
        
        for p in paragraphs:
            
            if birth_year[0] in p.text:
                first_paragraph = p.text
                break
            elif p.text is not None:
                first_paragraph = p.text
            else:
                print("Failed to retrieve first paragraph")

        return first_paragraph

    def to_json_file(self, filepath):
        """
    Saves the leaders_data to a JSON file.

    Parameters
    ----------
    filepath : str
        The path of the file to save the data to.
        """
        with open(filepath, 'w') as json_file:
            json.dump(self.leaders_data, json_file, indent = 4, separators=(',', ': '))