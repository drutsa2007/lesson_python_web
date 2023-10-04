from selenium import webdriver

# # Chrome
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get('http://selenium.dev/')

# Chromium
# from selenium.webdriver.chrome.service import Service as ChromiumService
# from webdriver_manager.core.os_manager import ChromeType
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
# driver.get('http://selenium.dev/')
#
# # Brave
# from selenium.webdriver.chrome.service import Service as BraveService
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.os_manager import ChromeType
#
# driver = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
#
# # Edge
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
#
# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
# driver.get('http://selenium.dev/')
#
# # Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

o = Options()
o.add_experimental_option("detach", True)
# o.add_experimental_option("path", r'd:\geckodriver.exe')

firefox_services = FirefoxService(
    executable_path='d:\\geckodriver.exe',
    # port=3000,
    service_args=['--marionette-port', '2828', '--connect-existing']
)
driver = webdriver.Firefox(service=firefox_services)
driver.get('http://selenium.dev/')
