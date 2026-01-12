# main.py
from scripts.scraper import get_list_offers, SEARCH_URL
from scripts.transform import process_offer
from scripts.database import save_to_db
from scripts.analysis import get_market_report

def run_pipeline():
    print("Start")
    
    raw_data = get_list_offers(SEARCH_URL)
    
    cleaned_data = [process_offer(offer) for offer in raw_data]
    
    save_to_db(cleaned_data)

    get_market_report()
    
if __name__ == "__main__":
    run_pipeline()