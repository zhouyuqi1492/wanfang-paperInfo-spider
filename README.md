# wanfang-paperInfo-spider
本程序为基于selenium的万方论文信息爬虫。

**config.conf**为配置文件，其中包含了搜索关键词，搜索模式，资源类型，每页资源数。

**spider_main.py**为主文件，运行后对万方相应关键字的搜索结果进行爬取，存储至**keyword_data.txt**文件中( **深度学习_data.txt**为爬取结果样例。

本程序运行还需要对应谷歌浏览器版本的**chromedriver**，镜像下载地址参考：http://npm.taobao.org/mirrors/chromedriver/

