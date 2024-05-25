from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Menjalankan Chrome dalam mode tanpa tampilan

# Inisialisasi WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Melakukan permintaan HTTP
url = 'https://www.cozymeal.com/'
driver.get(url)
html_content = driver.page_source
soup = BeautifulSoup(html_content, 'lxml')
rapih = soup.prettify()

links = rapih.find('div')
print(rapih)
# Menutup browser
driver.quit()
