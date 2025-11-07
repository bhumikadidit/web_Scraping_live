# Flask Web Project Boilerplate

A scalable Flask web application boilerplate built from scratch. This project provides a solid foundation for building Flask applications with proper structure, templates, and static files.

## Features

- **Application Factory Pattern** for flexible app creation
- **Blueprint-based Architecture** for modular development  
- **Jinja2 Templates** with inheritance support
- **Static File Handling** (CSS, JS, images)
- **Virtual Environment** setup
- **Development Server** configuration

## Quick Start

### Prerequisites
- Python 3.7+
- Basic terminal knowledge
- Understanding of virtual environments

### Installation

1. **Clone and setup the project:**
```bash
# Create project directory
mkdir my_flask_project
cd my_flask_project

# Create and activate virtual environment
python -m venv venv

# On Windows:
.\venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install Flask
pip install Flask
```

2. **Project Structure:**
```
my_flask_project/
├── board/
│   ├── __init__.py
│   ├── pages.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── _navigation.html
│   │   └── pages/
│   │       ├── home.html
│   │       └── about.html
│   └── static/
│       └── styles.css
└── venv/
```

### Complex Terminal Commands You Might Forget

```bash
# Run Flask with custom app factory and debug mode
python -m flask --app board run --port 8000 --debug

# Alternative way to run with environment variables
export FLASK_APP=board
export FLASK_DEBUG=1
flask run --port 8000

# Install Flask in development mode (if using setup.py)
pip install -e .

# Freeze dependencies to requirements.txt
pip freeze > requirements.txt

# Create multiple directories in one command
mkdir -p board/templates/pages board/static
```

### Development

1. **Start the development server:**
```bash
python -m flask --app board run --port 8000 --debug
```

2. **Visit your application:**
- Home page: http://localhost:8000
- About page: http://localhost:8000/about

## Project Structure Explained

- `board/__init__.py` - Application factory
- `board/pages.py` - Blueprint for page routes
- `templates/` - Jinja2 templates with inheritance
- `static/` - CSS, JavaScript, and image files

## Documentation

For detailed explanations and step-by-step instructions, check out the full tutorial:
[**Build a Scalable Flask Web Project From Scratch**](https://realpython.com/flask-project/)

## Next Steps

- Add a database (SQLite, PostgreSQL)
- Implement user authentication
- Add form handling
- Deploy to production

## License

This project follows the tutorial from Real Python. Feel free to use as a starting point for your own Flask applications.

---

*Built with Flask - The Python micro framework for web development*
