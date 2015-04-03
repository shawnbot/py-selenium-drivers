import os
from selenium import webdriver

SERVICE_URLS = {
    'sauce': 'http://%s:%s@ondemand.saucelabs.com:80/wd/hub'
}

WEBDRIVER_MAP = {
    'chrome':   webdriver.Chrome,
    'firefox':  webdriver.Firefox,
    # 'ie':       webdriver.InternetExplorer,
    'phantomjs': webdriver.PhantomJS,
    # 'safari':   webdriver.Safari
}

class DriverBuilder(object):
    def __init__(self, username=None, access_key=None):
        self.username = username
        self.access_key = access_key

    def build(self, spec, hub='sauce', *args, **kwargs):
        """
        """
        if spec in WEBDRIVER_MAP:
            return WEBDRIVER_MAP.get(spec)(*args, **kwargs)
        elif spec == 'remote':
            capabilities = {}
            capabilities.update(webdriver.DesiredCapabilities.CHROME)
        else:
            capabilities = {}
            capabilities.update(spec)
        capabilities.update(kwargs)
        return webdriver.Remote(
            desired_capabilities=capabilities,
            command_executor=self.get_hub_url(hub)
        )

    def get_hub_url(self, hub):
        """
        """
        if hub[0:4] == 'http':
            return hub % (self.username, self.access_key)
        return SERVICE_URLS.get(hub, '') % (self.username, self.access_key)
