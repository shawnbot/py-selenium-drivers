import os
import unittest

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

    def test_sauce_url(self):
        builder = DriverBuilder('foo', 'bar')
        self.assertEqual(builder.get_hub_url('sauce'), 'http://foo:bar@ondemand.saucelabs.com:80/wd/hub')

    def test_browserstack_url(self):
        builder = DriverBuilder('foo', 'bar')
        self.assertEqual(builder.get_hub_url('browserstack'), 'http://foo:bar@hub.browserstack.com:80/wd/hub')

    def test_custom_hub_url(self):
        builder = DriverBuilder('foo', 'bar')
        url = 'http://%s:%s@example.com/?foo=bar'
        self.assertEqual(builder.get_hub_url(url), url % ('foo', 'bar'))

    def test_phantomjs(self):
        self.driver = self.builder.build('phantomjs')
        self.assertTrue(isinstance(self.driver, webdriver.PhantomJS))

    def test_call(self):
        self.driver = self.builder('phantomjs')
        self.assertTrue(isinstance(self.driver, webdriver.PhantomJS))

    def test_firefox(self):
        self.driver = self.builder.build('firefox')
        self.assertTrue(isinstance(self.driver, webdriver.Firefox))

    def test_chrome(self):
        self.driver = self.builder.build('chrome')
        self.assertTrue(isinstance(self.driver, webdriver.Chrome))

    def test_ie(self):
        try:
            self.driver = self.builder.build('ie')
        except Exception, err:
            print('Unable to create IE driver: %s' % err)
            return
        self.assertTrue(isinstance(self.driver, webdriver.Ie))

    def test_remote(self):
        try:
            self.driver = self.builder.build(
                'remote',
                browserName='internet explorer',
                version='9.0',
                os='Windows XP'
            )
        except Exception, error:
            print('Unable to authenticate with username "%s", key "%s"; skipping remote test' % (self.builder.username, self.builder.access_key))
            return
        self.assertTrue(isinstance(self.driver, webdriver.Remote))

if __name__ == '__main__':
    unittest.main()
