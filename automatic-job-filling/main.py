from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
chrome_driver = "D:\Selenium\chromedriver"
from_url = "https://docs.google.com/forms/d/e/1FAIpQLSfEvUvX-spbWrpfdUMgAgu-1a4Dw4jI6me8zHJBYVrMUuSOGg/viewform"

headers = {
    "accept-language": "en-US,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
# print(soup.prettify())
prices = soup.find_all(name="div", class_="list-card-price")
addresses = soup.find_all(name="address", class_="list-card-addr")
links = soup.find_all(name="a", class_="list-card-link")
price_list = []
address_list = []
link_list = []
for item in range(len(prices)):
    price_list.append(prices[item].getText())
    address_list.append(addresses[item].getText())
    link_list.append(links[item].get("href"))
# print(price_list)
# print(address_list)
# print(link_list)

driver = webdriver.Chrome(chrome_driver)
webpage = driver.get(from_url)
time.sleep(2)
for num in range(len(price_list)):
    answers = driver.find_elements_by_class_name('quantumWizTextinputPaperinputInput')
    answers[0].send_keys(price_list[num])
    answers[1].send_keys(address_list[num])
    answers[2].send_keys(link_list[num])
    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit.click()
    time.sleep(2)
    another_response = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()
    time.sleep(2)
