import re

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