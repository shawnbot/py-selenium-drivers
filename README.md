# selenium_drivers
Helpers for creating [Selenium WebDriver] instances in Python:

```python
from selenium_drivers import DriverBuilder

builder = DriverBuilder(username='your-sauce-username', access_key='access-key')

# create a webdriver.Chrome()
chrome = builder.build('chrome')

# or just call the builder:
chrome = builder('chrome')
```

[Selenium WebDriver]: http://selenium-python.readthedocs.org/en/latest/api.html
