import os
import unittest
import urllib2

from selenium import webdriver
from selenium_drivers import DriverBuilder

class DriverBuilderTestCase(unittest.TestCase):
    builder = None
    driver = None

    def setUp(self):
        username = os.environ.get('SAUCE_USERNAME', 'username')
        access_key = os.environ.get('SAUCE_ACCESS_KEY', 'access_key')
        self.builder = DriverBuilder(username, access_key)

    def tearDown(self):
        self.driver and self.driver.quit()

    def test_phantomjs(self):
        self.driver = self.builder.build('phantomjs')
        self.assertTrue(isinstance(self.driver, webdriver.PhantomJS))

    def test_firefox(self):
        self.driver = self.builder.build('firefox')
        self.assertTrue(isinstance(self.driver, webdriver.Firefox))

    def test_chrome(self):
        self.driver = self.builder.build('chrome')
        self.assertTrue(isinstance(self.driver, webdriver.Chrome))

    def xtest_safari(self):
        self.driver = self.builder.build('safari')
        self.assertTrue(isinstance(self.driver, webdriver.Safari))

    def xtest_ie(self):
        self.driver = self.builder.build('ie')
        self.assertTrue(isinstance(self.driver, webdriver.IE))

    def test_remote(self):
        try:
            self.driver = self.builder.build(
                'remote',
                browserName='internet explorer',
                version='9.0',
                os='Windows XP'
            )
        except urllib2.HTTPError, error:
            print('Unable to authenticate with username "%s", key "%s"; skipping remote test' % (self.builder.username, self.builder.access_key))
            return
        self.assertTrue(isinstance(self.driver, webdriver.Remote))

if __name__ == '__main__':
    unittest.main()
