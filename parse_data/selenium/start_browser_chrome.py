from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# чтобы окно не закрывалось
o = Options()
o.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=o)
browser.get('http://selenium.dev/')

js = 'window.scrollTo(0, document.body.scrollHeight);'
browser.execute_script(js)

# закрытие окна
# browser.close()
