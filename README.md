# Live Notice Scraper

A Flask-based web application for live scraping notices from the Pokhara Municipality website (https://pokharamun.gov.np/news-notices). It fetches notices, filters them by date and keywords, and returns the data as JSON with readable Nepali text.

## Features

- **Live Scraping**: Real-time data fetching on demand
- **Date Filtering**: Filter notices by date range
- **Keyword Search**: Search notices by keywords in titles
- **Nepali Text Support**: Proper handling of Devanagari text in JSON responses
- **Error Handling**: Robust error handling with retry mechanism
- **RESTful API**: Simple JSON endpoints for easy integration

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/bhumikadidit/web_Scraping_live.git
cd web_Scraping_live
```

2. **Create and activate virtual environment**
```bash
python -m venv flask_app_project/venv
# On Windows:
flask_app_project\venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install flask requests beautifulsoup4
```

## Usage

### Start the Flask App
```bash
python flask_app_project/rp_flask_board/board/__init__.py
```
The app runs on `http://localhost:5000`

### Available Endpoints

#### 1. Home Page
- `GET /` - Application homepage

#### 2. About Page
- `GET /about` - About information

#### 3. Scrape All Notices
- `GET /scrape` - Returns all notices from last 2 years

#### 4. Filtered Search
- `GET /scrape_filtered/<keyword>/<start_date>/<end_date>` - Search notices with filters

**Parameters:**
- `keyword`: Search term (use "all" for no keyword filter)
- `start_date`: Start date in YYYY-MM-DD format
- `end_date`: End date in YYYY-MM-DD format

**Example URLs:**
- `http://localhost:5000/scrape_filtered/schools/2023-01-01/2024-12-31`
- `http://localhost:5000/scrape_filtered/all/2023-01-01/2024-12-31`
- `http://localhost:5000/scrape_filtered/education/2024-01-01/2024-06-30`

## Advanced Features

### URL Encoding
For keywords with spaces or special characters, use URL encoding:
- "school notices" → `school%20notices`
- "महत्वपूर्ण" → encoded automatically by browsers

### Nepali Text Handling
All responses preserve Nepali text without Unicode escapes:
```json
{
  "Title": "गण्डकी बहुप्राविधिक क्याम्पसको सूचना",
  "Date": "2024-01-15"
}
```

## Project Structure
```
live_scraping/
├── flask_app_project/
│   ├── rp_flask_board/
│   │   └── board/
│   │       ├── static/
│   │       ├── templates/
│   │       └── __init__.py
│   └── scraper_modules/
│       ├── scraper.py
│       └── data_processor.py
└── README.md
```

## Response Format
All endpoints return JSON with consistent structure:
```json
{
  "status": "success",
  "count": 15,
  "notices": [
    {
      "Title": "Notice title in Nepali",
      "Date": "2024-01-15"
    }
  ]
}
```

## Error Handling
- **400**: Invalid date format
- **500**: Server errors during scraping
- All errors include descriptive messages

## Legal Notes
- Scrapes only publicly available data
- Respects website terms of service
- Includes delays to avoid server overload

## Troubleshooting
- **Empty results**: Check internet connection
- **Encoding issues**: Ensure UTF-8 headers are used
- **Connection errors**: App includes automatic retries

This project is maintained for educational and development purposes.
