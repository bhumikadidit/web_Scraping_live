import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta  # timedelta no longer needed, but kept if you want to add back later
import time

def scrape_notices(base_url="https://pokharamun.gov.np/news-notices", max_pages=100):
    """
    Scrape all notices (no date filtering here; filtering happens in data_processor.py).
    Returns a list of dicts with 'Title' and 'Date'.
    """
    all_notices = []
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0'})
    
    for page in range(max_pages):
        url = f"{base_url}?page={page}"
        print(f"DEBUG: Scraping page {page}: {url}")  # DEBUG: Show current page
        try:
            response = session.get(url, timeout=30)
            response.raise_for_status()
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.content, 'html.parser')
            rows = soup.find_all('div', class_='node-article')
            print(f"DEBUG: Found {len(rows)} 'node-article' divs on page {page}")  # DEBUG: Check if divs are found
            if not rows:
                print(f"DEBUG: No 'node-article' divs found on page {page}, breaking")  # DEBUG: Why it stops
                break
            for row in rows:
                title_elem = row.find('h2')
                title = title_elem.find('a').text.strip() if title_elem and title_elem.find('a') else None
                date_elem = row.find('span', {'property': 'dc:date dc:created'})
                date_str = date_elem.text.strip() if date_elem else None
                print(f"DEBUG: Title: {title}, Date String: {date_str}")  # DEBUG: Show extracted data
                if date_str:
                    try:
                        date_part = date_str.split(',')[1].strip().split(' - ')[0].strip()
                        pub_date = datetime.strptime(date_part, '%m/%d/%Y')
                        print(f"DEBUG: Parsed Date: {pub_date}")  # DEBUG: Date parsing (no cutoff check)
                        if title:  # Only check for title existence; no date filter
                            all_notices.append({'Title': title, 'Date': pub_date.strftime('%Y-%m-%d')})
                            print(f"DEBUG: Added notice: {title}")  # DEBUG: Confirm addition
                    except ValueError as e:
                        print(f"DEBUG: Date parsing failed for '{date_str}': {e}")  # DEBUG: Parsing errors
            time.sleep(1)  # Respectful delay
        except requests.RequestException as e:
            print(f"DEBUG: Error on page {page}: {e}")  # DEBUG: Network errors
            break
    print(f"DEBUG: Total notices scraped: {len(all_notices)}")  # DEBUG: Final count
    return all_notices