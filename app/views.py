from app import app
from flask import render_template
from .request import get_news

#views
@app.route('/')
def index():
    """
    :return: index page and its data
    """
    
    title = 'Home - For Current Global News'
    popular_news = get_news('everything')
    top_headlines = get_news('top-headlines')
    return render_template('index.html', title = title, popular = popular_news, top = top_headlines)