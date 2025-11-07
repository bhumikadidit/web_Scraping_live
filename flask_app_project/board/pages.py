# board/pages.py
from flask import Blueprint, render_template, Response  # Removed jsonify, added Response
import json  # Added for custom JSON encoding
import sys
import os
from datetime import datetime

# Add path to import scraper_modules (adjust if your file structure differs)
# From board/pages.py, path to scraper_modules is ../scraper_modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scraper_modules'))

from scraping_module.scraper import scrape_notices  # Import from scraper_modules
from scraping_module.data_processor import process_for_json, process_for_json_filter

bp = Blueprint("pages", __name__)

@bp.route("/", endpoint="index")
def home():
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    return render_template("pages/about.html")

# New route for live scraping (updated for UTF-8 JSON)
@bp.route("/scrape")
def scrape():
    """
    Endpoint to scrape notices live.
    Scrapes from the site, processes, and returns JSON with readable UTF-8.
    """
    try:
        notices = scrape_notices()  # Call the scraper
        processed_data = process_for_json(notices)  # Process for response
        # Use json.dumps with ensure_ascii=False for readable Nepali
        json_data = json.dumps({
            "status": "success",
            "count": len(processed_data),
            "notices": processed_data
        }, ensure_ascii=False)  # Forces UTF-8 without escapes
        response = Response(
            response=json_data,
            status=200,
            mimetype='application/json; charset=utf-8'  # Explicit UTF-8 header
        )
        return response
    except Exception as e:
        error_json = json.dumps({"status": "error", "message": str(e)}, ensure_ascii=False)
        return Response(error_json, status=500, mimetype='application/json; charset=utf-8')
    

@bp.route("/scrape_filtered/<keyword>/<start_date>/<end_date>")
def scrape_filtered(keyword, start_date, end_date):
    """
    Endpoint to scrape notices live with filters.
    - keyword: Filter notices containing this keyword (case-insensitive).
    - start_date, end_date: Date range in 'YYYY-MM-DD' format.
    Returns JSON with readable UTF-8.
    """
    # try:
    #     notices = scrape_notices()  # Call the scraper
    #     # Convert date strings to datetime objects
    #     from datetime import datetime
    #     sd = datetime.strptime(start_date, '%Y-%m-%d') if start_date.lower() != 'none' else None
    #     ed = datetime.strptime(end_date, '%Y-%m-%d') if end_date.lower() != 'none' else None
        
    #     processed_data = process_for_json_filter(notices, keyword, sd, ed)  # Process with filters
    #     json_data = json.dumps({
    #         "status": "success",
    #         "count": len(processed_data),
    #         "notices": processed_data
    #     }, ensure_ascii=False)  # Forces UTF-8 without escapes
    #     response = Response(
    #         response=json_data,
    #         status=200,
    #         mimetype='application/json; charset=utf-8'  # Explicit UTF-8 header
    #     )
    #     return response
    # except Exception as e:
    #     error_json = json.dumps({"status": "error", "message": str(e)}, ensure_ascii=False)
    #     return Response(error_json, status=500, mimetype='application/json; charset=utf-8')
    



    try:
        # Scrape all notices
        notices = scrape_notices()

        # Parse dates
        parsed_start = datetime.strptime(start_date, '%Y-%m-%d') if start_date.lower() != 'none' else None
        parsed_end = datetime.strptime(end_date, '%Y-%m-%d') if end_date.lower() != 'none' else None
    
    # Filter and process
        filtered_notices = process_for_json_filter(notices, keyword=keyword, start_date=parsed_start, end_date=parsed_end)
    
    # Return JSON with readable Nepali text
        json_data = json.dumps({
            "status": "success",
            "keyword": keyword,
            "start_date": start_date,
            "end_date": end_date,
            "count": len(filtered_notices),
            "notices": filtered_notices
        }, ensure_ascii=False)  # Preserves Nepali characters
        return Response(json_data, status=200, mimetype='application/json; charset=utf-8')

    except ValueError as e:
    # Invalid date format
        error_json = json.dumps({"status": "error", "message": f"Invalid date format in '{start_date}' or '{end_date}': {e}"}, ensure_ascii=False)
        return Response(error_json, status=400, mimetype='application/json; charset=utf-8')
    except Exception as e:
        error_json = json.dumps({"status": "error", "message": str(e)}, ensure_ascii=False)
        return Response(error_json, status=500, mimetype='application/json; charset=utf-8')