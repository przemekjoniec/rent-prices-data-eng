import psycopg2

def get_market_report():
    try:
        conn = psycopg2.connect(
            host="localhost", database="real_estate",
            user="user", password="password", port="5432"
        )
        cur = conn.cursor()

        query = """
        SELECT 
            district, 
            ROUND(AVG(price), 2), 
            COUNT(*) 
        FROM raw_offers 
        WHERE price > 0 
        GROUP BY district 
        ORDER BY 2 DESC;
        """
        
        cur.execute(query)
        rows = cur.fetchall()

        print("\n--- RAPORT RYNKOWY: KRAKÓW ---")
        print(f"{'Dzielnica':<25} | {'Śr. Cena':<10} | {'Liczba ofert'}")
        print("-" * 55)
        
        for row in rows:
            print(f"{row[0]:<25} | {row[1]:<10} | {row[2]}")

    except Exception as e:
        print(f"Błąd analizy: {e}")
    finally:
        if conn: conn.close()

if __name__ == "__main__":
    get_market_report()