from selenium import webdriver
import math
import time 
from spider_paper import Paper
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re

def Selenium_op(url, chromeDriver_path = 'chromedriver', pagesize = 50, keyword='深度学习'):
    # 不打开浏览器模拟
    # option = webdriver.ChromeOptions()
    # option.add_argument("headless")
    # driver = webdriver.Chrome(executable_path=chromeDriver_path,chrome_options=option)
    regex = '^\d{4}(\-)\d{2}(\-)\d{2}$'
    driver = webdriver.Chrome(executable_path=chromeDriver_path)
    driver.get(url)
    # 计算总共有几页
    searchItem_num = int(driver.find_element_by_css_selector('.BatchOper_result_show span').text)
    page_num = math.ceil(searchItem_num/pagesize)
    if page_num>=100:
        page_num = 100
    count = 0
    for i in range(page_num):
        resultList = driver.find_elements_by_class_name('ResultList')
        for j in range(len(resultList)):
            try:
                paper = Paper()
                paper.title = resultList[j].find_element_by_css_selector('.title a').text
                paper.url = resultList[j].find_element_by_css_selector('.title a').get_property('href')
                authorList = resultList[j].find_elements_by_css_selector('.author a')
                for k in range(len(authorList)):
                    paper.author+=authorList[k].text + ' '
                paper.source = resultList[j].find_element_by_css_selector('.Source a').text 
                paper.summary = resultList[j].find_element_by_css_selector('.summary').text
                # 获取 时间
                response = urllib.request.urlopen(paper.url).read()
                soup = BeautifulSoup(response, 'lxml')
                c = soup.select('.info_right')
                s = c[-3].text 
                date = ''
                for i in range(len(s)):
                    if s[i].isdigit() or s[i] == '-':
                        date+=s[i]
                paper.date = date
                if re.match(regex, paper.date) == None:
                    continue
                paper.printFile(keyword = keyword)
                paper.printf()
                print('now:' + str(count))
                count+=1
            except:
                continue
        js = 'var a = document.getElementsByClassName("searchPageWrap_next")[0].children[0].click()'
        driver.execute_script(js)
        time.sleep(5)
    driver.quit()
    return count

if __name__ == '__main__':
    Selenium_op('http://www.wanfangdata.com.cn/search/searchList.do?searchType=all&showType=detail&pageSize=50&searchWord=%E6%91%98%E8%A6%81%3A%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&isTriggerTag=')
