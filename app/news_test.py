import unittest
from .models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the news class
    '''
    def setUp(self):
        '''
        Set up method that will run before every TestCase
        '''
        self.new_news = News('ABC News','Judge to rule Feb 6 on bid to scrap Assange arrest warrant','A British judge says she will rule next month on whether to scrap a U.K. arrest warrant for the WikiLeaks founder Julian Assange',http://abcnews.go.com/International/wireStory/assange-lawyers-court-bid-drop-arrest-warrant-52626181,http://a.abcnews.com/images/International/WireAP_bc6ec90e7bc647e08f8a59ea15f3c2d6_16x9_992.jpg,'2018-01-26T13:25:00Z')

        def test_instance(self):
            self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()
