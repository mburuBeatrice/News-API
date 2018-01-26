from app import app

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_articles_list = get_news_response['articles']
            news_articles = process_articles(news_articles_list)

    return news_articles

def process_articles(news_list):
    '''
    Function that processes the news articles and transform them
    to a list of objects

    Args:
        news_list:A list of dictionaries that contain news details

    Returns:
        news_articles:A list of news objects
    '''
    news_articles = []
    for news_item in news_list:
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')

        if urlToImage:
            news_object = News(author,title,description,url,urlToImage,publishedAt)
            news_articles.append(news_object)

    return news_articles
