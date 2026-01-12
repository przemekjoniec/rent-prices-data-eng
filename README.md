# Real Estate Market Data Pipeline (Kraków)

A end-to-end Data Engineering pipeline designed to extract, transform, and load rental property data from OLX. The system is containerized, idempotent, and follows a modular architecture.

## 🚀 Key Features
- **Automated Web Scraping:** Extracts real-time rental offers from OLX using Python & BeautifulSoup.
- **Data Transformation:** Cleans raw HTML strings into structured data (Regex price parsing, city/district splitting).
- **Idempotent Loading (UPSERT):** Prevents data duplication using SQL `ON CONFLICT` logic based on unique URLs.
- **Modular Architecture:** Clean code structure separating extraction, transformation, and storage logic.
- **Containerized Database:** Fully managed PostgreSQL environment via Docker Compose.
- **Market Analysis:** Integrated SQL reporting layer to calculate average prices per district.

---

## 🛠 Tech Stack
* **Language:** Python 3.10+
* **Libraries:** BeautifulSoup4, Requests, Psycopg2
* **Database:** PostgreSQL 15
* **Infrastructure:** Docker, Docker Compose
* **CI/CD (Conceptual):** GitHub Actions for scheduled runs

---

## 🏗 Project Structure
```text
.
├── .github/workflows
│   ├── pipeline.yml   # Automation
├── scripts/
│   ├── scraper.py     # Extract: Web scraping logic
│   ├── transform.py   # Transform: Data cleaning & normalization
│   ├── database.py    # Load: PostgreSQL connection and UPSERT logic
│   └── analysis.py    # Gold Layer: SQL-based market reporting
├── main.py            # Pipeline Orchestrator
├── docker-compose.yml # Infrastructure as Code
└── requirements.txt   # Dependencies
```
-- -

## ⚙️ Setup & Installation
1. Prerequisities  
    - Docker & Docker Desktop installed.
    - Python 3.10+ installed.

2. Environment Setup
Clone the repository and install dependencies:
```text
   git clone https://github.com/przemekjoniec/rent-prices-data-eng
   cd real-estate-data-pipeline
   pip install -r requirements.txt
```
4. Launch Infrastructure
Start the PostgreSQL database and pgAdmin:
```text
    docker-compose up -d
```
6. Run the Pipeline
Execute the full ETL process:
```text
    python main.py
```
---

## 📊 Data Model & UPSERT Logic
The pipeline utilizes a Medallion-inspired architecture:

Bronze: Raw HTML data extraction.

Silver: Cleaned integers and split location strings.

Gold: Aggregated reports (Average price by district).

Handling Duplicates: The system uses the listing URL as a UNIQUE CONSTRAINT. If a scraper encounters a listing already present in the database, it performs an UPDATE on the price and timestamp instead of creating a duplicate.

## 📈 Sample Analysis Output
After running the pipeline, the system automatically generates a market report:  
<img width="397" height="334" alt="photo1" src="https://github.com/user-attachments/assets/25204b54-6b22-4e65-b2c6-c46b6c8af87a" />


---
Created as a part of a Data Engineering Portfolio by Przemysław Joniec
