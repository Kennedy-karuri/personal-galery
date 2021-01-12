from django.test import TestCase
from .models import Article,tags
# Create your tests here.
class CategoryTestClass(TestCase):
    def setUp(self):
        '''
        Method to be run in every beginning of the test
        '''
        self.search= Category(category='search')
    def test_instance(self):
        self.assertTrue(isinstance(self.search,Category))
    def tearDown(self):
        '''
        Method to clear the test that has been done on category
        '''
        Category.objects.all().delete()
    def test_save_method(self):
        '''
        Method to save category
        '''
        self.search.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category)>0)
    def test_delete_method(self):
        '''
        Method to delete the category
        '''
        self.delete_category('search')
        category = Category.objects.all()
        self.assertTrue(len(category)==0)
class ArticleTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.location = Location(name = "")
        self.location.save_location()
        self.gallery = gallery(id = 1,title = "test",description = "test description",location = self.location, article_url = "path/to/article")
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
    def test_save_image(self):
        self.article.save_article()
        self.article = article.objects.all()
        self.assertTrue(len(self.article) > 0)
    def test_get_article_by_id(self):
        self.article.save_article()
        self.article = article.get_article_by_id(1)
        self.assertTrue(isinstance(self.article,Article))
   
    def test_search_by_category(self):
        self.article.save_article()
        self.category = categories(name = "test")
        self.category.save_category()
        self.article = Article.get_article_by_id(1).categories.add(self.category)
        self.searched_article = Article.search_by_category('test')
        self.assertTrue(len(self.searched_article) > 0)
   