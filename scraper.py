import requests
from bs4 import BeautifulSoup
import re

SEARCH_URL = "https://www.olx.pl/nieruchomosci/mieszkania/wynajem/krakow/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def get_list_offers(url):
    response = requests.get(url, headers=headers)
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

results = get_list_offers(SEARCH_URL)

# print(f"Pobrano {len(results)} ogłoszeń.")
# for r in results[:3]:
#    print(r)

def clean_price(price_str):
    if not price_str or "za darmo" in price_str.lower():
        return 0
    cleaned = re.sub(r'[^\d]', '', price_str)
    return int(cleaned) if cleaned else 0

def clean_location(location_str):
    parts = location_str.split(' - ')
    location = parts[0].split(', ')
    city = location[0] if len(location) > 0 else "Brak Lokalizacji"
    district = location[1] if len(location) > 1 else "Brak Dzielnicy"

    return city, district
def process_offer(raw_offer):
    city, district = clean_location(raw_offer['location'])

    return {
        'title': raw_offer['title'].strip(),
        'price': clean_price(raw_offer['price']),
        'city': city,
        'district': district,
        'url': raw_offer['url']
    }

raw_results = get_list_offers(SEARCH_URL)
cleaned_results = [process_offer(offer) for offer in raw_results]

for item in cleaned_results[:3]:
    print(item)