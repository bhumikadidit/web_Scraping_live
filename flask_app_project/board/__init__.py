from flask import Flask

from board import pages

def create_app():

    app = Flask(__name__)

    app.config['JSON_AS_ASCII'] = False  # <-- ADD: Ensures non-ASCII chars (like Nepali) aren't escaped

    app.register_blueprint(pages.bp)
    
    return app


