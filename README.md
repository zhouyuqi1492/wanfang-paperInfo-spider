# 万方论文信息爬虫
本程序为基于selenium的万方论文信息爬虫。

**config.conf**为配置文件，其中包含了搜索关键词，搜索模式，资源类型，每页资源数。

**spider_main.py**为主文件，运行后对万方相应关键字的搜索结果进行爬取，存储至**keyword_data.txt**文件中( **深度学习_data.txt**为爬取结果样例）。

**spider_op.py**文件包含了利用selenium进行数据爬取的具体操作。

本程序运行还需要本机对应谷歌浏览器版本的**chromedriver**，镜像下载地址参考：http://npm.taobao.org/mirrors/chromedriver/



# wanfang-paperInfo-spider
This program is a selenium-based Wanfang paper information crawler.

**config.conf** is a configuration file, which contains search keywords, search mode, resource type, and number of resources per page.

**spider_main.py** is the main file. Running it we can get paperinfo corresponding to the keyword in config file, then we store the data in **keyword_data.txt** file (**deep learning_data.txt** is an example) .

The **spider_op.py** file contains specific operations for data crawling using selenium.

For this program to run, you need the **chromedriver** corresponding to the Google Chrome version in your machine. The mirror download address reference: http://npm.taobao.org/mirrors/chromedriver/

