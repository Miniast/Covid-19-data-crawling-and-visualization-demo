# Python大作业：新冠疫情数据分析

<center><div style='height:2mm;'></div><div style="font-family:华文楷体;font-size:14pt;">计算机科学与技术 张晏宁 2019213684</div></center>
<center><span style="font-family:华文楷体;font-size:9pt;line-height:9mm">北京邮电大学 计算机学院</span>
</center>

## 实验环境

- Windows 10 Professional 18363.1474 OS
- Python 3.9.7
  - scrapy 2.5.1
  - selenium 4.1.0
  - pandas 1.3.5
  - numpy 1.21.4
  - pyecharts 1.9.1
  - matplotlib 3.5.0
- Pycharm 2021.3

## 数据来源及内容

### 数据部分一

**来源：COVID-19 World Statistics:** https://covid.observer

**首页：**<img src="C:\Users\12944\AppData\Roaming\Typora\typora-user-images\image-20220111230059926.png" alt="image-20220111230059926" style="zoom: 33%;" />

<center><strong>图2.1 COVID-19 Wrold Statistics 首页</strong></center>

**内容：**2021年12月5日~20日，共计16天的新冠疫情数据(15天的数据在计算时共与16天有关，如要计算新增比例时)，存储在 **result_covid.csv** 文件中，主要内容如下（次要部分省略）

| area_name | date | tot_confrimed | new_confirmed | tot_deaths | death_rate | affected_rate |
| --------- | ---- | ------------- | ------------- | ---------- | ---------- | ------------- |
| 地区名称  | 日期 | 总确诊数      | 新确诊数      | 总死亡数   | 死亡率     | 确诊比例      |

**展示：**（以下数据为爬虫运行即可得到的数据原型）

**"result_covid.csv"**

```
area_id,area_name,date,tot_confirmed,new_confirmed,tot_deaths,death_rate,affected_population_rate
0,World,Dec 20,275659302,752318,5368801,1.9,3.5
0,World,Dec 19,274906984,478207,5361917,2.0,3.5
0,World,Dec 18,274428777,575868,5357639,2.0,3.5
0,World,Dec 17,273852909,728768,5351641,2.0,3.5
...
1,Afghanistan,Dec 20,157797,10,7335,4.6,0.41
1,Afghanistan,Dec 19,157787,42,7335,4.6,0.41
...
217,Zimbabwe,Dec 7,141601,2555,4713,3.3,0.97
217,Zimbabwe,Dec 6,139046,0,4710,3.4,0.95
217,Zimbabwe,Dec 5,139046,523,4710,3.4,0.95

```

### 数据部分二

**来源：Our World In Data:** https://ourworldindata.org/

**首页：**<img src="C:\Users\12944\AppData\Roaming\Typora\typora-user-images\image-20220111231111958.png" alt="image-20220111231111958" style="zoom:33%;" />

**内容：**2021年12月5日~20日，各地区的疫苗接种人数与接种率，存储在 **result_vaccine.csv** 文件中。

| area_name | tot_vaccined | tot_vaccined_rate |
| --------- | ------------ | ----------------- |
| 地区名称  | 总接种人数   | 总接种率          |

<center><strong>图2.2 Our World In Data 首页</strong></center>

**展示：**（以下数据由于在爬取过程中为保证数据安全完整，采用分页爬取不同列的方式，因此需要对爬虫生成的csv文件再处理将分页的数据结合，并对爬取到的原生数据如 **"123,456", Dec 5, 2021 1.4 billion,  2.0%** 等再进行提取处理, 再处理代码见 **6.2 Our World In Data** 爬虫）

**"result_vaccined.csv"**

```
area_name,tot_vaccined,tot_vaccined_rate
Afghanistan,4140000.0,10.4
Africa,182860000.0,13.31
Albania,1130000.0,39.2
Algeria,7060000.0,15.83
Andorra,57085.0,73.8
Angola,7420000.0,21.88
Anguilla,10079.0,66.64
...
Yemen,556652.0,1.83
Zimbabwe,4060000.0,26.9
```

## 数据分析和展示

以下所有图片均采用 pyecharts 绘制。若该国家数据缺省时（由数据来源造成）将被排除出统计，必要时按照0进行渲染。

### 15天中，全球新冠疫情的总体变化趋势

从数据中取出15天全球累计确诊病例的变化情况，绘制折线图。

![image-20220112070730184](C:\Users\12944\AppData\Roaming\Typora\typora-user-images\image-20220112070730184.png)

<center><strong>图3.1 World Trend - Confirmed Cases</strong></center>

### 15天中，每日新增确诊数累计排名前10个国家的每日新增确诊数据的曲线图

将15天新增数据求和排序，提取出对应的国家列表，再提取数据进行图表生成。

由数据，10个国家分别为: United States of America, United Kingdom, France, Germany, Russian Federation, Spain, Poland, Italy, Turkey, South Africa

![image-20220112074821325](C:\Users\12944\AppData\Roaming\Typora\typora-user-images\image-20220112074821325.png)

<center><strong>图3.2 Confrimed Top 10 Countries Trend</strong></center>

### 累计确诊数排名前10的国家名称及其数量

将12月20日的累计确诊数进行排序，提取排名前10的国家，绘制图表。

由数据，10个国家分别为: United States of America, India, Brazil, United Kingdom, Russian Federation, Turkey, France, Germany, Iran, Spain

![image-20220112082316559](C:\Users\12944\AppData\Roaming\Typora\typora-user-images\image-20220112082316559.png)

<center><strong>图3.3 Confrimed Top 10 Countries</strong></center>

### 用饼图展示各个国家的累计确诊人数的比例

提取累计确诊数据数据绘制饼图，将12名后的国家合并为"others"进行处理，并显示百分比。

![image-20220112090637335](C:\Users\12944\AppData\Roaming\Typora\typora-user-images\image-20220112090637335.png)

<center><strong>图3.4 Confrimed Percentage of Countries</strong></center>

### 累计确诊人数占国家总人口比例最高的10个国家

按照累计确诊人数占总人口的比例排序，选取最高的10个国家绘制图表。

由数据，10个国家分别为：Montenegro, Seychelles, Slovakia, Gibraltar, Georgia, Czechia, Slovenia, San Marino, Israel, Sint Maarten

![image-20220112092533357](C:\Users\12944\AppData\Roaming\Typora\typora-user-images\image-20220112092533357.png)

<center><strong>图3.5 Confrimed Rate of Countries</strong></center>

### 疫苗接种情况

提取各国在12月20日时的疫苗接种情况，进行地图绘制(由于数据源的原因，有部分数据缺省，单位为 million/billion 时采用补0策略，详见代码)。

![image-20220112221051884](C:\Users\12944\AppData\Roaming\Typora\typora-user-images\image-20220112221051884.png)

<center><strong>图3.6 Total Vaccined Condition</strong></center>

### 疫苗接种率最低的10个国家

提取疫苗接种率最低的10个国家进行图表绘制。

由数据，10个国家分别为：Democratic Republic of Congo, Halti, Chad, Yemen, South Sudan, Niger, Madagascar, Cameroon, Papua New Guinea, Tanzania

![image-20220112221545817](C:\Users\12944\AppData\Roaming\Typora\typora-user-images\image-20220112221545817.png)

<center><strong>图3.7 Total Vaccined Bottom 10 Countries</strong></center>

### 全球GDP前十名国家的累计确诊人数箱型图

查询得到，全球GDP前十名国家为：美国，中国，日本，德国，英国，印度，法国，意大利，加拿大，韩国。根据这一结果建立list，取出12月20日各国的累计确诊人数数据，绘制箱型图。

```python
country_list = ['United States of America', 'China', 'Japan', 'Germany', 'United Kingdom', 'India', 'France', 'Italy', 'Canada', 'South Korea']
```

**Echarts 官方答复：通常箱型图不进行平均值显示，因此 echarts 箱型图不允许添加平均值。**

**因此本题给出两种结果：pyecharts不含平均值图与matplotlib绘制的含平均值图。**

![image-20220112230745686](C:\Users\12944\AppData\Roaming\Typora\typora-user-images\image-20220112230745686.png)

<center><strong>图3.8.1 Vaccined Data of GDP Top 10 Countries by Pyecharts</strong></center>

![image-20220112231405329](C:\Users\12944\AppData\Roaming\Typora\typora-user-images\image-20220112231405329.png)

<center><strong>图3.8.2 Vaccined Data of GDP Top 10 Countries by Matplotlib</strong></center>

### 死亡率最高的10个国家

取12月20日的死亡率数据进行排序，得到死亡率最高的10个国家并绘制图表。

由数据，死亡率最高的10个国家/地区为：Vanuatu, Peru, Mexico, Sudan, Ecuador, Somalia, Syrian Arab Republic, Egypt, Taiwan, Liberia.

![image-20220112231851307](C:\Users\12944\AppData\Roaming\Typora\typora-user-images\image-20220112231851307.png)

<center><strong>图3.9 Death Rate of Top 10 Countries</strong></center>

## 疫情应对分析

考虑确诊人数和疫苗接种率，按照累计确诊数升序排列，疫苗接种率降序排列，分别各取出前15名，得到两图表如下：

![image-20220112233618554](C:\Users\12944\AppData\Roaming\Typora\typora-user-images\image-20220112233618554.png)

<center><strong>图4.1 Confirmed Rate of Bottom 12 Countries</strong></center>

![image-20220112233725155](C:\Users\12944\AppData\Roaming\Typora\typora-user-images\image-20220112233725155.png)

<center><strong>图4.2 Vaccined Rate of Top 12 Countries</strong></center>

**由以上两部分数据综合考虑，结合国家经济和人口状况，以及数据统计合理性（部分国家无力提供可靠的全部数据）可得全世界疫情应对最好的10个国家/地区：China, Singapore, South Korea, United Arab Emirates, Cuba, Portugal, Brunei, Chile, Ceyman Islands, Samoa.**

## 后5天疫情预测与对比分析

### 数据预测

利用前10天的累计确诊数据，采用最小二乘法进行线性回归分析和预测，并将结果输出如下，代码过程见“6 核心代码”。

其中拟合直线的线性回归方程：

![img](https://bkimg.cdn.bcebos.com/formula/a622e40cc910bfe0454f32228d11ef47.svg)

![img](https://bkimg.cdn.bcebos.com/formula/e95feaa16218549856a22159f867dcc6.svg)

![image-20220113003906516](C:\Users\12944\AppData\Roaming\Typora\typora-user-images\image-20220113003906516.png)

<center><strong>图5.1 预测数据，实际数据与差的绝对值</strong></center>

### 对比分析

由数据可以得出，预测相对差异基本稳定在1e-4级别。由于这一差异较小，认为预测结果良好。实际中的数据受到未来5天各国应对疫情状况（如医疗状况，财政经济状况等）、数据统计状况与其他疾病因素导致误差等现实条件的影响，因此与预测数据有一定差异，与实际情况相符。

## 核心代码

### COVID Observer爬虫

由于页数限制，由爬虫自动生成的相关非核心代码（如不需要 selenium 时的 middleware.py 和 settings.py 等）不再进行粘贴，按照通常爬虫自动生成并设置即可。

- covid/spiders/covidSpider.py

  ```python
  import copy
  import re
  import scrapy
  from covid.http import MyRequest
  from covid.items import CovidItem
  
  
  def get_integer(myinfo):
      if myinfo is not None:
          return int(''.join(c for c in str(myinfo) if c.isdigit()))
      else:
          return None
  
  
  def get_float(myinfo):
      if myinfo is not None:
          return float(re.findall(r"\d+\.?\d*", str(myinfo))[0])
      else:
          return None
  
  
  class CovidspiderSpider(scrapy.Spider):
      name = 'covidSpider'
      start_urls = ['https://covid.observer']
      area_abbr_list = ['World']
      area_name_list = ['World']
  
      def start_requests(self):
          for url in self.start_urls:
              yield MyRequest(url=url, callback=self.parse, dont_filter=True, cb_kwargs={'now_area_id': 0})
  
      def parse(self, response, **kwargs):
          item = CovidItem()
          info = response.xpath('//table/tbody')
          now_id = 1
  
          if info.xpath(f'./tr[{now_id}]/td[1]/text()').get() is not None:
              date_time = str(info.xpath(f'./tr[{now_id}]/td[1]/text()').get())
              while re.match("Dec", date_time) is None or not 5 <= int(re.findall('\d+', date_time)[0]) <= 20:
                  now_id += 1
                  date_time = str(info.xpath(f'./tr[{now_id}]/td[1]/text()').get())
              limit_id = now_id + 15
              daily_info = {}
              daily_info_list = []
              item['area_id'] = kwargs['now_area_id']
              item['area_name'] = self.area_name_list[kwargs['now_area_id']]
  
              while now_id <= limit_id:
                  daily_info['date'] = info.xpath(f'./tr[{now_id}]/td[1]/text()').get()
                  daily_info['tot_confirmed'] = get_integer(info.xpath(f'./tr[{now_id}]/td[2]/text()').get())
                  pre_confirmed = get_integer(info.xpath(f'./tr[{now_id + 1}]/td[2]/text()').get())
                  if daily_info['tot_confirmed'] is not None and pre_confirmed is not None:
                      daily_info['new_confirmed'] = daily_info['tot_confirmed'] - pre_confirmed
                  else:
                      daily_info['new_confirmed'] = None
                  daily_info['tot_deaths'] = get_integer(info.xpath(f'./tr[{now_id}]/td[5]/text()').get())
                  daily_info['death_rate'] = get_float(info.xpath(f'./tr[{now_id}]/td[8]/text()').get())
                  daily_info['affected_population_rate'] = get_float(info.xpath(f'./tr[{now_id}]/td[9]/text()').get())
                  daily_info_list.append(copy.deepcopy(daily_info))
                  now_id += 1
              item['covid_info'] = daily_info_list
              yield item
  
          if kwargs['now_area_id'] == 0:
              self.area_abbr_list.extend(response.xpath(f'/html/body/div[10]/div[2]/p/a/@href').extract())
              self.area_name_list.extend(response.xpath(f'/html/body/div[10]/div[2]/p/a/text()').extract())
              next_page_url = self.start_urls[0] + self.area_abbr_list[kwargs['now_area_id'] + 1]
              yield MyRequest(url=next_page_url, callback=self.parse, dont_filter=True,
                              cb_kwargs={'now_area_id': kwargs['now_area_id'] + 1})
          elif kwargs['now_area_id'] + 1 < len(self.area_abbr_list):
              next_page_url = self.start_urls[0] + self.area_abbr_list[kwargs['now_area_id'] + 1]
              yield MyRequest(url=next_page_url, callback=self.parse, dont_filter=True,
                              cb_kwargs={'now_area_id': kwargs['now_area_id'] + 1})
          pass
  ```
  
- covid/http.py

  ```python
  from scrapy import Request
  
  class MyRequest(Request):
      def __init__(self, wait_time=None, wait_until=None, *args, **cb_kwargs):
          self.wait_time = wait_time
          self.wait_until = wait_until
          super().__init__(*args, **cb_kwargs)
  ```

- covid/pipeline.py

  ```python
  # Define your item pipelines here
  #
  # Don't forget to add your pipeline to the ITEM_PIPELINES setting
  # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
  import csv
  
  # useful for handling different item types with a single interface
  from itemadapter import ItemAdapter
  
  
  class CovidPipeline:
      fieldname = ['area_id', 'area_name', 'date', 'tot_confirmed', 'new_confirmed', 'tot_deaths', 'death_rate',
                   'affected_population_rate']
  
      def __init__(self):
          self.file = open('result.csv', 'w', newline='')
          self.writer = csv.DictWriter(self.file, self.fieldname)
          self.writer.writeheader()
  
      def process_item(self, item, spider):
          info = {'area_id': item['area_id'], 'area_name': item['area_name']}
          for i in range(len(item['covid_info'])):
              info['date'] = item['covid_info'][i]['date']
              info['tot_confirmed'] = item['covid_info'][i]['tot_confirmed']
              info['new_confirmed'] = item['covid_info'][i]['new_confirmed']
              info['tot_deaths'] = item['covid_info'][i]['tot_deaths']
              info['death_rate'] = item['covid_info'][i]['death_rate']
              info['affected_population_rate'] = item['covid_info'][i]['affected_population_rate']
              self.writer.writerow(info)
          return item
  
      def close_spider(self, spider):
          self.file.close()
  ```

### Our World In Data爬虫

基本架构与 **6.1 COVID Observer爬虫** 相同，需使用 selenium 进行模拟，使用随机更换User-Agent，并对页面进行点击以保证页面刷新响应。

在得到数据后，由于 **2.2 数据部分二** 中提到的数据问题，需运行 process.py 进行再处理。

- vaccine/spiders/vaccineSpider.py

  ```python
  import copy
  import re
  import scrapy
  from vaccine.http import MyRequest
  from vaccine.items import VaccineItem
  
  
  class VaccinespiderSpider(scrapy.Spider):
      name = 'vaccineSpider'
      allowed_domains = ['ourworldindata.org']
      start_urls = [
          'https://ourworldindata.org/explorers/coronavirus-data-explorer?tab=table&time=2021-12-20&facet=none&Metric=People+vaccinated&Interval=Cumulative&Relative+to+Population=false&Color+by+test+positivity=false&country=USA~ITA~CAN~DEU~GBR~FRA']
      next_url = 'https://ourworldindata.org/explorers/coronavirus-data-explorer?tab=table&time=2021-12-20&facet=none&Metric=People+vaccinated&Interval=Cumulative&Relative+to+Population=true&Color+by+test+positivity=false&country=USA~ITA~CAN~DEU~GBR~FRA'
  
      def start_requests(self):
          for url in self.start_urls:
              yield MyRequest(url=url, callback=self.parse, dont_filter=True, cb_kwargs={'rate_info': 0})
  
      def parse(self, response, **kwargs):
          item = VaccineItem()
          vaccine_table = response.xpath('/html/body/main/div/div[3]/div/div[1]/div/table/tbody')
          now_id = 1
          now_area_name = vaccine_table.xpath(f'./tr[{now_id}]/td[1]/text()').get()
          while now_area_name is not None:
              item['area_name'] = now_area_name
              tmp = vaccine_table.xpath(f'./tr[{now_id}]/td[2]/text()').get()
              if kwargs['rate_info'] == 0:
                  item['tot_vaccined'] = vaccine_table.xpath(f'./tr[{now_id}]/td[2]/text()').get()
              else:
                  item['tot_vaccined_rate'] = vaccine_table.xpath(f'./tr[{now_id}]/td[2]/text()').get()
              now_id += 1
              now_area_name = vaccine_table.xpath(f'./tr[{now_id}]/td[1]/text()').get()
              yield item
  
          if kwargs['rate_info'] == 0:
              next_page_url = self.next_url
              yield MyRequest(url=next_page_url, callback=self.parse, dont_filter=True,
                              cb_kwargs={'rate_info': 1})
          pass
  
  ```
  
- vaccine/http.py

  同上
  
- vaccine/pipeline.py

  ```python
  import csv
  # useful for handling different item types with a single interface
  from itemadapter import ItemAdapter
  
  
  class VaccinePipeline:
      fieldname = ['area_name', 'tot_vaccined', 'tot_vaccined_rate']
  
      def __init__(self):
          self.file = open('result.csv', 'w', newline='')
          self.writer = csv.DictWriter(self.file, self.fieldname)
          self.writer.writeheader()
  
      def process_item(self, item, spider):
          self.writer.writerow(item)
          return item
  
      def close_spider(self, spider):
          self.file.close()
  
  ```

- vaccine/middlewares.py

  ```python
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
          return response
  
      def process_exception(self, request, exception, spider):
          pass
  
      def spider_opened(self, spider):
          spider.logger.info('Spider opened: %s' % spider.name)
  
      def spider_closed(self, spider):
          spider.driver.quit()
  
  ```
  
- vaccine/settings.py

  添加USER_AGENT_LIST以供使用，开启AUTOTHROTTLE，其他同上设置

  ```
  ...
  USER_AGENT_LIST = [
      "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
      "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
      "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
      "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
      "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
      "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
      "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
      "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
      "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
      "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
      "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
      "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
      "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
  ]
  ...
  AUTOTHROTTLE_ENABLED = True
  ...
  ```

- process.py

  ```python
  import re
  import pandas as pd
  
  headers = ['area_name', 'tot_vaccined', 'tot_vaccined_rate']
  f = open("result.csv", "r")
  
  f.readline()
  items = []
  while 1:
      item = []
      info = f.readline().split(',')
      if info is None or info[0] == '':
          break
      item.append(info[0])
      if info[1] == '':
          item.append(None)
      else:
          val = float(re.findall(r"\d+\.?\d*", info[1])[-1])
          if info[1].split(' ')[-1].replace('\n', '') == 'billion':
              val = val * 1000000000
              item.append(int(round(val, 0)))
          elif info[1].split(' ')[-1].replace('\n', '') == 'million':
              val = val * 1000000
              item.append(int(round(val, 0)))
          else:
              item.append(val)
      if info[2] == '\n':
          item.append(None)
      else:
          val = float(re.findall(r"\d+\.?\d*", info[2])[-1])
          item.append(val)
      items.append(item)
  
  wf = pd.DataFrame(columns=headers, data=items)
  af = wf.loc[(~wf['tot_vaccined'].isna()) & (wf['tot_vaccined_rate'].isna())]
  bf = wf.loc[(wf['tot_vaccined'].isna()) & (~wf['tot_vaccined_rate'].isna())]
  del af['tot_vaccined_rate']
  del bf['tot_vaccined']
  df = pd.merge(af, bf, how='inner', on='area_name')
  df.to_csv("result-vaccined.csv", index=None)
  
  ```

### 数据处理及数据展示

采用了较为面向工程的代码风格，在同一个 .py 文件中分函数模块实现各个功能以复用代码，减小代码长度，与图片中的数据命名相对，并添加一定注释以供理解。

```python
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Line
from pyecharts.charts import Pie
from pyecharts.charts import Map
from pyecharts.charts import Boxplot
from pyecharts.globals import ThemeType
import matplotlib.pyplot as plt

dc = pd.read_csv('result-covid.csv', encoding='utf-8')
dv = pd.read_csv('result-vaccined.csv', encoding='utf-8')

mtmp = dc.loc[dc['area_name'] == 'World']
date_list = mtmp['date'].values.tolist()
date_list.reverse()


# 15天中，全球新冠疫情的总体变化趋势
def world_trend() -> Line:
    tmp = dc.loc[dc['area_name'] == 'World']
    data_x = date_list
    data_y = tmp['tot_confirmed'].values.tolist()
    data_y.reverse()

    c = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1000px'))
            .add_xaxis(data_x)
            .add_yaxis("全球总确诊人数", data_y, is_smooth=True, is_connect_nones=True)
            .set_series_opts(
            areastyle_opts=opts.AreaStyleOpts(opacity=0.8)
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="World trend - Covid-19 pandamic"),
            xaxis_opts=opts.AxisOpts(
                name='日期',
                is_show=True,
                name_location='end',
                splitline_opts=opts.SplitLineOpts(
                    is_show=True,
                    linestyle_opts=opts.LineStyleOpts(
                        type_='dashed'
                    )
                )
            ),
            yaxis_opts=opts.AxisOpts(
                name='确诊人数',
                is_show=True,
                name_location='end',
                name_textstyle_opts=opts.TextStyleOpts(
                    padding=[0, 100, 0, 0]
                ),
                min_=264000000,
                splitline_opts=opts.SplitLineOpts(
                    is_show=True,
                    linestyle_opts=opts.LineStyleOpts(
                        type_='dashed'
                    )
                )
            )
        )
    )

    return c


# 15 天中，每日新增确诊数累计排名前 10 个国家的每日新增确诊数据的曲线图
def new_confirmed_top_10() -> Line:
    tmp = dc['new_confirmed'].groupby(dc['area_name']).sum()
    tmp.sort_values(inplace=True, ascending=False)
    country_list = tmp.index.tolist()[1:11]
    tmp = dc.loc[dc['area_name'].isin(country_list)]
    data_x = date_list

    c = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1000px'))
            .add_xaxis(data_x)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="New confirmed top 10 - Covid-19 pandamic"),
            xaxis_opts=opts.AxisOpts(
                name='日期',
                is_show=True,
                name_location='end',
                splitline_opts=opts.SplitLineOpts(
                    is_show=True,
                    linestyle_opts=opts.LineStyleOpts(
                        type_='dashed'
                    )
                )
            ),
            yaxis_opts=opts.AxisOpts(
                name='每日新增确诊数',
                is_show=True,
                name_location='end',
                name_textstyle_opts=opts.TextStyleOpts(
                    padding=[0, 100, 0, 0]
                ),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True,
                    linestyle_opts=opts.LineStyleOpts(
                        type_='dashed'
                    )
                )
            ),
            legend_opts=opts.LegendOpts(
                pos_left='right',
                pos_right='right',
                pos_top='bottom',
                pos_bottom='bottom'
            )

        )
    )
    for i in range(1, 11):
        tmp_y = tmp.loc[tmp['area_name'] == country_list[i - 1]]
        data_y = tmp_y['new_confirmed'].values.tolist()
        data_y.reverse()
        for j in range(len(data_y)):
            if data_y[j] <= 0:
                data_y[j] = None

        c_ = (
            Line(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1000px'))
                .add_xaxis(data_x)
                .add_yaxis(country_list[i - 1], data_y, is_smooth=True, is_connect_nones=True)
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        )
        c.overlap(c_)
    return c


# 累计确诊数排名前 10 的国家名称及其数量
def confirmed_top_10() -> Bar:
    tmp = dc.loc[dc['date'] == 'Dec 20']
    ttmp = tmp.sort_values(by='tot_confirmed', ascending=False)
    data_x = ttmp['area_name'].values.tolist()[1:11]
    data_y = ttmp['tot_confirmed'].values.tolist()[1:11]

    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1200px', height='600px'))
            .add_xaxis(data_x)
            .add_yaxis('tot_confirmed', data_y)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Total confirmed top 10 - Covid-19 pandamic"),
            xaxis_opts=opts.AxisOpts(
                name='国家',
                is_show=True,
                name_location='end',
                axislabel_opts=opts.LabelOpts(
                    interval=0
                )
            ),
            yaxis_opts=opts.AxisOpts(
                name='确诊人数',
                is_show=True,
                name_location='end',
                name_textstyle_opts=opts.TextStyleOpts(
                    padding=[0, 100, 0, 0]
                )
            ),
            legend_opts=opts.LegendOpts(
                pos_left='right',
                pos_right='right',
                pos_top='top',
                pos_bottom='top'
            )
        )
    )
    return c


# 用饼图展示各个国家的累计确诊人数的比例
def confirmed_percentage() -> Pie:
    tmp = dc.loc[dc['date'] == 'Dec 20']
    ttmp = tmp.sort_values(by='tot_confirmed', ascending=False)
    data_x = ttmp['area_name'].values.tolist()[1:13]
    data_y = ttmp['tot_confirmed'].values.tolist()[1:13]
    data_x.append('Others')
    sum_y = 0
    for it in data_y:
        sum_y += it
    data_y.append(ttmp.loc[ttmp['area_name'] == 'World']['tot_confirmed'].values[0] - sum_y)
    data = []
    for i in range(len(data_x)):
        data.append((data_x[i], data_y[i]))
    c = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1000px', height='600px'))
            .add(
            "",
            data,
            radius=[30, 180]
        )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b} : {d}%"))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Confirmed percentage - Covid-19 pandamic"),
            legend_opts=opts.LegendOpts(
                pos_right='right',
                pos_bottom='bottom'
            )
        )
    )
    return c


# 累计确诊人数占国家总人口比例最高的 10 个国家
def confirmed_rate_top_10() -> Bar:
    tmp = dc.loc[dc['date'] == 'Dec 20']
    ttmp = tmp.sort_values(by='affected_population_rate', ascending=False)
    data_x = ttmp['area_name'].values.tolist()[1:11]
    data_y = ttmp['affected_population_rate'].values.tolist()[1:11]
    for it in data_y:
        it = float("%.2f" % it)

    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1200px', height='600px'))
            .add_xaxis(data_x)
            .add_yaxis('affected_population_rate', data_y)
            .set_series_opts(label_opts=opts.LabelOpts(formatter='{c}.0%'))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Confirmed rate top 10 - Covid-19 pandamic"),
            xaxis_opts=opts.AxisOpts(
                name='国家',
                is_show=True,
                name_location='end',
                axislabel_opts=opts.LabelOpts(
                    interval=0
                )
            ),
            yaxis_opts=opts.AxisOpts(
                name='确诊人数占比',
                is_show=True,
                name_location='end',
                name_textstyle_opts=opts.TextStyleOpts(
                    padding=[0, 100, 0, 0]
                )
            ),
            legend_opts=opts.LegendOpts(
                pos_left='center',
                pos_right='center',
                pos_top='bottom',
                pos_bottom='bottom'
            )
        )
    )
    return c


# 疫苗接种情况（至少接种了一针及以上），请用地图形式展示
def tot_vaccined() -> Map:
    data_x = dv['area_name'].values.tolist()
    data_y = dv['tot_vaccined'].values.tolist()
    data = []
    for i in range(len(data_x)):
        if np.isnan(data_y[i]):
            data_y[i] = 0
        data.append((data_x[i], data_y[i]))
    print(data)
    c = (
        Map(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1200px', height='600px'))
            .add('tot_vaccined', data, "world")
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False), showLegendSymbol=False)
            .set_global_opts(
            title_opts=opts.TitleOpts(title='Total vaccined'),
            visualmap_opts=opts.VisualMapOpts(max_=100000000)
        )
    )
    return c


# 疫苗接种率（累计疫苗接种人数/国家人数）最低的 10 个国家
def vaccined_bottom_10() -> Bar:
    tmp = dv.sort_values(by='tot_vaccined_rate', ascending=True)
    data_x = tmp['area_name'].values.tolist()[1:11]
    data_y = tmp['tot_vaccined_rate'].values.tolist()[1:11]

    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1400px', height='600px'))
            .add_xaxis(data_x)
            .add_yaxis('vaccined_bottom_10', data_y)
            .set_series_opts(label_opts=opts.LabelOpts(formatter='{c}%'))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Vaccined rate bottom 10 - Covid-19 pandamic"),
            xaxis_opts=opts.AxisOpts(
                name='国家',
                is_show=True,
                name_location='end',
                axislabel_opts=opts.LabelOpts(
                    interval=0
                )
            ),
            yaxis_opts=opts.AxisOpts(
                name='接种人口比例',
                is_show=True,
                name_location='end',
                name_textstyle_opts=opts.TextStyleOpts(
                    padding=[0, 100, 0, 0]
                )
            ),
            legend_opts=opts.LegendOpts(
                pos_left='center',
                pos_right='center',
                pos_top='bottom',
                pos_bottom='bottom'
            )
        )
    )
    return c


# 全球 GDP 前十名国家的累计确诊人数箱型图，要有平均值
def GDP_top_10_confirmed() -> Boxplot:
    country_list = ['United States of America', 'China', 'Japan', 'Germany', 'United Kingdom', 'India', 'France',
                    'Italy', 'Canada', 'South Korea']
    tmp = dc.loc[dc['area_name'].isin(country_list)].loc[dc['date'] == 'Dec 20']
    data_x = ['Countries']
    data_y = tmp['tot_confirmed'].values.tolist()

    c = (Boxplot(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='800px', height='600px')))
    c.add_xaxis(data_x)
    c.add_yaxis('GDP_top_10_vaccined', c.prepare_data([data_y]))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="GDP top 10 vaccined - Covid-19 pandamic"),
        legend_opts=opts.LegendOpts(
            pos_left='right',
            pos_right='right',
            pos_top='top',
            pos_bottom='top'
        )
    )

    plt.boxplot(data_y, showmeans=True, vert=True, labels=['countries'])
    plt.show()

    return c


# 死亡率最高的 10 个国家
def death_rate_top_10() -> Bar:
    tmp = dc.loc[dc['date'] == 'Dec 20']
    ttmp = tmp.sort_values(by='death_rate', ascending=False)
    data_x = ttmp['area_name'].values.tolist()[1:11]
    data_y = ttmp['death_rate'].values.tolist()[1:11]
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1400px', height='600px'))
            .add_xaxis(data_x)
            .add_yaxis('death_rate_top_10', data_y)
            .set_series_opts(label_opts=opts.LabelOpts(formatter='{c}%'))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Death rate top 10 - Covid-19 pandamic"),
            xaxis_opts=opts.AxisOpts(
                name='国家',
                is_show=True,
                name_location='end',
                axislabel_opts=opts.LabelOpts(
                    interval=0
                )
            ),
            yaxis_opts=opts.AxisOpts(
                name='死亡率',
                is_show=True,
                name_location='end',
                name_textstyle_opts=opts.TextStyleOpts(
                    padding=[0, 100, 0, 0]
                )
            ),
            legend_opts=opts.LegendOpts(
                pos_left='center',
                pos_right='center',
                pos_top='bottom',
                pos_bottom='bottom'
            )
        )
    )
    return c


# 全世界应对新冠疫情最好的 10 个国家：分析图1
def confirmed_rate_bottom_12() -> Bar:
    tmp = dc.loc[dc['date'] == 'Dec 20']
    ttmp = tmp.sort_values(by='affected_population_rate', ascending=True)
    data_x = ttmp['area_name'].values.tolist()[1:13]
    data_y = ttmp['affected_population_rate'].values.tolist()[1:13]

    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1400px', height='600px'))
            .add_xaxis(data_x)
            .add_yaxis('tot_confirmed_rate', data_y)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Total confirmed rate bottom 12 - Covid-19 pandamic"),
            xaxis_opts=opts.AxisOpts(
                name='国家',
                is_show=True,
                name_location='end',
                axislabel_opts=opts.LabelOpts(
                    interval=0
                )
            ),
            yaxis_opts=opts.AxisOpts(
                name='确诊人数',
                is_show=True,
                name_location='end',
                name_textstyle_opts=opts.TextStyleOpts(
                    padding=[0, 100, 0, 0]
                )
            ),
            legend_opts=opts.LegendOpts(
                pos_left='right',
                pos_right='right',
                pos_top='top',
                pos_bottom='top'
            )
        )
    )
    return c


# 全世界应对新冠疫情最好的 10 个国家：分析图2
def vaccined_top_12() -> Bar:
    tmp = dv.sort_values(by='tot_vaccined_rate', ascending=False)
    data_x = tmp['area_name'].values.tolist()[1:13]
    data_y = tmp['tot_vaccined_rate'].values.tolist()[1:13]

    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1400px', height='600px'))
            .add_xaxis(data_x)
            .add_yaxis('vaccined_top_12', data_y)
            .set_series_opts(label_opts=opts.LabelOpts(formatter='{c}%'))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Vaccined rate top 12 - Covid-19 pandamic"),
            xaxis_opts=opts.AxisOpts(
                name='国家',
                is_show=True,
                name_location='end',
                axislabel_opts=opts.LabelOpts(
                    interval=0
                )
            ),
            yaxis_opts=opts.AxisOpts(
                name='接种人口比例',
                is_show=True,
                name_location='end',
                name_textstyle_opts=opts.TextStyleOpts(
                    padding=[0, 100, 0, 0]
                )
            ),
            legend_opts=opts.LegendOpts(
                pos_left='center',
                pos_right='center',
                pos_top='bottom',
                pos_bottom='bottom'
            )
        )
    )
    return c


# 针对全球累计确诊数，利用前 10 天采集到的数据做后 5 天的预测，并与实际数据进行对比
def covid_predict():
    tmp = dc.loc[dc['area_name'] == 'World']
    data_x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    tmp_y = tmp['tot_confirmed'].values.tolist()
    tmp_y.reverse()
    data_y = np.array(tmp_y[1:11])

    # 最小二乘法求解线性回归并进行分析
    # 拟合直线回归方程计算
    x_mean = np.mean(data_x)
    y_mean = np.mean(data_y)
    numerator = 0.0
    denominator = 0.0
    for i in range(len(data_x)):
        numerator += (data_x[i] - x_mean) * (data_y[i] - y_mean)
        denominator += np.square((data_x[i] - x_mean))
    a_ = numerator / denominator
    b_ = y_mean - a_ * x_mean

    # 预测数据和对比数据生成
    x_predic = [11, 12, 13, 14, 15]
    real_val = tmp_y[11:16]
    predic_val = []
    abs_dif = []
    rel_dif = []
    for it in x_predic:
        predic_val.append(it * a_ + b_)
    labels = ['Data', 'Dec 15', 'Dec 16', 'Dec 17', 'Dec 18', 'Dec 19']
    for i in range(len(real_val)):
        abs_dif.append(abs(predic_val[i] - real_val[i]))
        rel_dif.append(round(10000 * abs_dif[i] / real_val[i], 1))
        
    # 对比展示
    real_val.insert(0, 'real_value')
    predic_val.insert(0, 'predict_value')
    abs_dif.insert(0, 'abs_difference')
    rel_dif.insert(0, 'rel_difference(*1e-4)')
    data = [tuple(predic_val), tuple(real_val), tuple(abs_dif), tuple(rel_dif)]
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.max_rows', 20)
    pd.set_option('max_colwidth', 200)
    df = pd.DataFrame.from_records(data, columns=labels)
    print(df)


# world_trend().render()
# new_confirmed_top_10().render()
# confirmed_top_10().render()
# confirmed_percentage().render()
# confirmed_rate_top_10().render()
# tot_vaccined().render()
# vaccined_bottom_10().render()
# GDP_top_10_confirmed().render()
# death_rate_top_10().render()

# confirmed_rate_bottom_12().render()
# vaccined_top_12().render()

# covid_predict()

```