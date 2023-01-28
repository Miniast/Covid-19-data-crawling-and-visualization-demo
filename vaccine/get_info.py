import selenium
from selenium import webdriver

path = 'D:\study\Python\Assignment_2\chromedriver.exe'
webdriver.Chrome(executable_path=path, options=webdriver.ChromeOptions())
url = 'https://ourworldindata.org/explorers/coronavirus-data-explorer?tab=table&time=2021-12-20&facet=none&Metric=People+vaccinated&Interval=Cumulative&Relative+to+Population=false&Color+by+test+positivity=false&country=USA~ITA~CAN~DEU~GBR~FRA'

browser = webdriver.Chrome()
browser.get(url)
browser.implicitly_wait(10)

info = browser.find_element_by_xpath('/html/body/main/div/div[3]/div/div[1]/div/table/tbody/tr[1]/td[1]')
print(info.text)
