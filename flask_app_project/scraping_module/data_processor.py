# scraping_module/data_processor.py
import csv
from datetime import datetime

def save_to_csv(data, filename, headers):
    """Save data to CSV (from your original code)."""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)

def process_for_json(notices):
    """
    Process notices for JSON response.
    Returns the list of dicts (simple pass-through for now).
    You could add sorting, filtering, or other logic here.
    """
    return notices

def filter_notices(notices, keyword=None, start_date=None, end_date=None):
    """
    Filter notices by keyword (in title) and date range.
    - keyword: String to search in titles (case-insensitive). If None or 'all', no filter.
    - start_date/end_date: datetime objects. If None, no date filter.
    Handles Nepali text correctly (no encoding issues).
    """
    filtered = []
    for notice in notices:
        # Keyword filter (case-insensitive substring match)
        if keyword and keyword.lower() not in ('', 'all'):
            if keyword.lower() not in notice['Title'].lower():
                continue
        
        # Date filter
        notice_date = datetime.strptime(notice['Date'], '%Y-%m-%d')
        if start_date and notice_date < start_date:
            continue
        if end_date and notice_date > end_date:
            continue
        
        filtered.append(notice)
    return filtered

def process_for_json_filter(notices, keyword=None, start_date=None, end_date=None):
    """
    Process notices for JSON, applying filters.
    Returns filtered list, preserving Nepali text.
    """
    filtered_notices = filter_notices(notices, keyword, start_date, end_date)
    return filtered_notices

