from django.test import TestCase

# Create your tests here.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class MultiSelectFunctionalTests(TestCase):

    base_url = 'http://localhost:8000/tests'
    fixtures=['publications']
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

        #username_input = self.driver.find_element_by_name("username")
        #username_input.send_keys(user)
       
    def tearDown(self):
        self.driver.close()

    def testAddArticlePage(self):
    	"""As a visitor to the site, when I load the articles page, I see the 
    	publications in Selectize.js multiselect theme."""

    	self.driver.get('{0}{1}'.format(self.base_url,'/articles/'))
    	self.assertIn("Headline:", self.driver.find_element_by_tag_name('body').text)