# selenium_drivers
Helpers for creating [Selenium WebDriver] instances in Python!

1. In your environment: `pip install selenium_drivers`
2. In Python, either:
  * `import selenium_drivers` or
  * `from selenium_drivers import DriverBuilder`

Available drivers:
* `chrome` -> `webdriver.Chrome()`
* `firefox` -> `webdriver.Firefox()`
* `phantomjs` -> `webdriver.PhantomJS()`
* `ie` -> `webdriver.Ie()` (on Windows only)
* `remote` -> `webdriver.Remote()` (see below)

## Examples:
```python
from selenium_drivers import DriverBuilder

# the builder takes an optional remote username and access key
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
