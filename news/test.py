from django.test import TestCase
from .models import User,Article,tags


class UserTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.david= User(first_name = 'David', last_name ='Mark', email ='markkariuki17@gmail.com')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.david,User))

# Testing Save Method
    def test_save_method(self):
        self.james.save_user()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)

class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.david= User(first_name = 'David', last_name ='Mark', email ='markkariuki17@gmail.com')
        self.david.save_user()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        User.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)    
