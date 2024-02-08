Wikipedia Scraper
This project is a Python script that scrapes data from https://country-leaders.onrender.com/docs and the Wikipedia pages of the leaders. The script retrieves the list of countries and their leaders from the API, then scrapes the first paragraph of each leader's Wikipedia page. The data is stored in a JSON file.

Installation# wikipedia_scraper

A) Installation

1) Clone the repository:
git clone https://github.com/yourusername/wikipedia-scraper.git

2) Navigate to the project directory:
cd wikipedia-scraper

3) Create a virtual environment:
python3 -m venv venv

4) Activate the virtual environment:
- On Windows, run: venv\Scripts\activate
- On Unix or MacOS, run: source venv/bin/activate

5) Install the requirements:
pip install -r requirements.txt

B) Usage

1) Ensure that you are in the project directory and your virtual environment is activated.
2) Run the script:
python main.py

3) The script will create a JSON file named leaders_data.json in the project directory. This file contains the data of the countries and their leaders, including the first paragraph of each leader's Wikipedia page.

C) Visuals
Here's an example of what the output JSON file looks like:
{
    "USA": [
        {
            "wikipedia_url": "https://en.wikipedia.org/wiki/Joe_Biden",
            "first_name": "Joe",
            "last_name": "Biden",
            "first_paragraph": "Joseph Robinette Biden Jr. (/ˈbaɪdən/ BY-dən; born November 20, 1942) is an American politician who is the 46th and current president of the United States. A member of the Democratic Party, he served as the 47th vice president from 2009 to 2017 under Barack Obama and represented Delaware in the United States Senate from 1973 to 2009."
        },
        ...
    ],
    ...
}

D) Files
main.py: This script creates a WikipediaScraper object, refreshes the cookie, gets the list of countries, and for each country, gets the leaders and adds the first paragraph of their Wikipedia page to the leaders data. Finally, it saves the leaders data to a JSON file.

scraper.py: This file contains the WikipediaScraper class, which is used to scrape data from the Country Leaders API. It has methods to refresh the cookie for the API calls, get the list of countries from the API, get the leaders of a country from the API and add them to the leaders data, scrape the first paragraph of a leader's Wikipedia page that contains their birth year, and save the leaders data to a JSON file.