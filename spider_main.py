import os 
import math 
from configparser import ConfigParser
import spider_op
import urllib.parse

searchtype_dict = {'全部':'all', '期刊':'perio', '学位':'degree', '会议':'conference', '专利':'patent', '科研报告':'tech', '科研成果':'tech_result'}

# http://www.wanfangdata.com.cn/search/searchList.do?searchType=tech_result&showType=detail&pageSize=50&searchWord=%E6%91%98%E8%A6%81%3A%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&isTriggerTag=
if __name__ == '__main__':
    cf = ConfigParser()
    cf.read('config.conf', encoding='utf-8')
    keyword = cf.get('base', 'keyword')
    searchlocation = cf.get('base', 'searchlocation')
    searchtype = searchtype_dict[cf.get('base', 'searchtype')]
    pagesize = cf.getint('base', 'pagesize')
    
    link1 = 'http://www.wanfangdata.com.cn/search/searchList.do?'
    keyword_parse = urllib.parse.quote(searchlocation + ':' +keyword)
    link2 = 'searchType='+searchtype+'&showType=detail&pageSize='+str(pagesize)+'&searchWord='+keyword_parse+'&isTriggerTag='
    link = link1 + link2
    count = spider_op.Selenium_op(url = link, pagesize = pagesize, keyword = keyword)
    print('write items:' + str(count))




