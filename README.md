# selenium_drivers
Helpers for creating [Selenium WebDriver] instances in Python:

```python
from selenium_drivers import DriverBuilder

builder = DriverBuilder(username='your-sauce-username', access_key='access-key')

# create a webdriver.Chrome()
chrome = builder.build('chrome')

# or just call the builder:
chrome = builder('chrome')

# webdriver.Remote() instances:
remote = builder('remote', browserName='internet explorer', version='9.0')

# or as a dict:
remote = builder({'browserName': 'internet explorer', ...})

# the default service for remote drivers is Sauce Labs, but
# we also do BrowserStack:
remote = builder(capabilities, service='browserstack')
# and custom hub URLs:
remote = builder(capabilities, service='http://%s:%s@hub.example.com')
```

[Selenium WebDriver]: http://selenium-python.readthedocs.org/en/latest/api.html
