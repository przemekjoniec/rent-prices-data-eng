import os
import psycopg2

def save_to_db(data_list):
    db_host = os.getenv('DB_HOST', 'localhost')
    db_name = os.getenv('DB_NAME', 'real_estate')
    db_user = os.getenv('DB_USER', 'user')
    db_pass = os.getenv('DB_PASS', 'password')
    db_port = os.getenv('DB_PORT', '5432')

    conn = None
    cur = None

    try:
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_pass,
            port=db_port
        )
        cur = conn.cursor()
        
        upsert_query = """
        INSERT INTO raw_offers (title, price, city, district, url)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (url) 
        DO UPDATE SET 
            price = EXCLUDED.price,
            scraped_at = CURRENT_TIMESTAMP;
        """
        
        for item in data_list:
            cur.execute(upsert_query, (
                item['title'], item['price'], 
                item['city'], item['district'], item['url']
            ))
        
        conn.commit()
        print(f"✅ Przetworzono {len(data_list)} rekordów (UPSERT zakończony).")
        
    except Exception as error:
        print(f"❌ Błąd bazy danych: {error}")
    finally:
        if cur: cur.close()
        if conn: conn.close()