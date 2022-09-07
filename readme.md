Crawlpic Readme
===============
在[四川省建筑市场监管公共服务平台](http://sjfw.scjs.net.cn:8001/xxgx/Person/rList.aspx)搜索人员，对人员信息页进行网页全屏截图并保存的一个小工具

[readme.md](./readme.md)


项目概述
=========


### 需求来源
由于我妈做标书，需要在网站上搜索人员的证书信息并截图，将截图用于标书中，整个过程需要重复的搜索人员信息，截图，返回搜索，再截图循环往复
这让我萌生出想做一款工具来，仅通过输入所有要搜索的人员，然后程序自动去一个一个地将网页的信息截图并保存下来

### 技术选择
- 在java与python中做抉择，java的话，运行环境可能会不太友好，希望能够直接用，所以选择了**python3.9.13+PyQt5**进行一个界面的构建

- 对网页进行全屏截图使用了**selenium**
webdriver是用的[chromedriver105.0.5195.52_mac64_m1](http://chromedriver.storage.googleapis.com/index.html?path=105.0.5195.52/)的版本
如需其他版本，可根据自己的浏览器版本，在[chromederiver](http://chromedriver.storage.googleapis.com/index.html)自行下载

- 对网页爬取与解析使用的是**requests+bs4**

项目贡献
======

[DeIn221](https://github.com/DeIn221)

