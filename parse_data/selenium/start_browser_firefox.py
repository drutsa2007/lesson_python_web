from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# чтобы окно не закрывалось
o = Options()
o.add_experimental_option("detach", True)

browser = webdriver.Firefox(options=o)
browser.get('http://selenium.dev/')

# закрытие окна
# browser.close()
