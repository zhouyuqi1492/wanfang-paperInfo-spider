# wanfang-paperInfo-spider
This program is a selenium-based Wanfang paper information crawler.

**config.conf** is a configuration file, which contains search keywords, search mode, resource type, and number of resources per page.

**spider_main.py** is the main file. Running it we can get paperinfo corresponding to the keyword in config file, then we store the data in **keyword_data.txt** file (**deep learning_data.txt** is an example) .

The **spider_op.py** file contains specific operations for data crawling using selenium.

For this program to run, you need the **chromedriver** corresponding to the Google Chrome version in your machine. The mirror download address reference: http://npm.taobao.org/mirrors/chromedriver/

