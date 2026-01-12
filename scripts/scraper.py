import requests
from bs4 import BeautifulSoup

SEARCH_URL = "https://www.olx.pl/nieruchomosci/mieszkania/wynajem/krakow/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def get_list_offers(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    offers = soup.find_all('div', {'data-cy': 'l-card'})
    
    scraped_data = []
    for offer in offers:
        title = offer.find('h4').text if offer.find('h4') else "Brak tytułu"
        price_tag = offer.find('p', {'data-testid': 'ad-price'})
        price_raw = price_tag.text if price_tag else "0"
        loc_tag = offer.find('p', {'data-testid': 'location-date'})
        location_raw = loc_tag.text if loc_tag else "Brak lokalizacji"
        link_tag = offer.find('a')
        link = "https://www.olx.pl" + link_tag['href'] if link_tag else ""

        scraped_data.append({
            'title': title,
            'price': price_raw,
            'location': location_raw,
            'url': link
        })
    return scraped_data