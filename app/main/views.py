from flask import render_template,request,redirect,url_for
from . import main
from .request import get_news,get_newsy
#views
@main.route('/')
def index():

    """
    View root page function that returns the index page and its data
    """
    # Getting popular news
    business_news = get_news('business')

    entertainment_news = get_news('entertainment')

    general_news = get_news('general')

    technology_news = get_news('technology')

    title = 'Home - Welcome to news on the go.'

    return render_template('index.html',title = title,business=business_news,entertainment=entertainment_news,general=general_news,technology=technology_news)
@main.route('/news/<int:news_id>')
def news(news_id):
    """
    View news page function that returns news details page
    page and its data
    """
    newsy = get_newsy(id)
    title = f'You are viewing {news_id}'
    return render_template('news.html',title = title)
