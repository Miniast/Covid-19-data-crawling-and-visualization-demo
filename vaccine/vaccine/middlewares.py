import random
import time

from scrapy import signals
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from scrapy.http import HtmlResponse
from vaccine.settings import USER_AGENT_LIST


class VaccineDownloaderMiddleware:

    def __init__(self):
        path = 'D:\study\Python\Assignment\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=path, options=webdriver.ChromeOptions())

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT_LIST)
        if user_agent:
            request.headers.setdefault('User-Agent', user_agent)
        self.driver.implicitly_wait(10)
        self.driver.get(request.url)

        time.sleep(3)
        click_item = self.driver.find_element_by_xpath("/html/body/main/div/form/div[1]/div[1]")
        click_item.click()
        time.sleep(3)

        if request.wait_until:
            WebDriverWait(self.driver, request.wait_time).until(
                request.wait_until
            )

        body = str.encode(self.driver.page_source)
        request.meta.update({'driver': self.driver})

        return HtmlResponse(
            self.driver.current_url,
            body=body,
            encoding='utf-8',
            request=request
        )
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

    def spider_closed(self, spider):
        spider.driver.quit()
