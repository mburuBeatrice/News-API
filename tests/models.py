class News:
    '''
    News class to define News objects
    '''
    def __init__(self,author,title,description,url,urlToImage,PublishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.PublishedAt = PublishedAt
