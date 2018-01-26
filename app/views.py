from flask import render_template
from app import app
from .request import get_news
#views
@app.route('/')
def index():

    """
    View root page function that returns the index page and its data
    """
    # Getting popular news
    business_news = get_news('business')
    print(business_news)
    entertainment_news = get_news('entertainment')
    print(entertainment_news)
    general_news = get_news('general')
    print(general_news)
    technology_news = get_news('technology')
    print (technology_news)
    title = 'Home - Welcome to news on the go.'

    return render_template('index.html',title = title,business=business_news,entertainment=entertainment_news,general=general_news,technology=technology_news)
@app.route('/news/<int:news_id>')
def news(news_id):
    """
    View news page function that returns news details page
    page and its data
    """
    title = f'You are viewing {news_id}'
    return render_template('news.html',title = title)
